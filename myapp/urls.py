
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('libros/', views.libros_view, name='book'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('about/', views.about),
    path('hello/<str:username>',views.hello),
    path('project/', views.project),
    path('task/', views.task),
    path('libros/resena/', views.create_creacion, name='create_creacion'), 
    path('libro/agregar/', views.agregrar_libros, name='agregrar_libros'), 
    

    #path('book/<int:id>', views.book),

]
