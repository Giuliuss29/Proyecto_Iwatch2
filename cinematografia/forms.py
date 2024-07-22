from django import forms 
from .models import Peliculas, Series

class FormPelicula(forms.ModelForm):
    img = forms.ImageField(required=False)
    class Meta:
        model = Peliculas
        fields = ['titulo', 'subtitulo', 'img', 'cuerpo', 'director', 'genero']
        
class FormSeries(forms.ModelForm):
    img = forms.ImageField(required=False)
    class Meta:
        model = Series
        fields = ['titulo', 'subtitulo', 'img', 'cuerpo', 'director', 'genero', 'temporadas']
                


class BuscarPelis(forms.Form):
    peli = forms.CharField(max_length=20)
        