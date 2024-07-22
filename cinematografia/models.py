from django.db import models
import os
from django.contrib.auth.models import User


def upload_to():
    return os.path.join('media/')



class Peliculas(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    img = models.ImageField(upload_to=upload_to(),null=True)
    cuerpo = models.CharField(max_length=9000)
    director = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField (auto_now_add=True)
    
class Series(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    img = models.ImageField(upload_to=upload_to(),null=True)
    cuerpo = models.CharField(max_length=9000)
    director = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    temporadas = models.DecimalField(decimal_places=1, max_digits=3)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField (auto_now_add=True)
    

    
