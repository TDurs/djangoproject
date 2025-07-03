from django.http import HttpResponse, JsonResponse
from .models import Project, Task, ReseñaLibro, EstadoDeLectura, AlmacenLibros, LibroFavorito
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import CreateNewTask, AgregarLibro
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.contrib import messages
from django.views.decorators.http import require_POST






# Create your views here.
@login_required
def libros_view(request):
    libros = AlmacenLibros.objects.all()
    favoritos = []

    if request.user.is_authenticated:
        favoritos = LibroFavorito.objects.filter(usuario=request.user).values_list('libro_id', flat=True)
    return render(request, 'libros.html', {
        'libros': libros,
        'favoritos': favoritos,
    })

@login_required
def agregar_favorito(request, libro_id):
    libro = get_object_or_404(AlmacenLibros, id=libro_id)
    LibroFavorito.objects.get_or_create(usuario=request.user, libro=libro)
    return redirect('libros_view')  # o la URL donde se muestra la lista



@require_POST
@login_required
def toggle_favorito(request):
    libro_id = request.POST.get('libro_id')  
    libro = AlmacenLibros.objects.filter(id=libro_id).first()
    if not libro:
        return JsonResponse({'success': False, 'error': 'Libro no encontrado'}, status=404)

    favorito, creado = LibroFavorito.objects.get_or_create(usuario=request.user, libro=libro)
    if not creado:
        favorito.delete()
        return JsonResponse({'success': True, 'favorito': False})
    return JsonResponse({'success': True, 'favorito': True})


@login_required
def libros_favoritos(request):
    libros = AlmacenLibros.objects.filter(librofavorito__usuario=request.user)
    estados = EstadoDeLectura.objects.filter(user=request.user)
    estado_dict = {e.title.id: e.estado for e in estados}

    return render(request, 'libros_favoritos.html', {
        'libros': libros,
        'estados_lectura': estado_dict,
        'estado_choices': EstadoDeLectura.ESTADO_CHOICES,
    })

@require_POST
@login_required
def cambiar_estado_lectura(request):
    libro_id = request.POST.get('libro_id')
    nuevo_estado = request.POST.get('estado')

    libro = get_object_or_404(AlmacenLibros, id=libro_id)

    if nuevo_estado not in dict(EstadoDeLectura.ESTADO_CHOICES).keys():
        return JsonResponse({'success': False, 'error': 'Estado inválido'}, status=400)

    estado_obj, creado = EstadoDeLectura.objects.get_or_create(user=request.user, title=libro)
    estado_obj.estado = nuevo_estado
    estado_obj.save()

    return JsonResponse({'success': True, 'estado': nuevo_estado})


@login_required
def resena_detallada(request, reseñalibro_estado_lectura_id):
    libro = get_object_or_404(AlmacenLibros, pk=reseñalibro_estado_lectura_id)
    filtro = request.GET.get('filtro', 'recientes')

    reseñas = ReseñaLibro.objects.filter(estado_lectura=libro)

    if filtro == 'recientes':
        reseñas = reseñas.order_by('-fecha_reseña')
    elif filtro == 'antiguos':
        reseñas = reseñas.order_by('fecha_reseña')
    elif filtro == 'mejor_calificados':
        reseñas = reseñas.order_by('-calificacion', '-fecha_reseña')
    elif filtro == 'mios' and request.user.is_authenticated:
        reseñas = reseñas.filter(user=request.user)

    paginator = Paginator(reseñas, 5)
    page_number = request.GET.get('page')
    resenas_page = paginator.get_page(page_number)

    return render(request, 'resena_detallada.html', {
        'resena': resenas_page,
        'libro': libro,
        'filtro': filtro,
    })




@login_required
def create_creacion(request, libro_id):
    libro = get_object_or_404(AlmacenLibros, pk=libro_id)

    if request.method == "GET":
        return render(request, 'create_creacion.html', {
            'form': CreateNewTask(),
            'libro': libro,
        })
    else:
        form = CreateNewTask(request.POST)
        if form.is_valid():
            ReseñaLibro.objects.create(
                estado_lectura=libro,
                user=request.user,
                texto_reseña=form.cleaned_data['texto_reseña'],
                calificacion=int(form.cleaned_data['calificacion']),
            )
            return redirect(f'/libros/{libro.id}/')  # Vuelve a la vista de reseñas
        else:
            return render(request, 'create_creacion.html', {
                'form': form,
                'libro': libro,
            })
        

@login_required
def editar_reseña(request, reseña_id):
    reseña = get_object_or_404(ReseñaLibro, pk=reseña_id)

    if reseña.user != request.user:
        return HttpResponseForbidden("No puedes editar esta reseña.")

    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            reseña.texto_reseña = form.cleaned_data['texto_reseña']
            reseña.calificacion = int(form.cleaned_data['calificacion'])
            reseña.save()
            return redirect('resena_detallada', reseña.estado_lectura.id)
    else:
        form = CreateNewTask(initial={
            'texto_reseña': reseña.texto_reseña,
            'calificacion': reseña.calificacion,
        })

    return render(request, 'editar_reseña.html', {
        'form': form,
        'reseña': reseña
    })


        
@login_required
def eliminar_reseña(request, reseña_id):
    reseña = get_object_or_404(ReseñaLibro, pk=reseña_id)

    if reseña.user != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta reseña.")

    libro_id = reseña.estado_lectura.id
    reseña.delete()
    return redirect('resena_detallada', libro_id)

        

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)

                    #return HttpResponse('User creado satisfacoriamente')
                return redirect('libros_view')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    "error":'Username ya existe'
                }) 
                
        return render(request,'signup.html',{
                    'form': UserCreationForm,
                    "error":'Password no coinciden'
                }) 
    
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                'error':'Username or password esta incorrecto'
            })
        else:
            login(request,user)
            return redirect('libros_view')
             


@login_required
def agregrar_libros(request):
    if request.method == 'GET':
        return render (request, 'agregar_libros.html',{
            'form': AgregarLibro
        })
    else:
        try:
            form=AgregarLibro(request.POST)
            agregar=form.save(commit=False)
            agregar.save()
            return redirect('libros_view')
        except ValueError:
            return render (request, 'agregar_libros.html',{
            'form': AgregarLibro,
            'error': 'Proporcionar datos válido'
        })


def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 🔹 Obtiene el username del formulario (no 'name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validación: Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ya existe un usuario con ese nombre.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Ya existe un usuario con ese correo.")
        else:
            # Crea el usuario (username es obligatorio)
            user = User.objects.create_user(
                username=username,  # 🔹 Usa el username del formulario
                email=email,
                password=password,
                first_name='',  # Opcional (para evitar el error NOT NULL)
                last_name='',    # Opcional
            )
            login(request, user)  # Inicia sesión automáticamente
            return redirect('libros_view')  # Redirige al dashboard

    return render(request, 'registro.html')