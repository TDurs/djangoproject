from django import forms
from .models import EstadoDeLectura, ReseñaLibro, Project, AlmacenLibros
from django.contrib.auth.models import User
from django.forms import ModelForm

class CreateNewTask(forms.Form):
    estado_lectura = forms.ModelChoiceField(
        queryset=AlmacenLibros.objects.all(),
        label="Estado de Lectura"
    )

    
    texto_reseña = forms.CharField(
        label="Reseña", 
        widget=forms.Textarea,
        required=True
    )

    calificacion = forms.ChoiceField(
        label="Calificación",
        choices=[(str(i), str(i)) for i in range(1, 6)],  # Las opciones deben ser strings si esperas texto en POST
        required=True
    )

class AgregarLibro(ModelForm):
    
    class Meta:
        model = AlmacenLibros
        fields = ['titulo','autor','genero','año','clasificacion','critica_de_internet']