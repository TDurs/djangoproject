from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

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

