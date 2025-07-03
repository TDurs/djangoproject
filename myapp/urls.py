
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('libros/', views.libros_view, name='libros_view'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('crear_reseña/<int:libro_id>/', views.create_creacion, name='crear_resena'), 
    path('libros/agregar/', views.agregrar_libros, name='agregrar_libros'),
    path('libros/<int:reseñalibro_estado_lectura_id>/', views.resena_detallada, name='resena_detallada'),
    path('eliminar_reseña/<int:reseña_id>/', views.eliminar_reseña, name='eliminar_reseña'),
    path('editar_reseña/<int:reseña_id>/', views.editar_reseña, name='editar_reseña'),
    path('registro/', views.registro_view, name='registro'),
    path('libros/favorito/toggle/', views.toggle_favorito, name='toggle_favorito'),
    path('favoritos/', views.libros_favoritos, name='libros_favoritos'),
   


    

    #path('book/<int:id>', views.book),

]
