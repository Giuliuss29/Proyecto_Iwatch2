from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestroFormularioDeCreacion(UserCreationForm):
    
    email = forms.EmailField()
    edad = forms.IntegerField(max_value=100, min_value=13)
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'edad' ,'password1', 'password2']
        help_texts = {key: ''for key in fields}