
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('libros/', views.libros_view, name='libros_view'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('about/', views.about),
    path('hello/<str:username>',views.hello),
    path('project/', views.project),
    path('task/', views.task),
    path('crear_reseña/<int:libro_id>/', views.create_creacion, name='crear_resena'), 
    path('libros/agregar/', views.agregrar_libros, name='agregrar_libros'),
    path('libros/<int:reseñalibro_estado_lectura_id>/', views.resena_detallada, name='resena_detallada'),
    path('eliminar_reseña/<int:reseña_id>/', views.eliminar_reseña, name='eliminar_reseña'),
    path('editar_reseña/<int:reseña_id>/', views.editar_reseña, name='editar_reseña'),

    

    #path('book/<int:id>', views.book),

]
