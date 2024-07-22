from django.urls import path
from . import views
from .views import Registrarse, logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/',logout_view,name= 'logout'),
    path('registro/', Registrarse.as_view(), name='registro')
]
  