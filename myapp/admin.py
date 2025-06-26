from django.contrib import admin
from .models import Project, Task, Generolibros, ClasificacionLibros, AlmacenLibros, EstadoDeLectura,ReseñaLibro

class HoraDeCracion(admin.ModelAdmin):
    readonly_fields = ("created",)


# Register your models here.
admin.site.register(Project)
admin.site.register(Task, HoraDeCracion)
admin.site.register(EstadoDeLectura)
admin.site.register(Generolibros)
admin.site.register(ClasificacionLibros)
admin.site.register(AlmacenLibros,HoraDeCracion)
admin.site.register(ReseñaLibro, HoraDeCracion)
