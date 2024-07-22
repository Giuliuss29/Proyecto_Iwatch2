from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import NuestroFormularioDeCreacion
from django.views import View
from django.contrib.auth import logout

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('prueba')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})     
    




class Registrarse(View):
    def get(self, request):
        formulario = NuestroFormularioDeCreacion()
        return render(request, "usuarios/registro.html", {'formulario': formulario})

    def post(self, request):
        formulario = NuestroFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Asegura que la redirección se hace correctamente
            return redirect('login') 
        else:
            # Si el formularioulario no es válido, renderiza de nuevo la página con el formularioulario y errores
            return render(request, "usuarios/registro.html", {'formulario': formulario})


def logout_view(request):
    logout(request)
    return render(request,'usuarios/logout.html')         
        
    