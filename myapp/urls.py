
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('about/', views.about),
    path('hello/<str:username>',views.hello),
    path('project/', views.project),
    path('task/', views.task),
    path('create_creacion/', views.create_creacion), 

    #path('book/<int:id>', views.book),

]
