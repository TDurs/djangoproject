from django.http import HttpResponse, JsonResponse
from .models import Project, Task, ReseñaLibro, EstadoDeLectura, AlmacenLibros
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import CreateNewTask, AgregarLibro
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



# Create your views here.

def libros_view(request):
    libros = AlmacenLibros.objects.all()
    return render(request, 'libros.html', {
        'libros': libros
    })

def hello(request, username):
    return HttpResponse("Hello world %s " % username)

def about(request):
    return render(request, 'about.html')

def project(request):   
   # project = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects': projects
    })

def task(request):
    #task = get_object_or_404(Task, title=title) 
    task = Task.objects.all()
    return render(request, 'tasks.html',{
        'task': task
    })

#def book(request, id):
    book = get_object_or_404(Book, id=id)
    return HttpResponse('book: %s'% book.title)

def create_creacion(request):
    if request.method == "GET":
        return render(request, 'create_creacion.html', {
            'form': CreateNewTask()
        })
    else:
        form = CreateNewTask(request.POST)
        if form.is_valid():
            reseña = ReseñaLibro.objects.create(
                estado_lectura=form.cleaned_data['estado_lectura'],
                user= request.user,
                texto_reseña=form.cleaned_data['texto_reseña'],
                calificacion=int(form.cleaned_data['calificacion']),
                )
            return redirect('/libro/')
        else:
            return render(request, 'create_creacion.html', {'form': form})
        

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
                return redirect('index')
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
            return redirect('index')
             

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
            return redirect('book')
        except ValueError:
            return render (request, 'agregar_libros.html',{
            'form': AgregarLibro,
            'error': 'Proporcionar datos válido'
        })