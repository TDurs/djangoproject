from django.db import models
from django.core.exceptions import ValidationError





#Datos especificos
    
class Generolibros(models.Model):
    genero = models.CharField(max_length=200)
    def __str__(self):
        return self.genero
    
class ClasificacionLibros(models.Model):
    clasificacion = models.CharField(max_length=200)
    def __str__(self):
        return self.clasificacion





# Create your models here.
class Project(models.Model):
    ID_usuario = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    correo =  models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name



    
class AlmacenLibros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.ForeignKey(Generolibros, on_delete=models.CASCADE)
    año = models.CharField(max_length=200)
    clasificacion = models.ForeignKey(ClasificacionLibros, on_delete=models.CASCADE)
    critica_de_internet = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo + ' - ' + self.autor

class EstadoDeLectura(models.Model):
    title = models.ForeignKey(AlmacenLibros, on_delete=models.CASCADE)
    ESTADO_CHOICES = [
        ('leido', 'Leído'),
        ('leyendo', 'Leyendo'),
        ('quiero', 'Quiero Leer'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project}-{self.title} -{self.estado} "


class ReseñaLibro(models.Model):
    estado_lectura = models.ForeignKey(AlmacenLibros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Project, on_delete=models.CASCADE)
    texto_reseña = models.TextField()
    fecha_reseña = models.DateTimeField(auto_now_add=True)
    calificacion = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        help_text="Calificación del 1 al 5"
    )

    def __str__(self):
        return f"{self.estado_lectura} - {self.usuario.name} ({self.calificacion}/5)"






    