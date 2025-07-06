from django.http import HttpResponse, JsonResponse
from .models import Project, Task, ReseñaLibro, EstadoDeLectura, AlmacenLibros, LibroFavorito,Generolibros, ClasificacionLibros
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
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_GET
from django.contrib.admin.views.decorators import staff_member_required








# Create your views here.
@login_required
def libros_view(request):
    # Obtener todos los libros existentes
    libros = AlmacenLibros.objects.all().order_by('-id')  # Ordenados por ID descendente (los más nuevos primero)

    # Obtener géneros y clasificaciones (para el formulario)
    generos = Generolibros.objects.all()
    clasificaciones = ClasificacionLibros.objects.all()

    # Valores predeterminados para el formulario
    genero_predeterminado = generos.first()
    clasificacion_predeterminada = clasificaciones.first()

    if request.method == 'POST':
        try:
            # Código para guardar el nuevo libro (como ya lo tienes)
            libro = AlmacenLibros(
                titulo=request.POST.get('titulo'),
                autor=request.POST.get('autor'),
                genero_id=request.POST.get('genero', genero_predeterminado.id),
                año=request.POST.get('año'),
                clasificacion_id=request.POST.get('clasificacion', clasificacion_predeterminada.id),
                critica_de_internet=request.POST.get('critica_de_internet', 3),
                descripcion=request.POST.get('descripcion')
            )
            libro.save()
            messages.success(request, '¡Libro agregado con éxito!')
            return redirect('libros_view')  # Recarga la página para mostrar el nuevo libro
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    # Enviar todo al template
    context = {
        'libros': libros,  # <- Asegúrate de incluir esto
        'generos': generos,
        'clasificaciones': clasificaciones,
        'genero_predeterminado': genero_predeterminado,
        'clasificacion_predeterminada': clasificacion_predeterminada
    }
    return render(request, 'home.html', context)





@require_GET
def buscar_libros(request):
    query = request.GET.get('q', '')
    libros = AlmacenLibros.objects.filter(titulo__icontains=query)[:20]
    resultados = []
    
    for libro in libros:
        resultados.append({
            'titulo': libro.titulo,
            'autor': libro.autor,
            'imagen': libro.imagen.url if libro.imagen else '',
            'critica_de_internet': libro.critica_de_internet,
            'descripcion': libro.descripcion,
            'año': libro.año,
            'genero': str(libro.genero),
            'clasificacion': str(libro.clasificacion)
        })
    
    return JsonResponse(resultados, safe=False)

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

    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if form.is_valid():
            ReseñaLibro.objects.create(
                estado_lectura=libro,
                user=request.user,
                texto_reseña=form.cleaned_data['texto_reseña'],
                calificacion=int(form.cleaned_data['calificacion']),
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect(f'/libros/{libro.id}/')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
            return render(request, 'create_creacion.html', {
                'form': form,
                'libro': libro,
            })
    
    # GET request (no debería ocurrir con el modal)
    return redirect(f'/libros/{libro.id}/')
        

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
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('resena_detallada', reseña.estado_lectura.id)
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
    
    # Para GET requests (no debería ocurrir con el modal)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

        
@login_required
def eliminar_reseña(request, reseña_id):
    reseña = get_object_or_404(ReseñaLibro, pk=reseña_id)

    if reseña.user != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta reseña.")

    libro_id = reseña.estado_lectura.id
    reseña.delete()
    return redirect('resena_detallada', libro_id)

        
@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('libros_view')  # ← Nombre debe coincidir con urls.py
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })
    
def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request, 'registro.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request,'registro.html',{
                'form':AuthenticationForm,
                'error':'Username or password esta incorrecto'
            })
        else:
            login(request,user)
            return redirect('libros_view')
             


@login_required
def agregar_libros(request):
    genero_predeterminado = Generolibros.objects.get(id=1)  # Obtener el género predeterminado
    clasificacion_predeterminada = ClasificacionLibros.objects.get(id=1)  # Obtener clasificación predeterminada

    if request.method == 'POST':
        try:
            libro = AlmacenLibros(
                titulo=request.POST.get('titulo'),
                autor=request.POST.get('autor'),
                genero_id=request.POST.get('genero', genero_predeterminado.id),  # Valor predeterminado
                año=request.POST.get('año'),
                clasificacion_id=request.POST.get('clasificacion', clasificacion_predeterminada.id),  # Valor predeterminado
                critica_de_internet=request.POST.get('critica_de_internet', 3),  # Valor predeterminado 3
                descripcion=request.POST.get('descripcion')
            )
            libro.save()
            messages.success(request, '¡Libro agregado con éxito!')
            return redirect('#register')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    generos = Generolibros.objects.all()
    clasificaciones = ClasificacionLibros.objects.all()
    
    return render(request, 'home.html', {
    'generos': generos,
    'clasificaciones': clasificaciones,
    'genero_predeterminado': genero_predeterminado,  # Pasa el objeto completo
    'clasificacion_predeterminada': clasificacion_predeterminada  # Pasa el objeto completo
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


@require_POST
@user_passes_test(lambda u: u.is_staff)
def subir_imagen_libro(request, libro_id):
    libro = get_object_or_404(AlmacenLibros, id=libro_id)
    
    if 'imagen' not in request.FILES:
        return JsonResponse({'success': False, 'error': 'No se proporcionó imagen'}, status=400)
    
    libro.imagen = request.FILES['imagen']
    libro.save()
    
    return JsonResponse({
        'success': True,
        'imagen_url': libro.imagen.url
    })


@require_POST
@staff_member_required
def upload_book_image(request, libro_id):
    libro = get_object_or_404(AlmacenLibros, id=libro_id)
    
    if 'imagen' not in request.FILES:
        return JsonResponse({'success': False, 'error': 'No se proporcionó imagen'})
    
    imagen = request.FILES['imagen']
    
    # Validar tamaño y tipo de imagen si lo deseas
    if imagen.size > 5*1024*1024:  # 5MB máximo
        return JsonResponse({'success': False, 'error': 'La imagen es demasiado grande (máx. 5MB)'})
    
    libro.imagen = imagen
    libro.save()
    
    return JsonResponse({
        'success': True,
        'image_url': libro.imagen.url
    })