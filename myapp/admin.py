from django.contrib import admin
from .models import Project, Task, Generolibros, ClasificacionLibros, AlmacenLibros, EstadoDeLectura,ReseñaLibro

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(EstadoDeLectura)
admin.site.register(Generolibros)
admin.site.register(ClasificacionLibros)
admin.site.register(AlmacenLibros)
admin.site.register(ReseñaLibro)
