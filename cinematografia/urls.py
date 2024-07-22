from django.urls import path
from cinematografia import views
from .views import agregar_peli, agregar_series, about_me, prueba, detalle_pelicula, detalle_serie, perfil

urlpatterns = [
    
    path('', prueba, name='prueba'),
    path('pelicula/<int:pk>',detalle_pelicula,name='detalle_pelicula'),
    path('serie/<int:pk>',detalle_serie,name='detalle_serie'),
    path('peliculas/', views.Peliculas01.as_view(), name='peliculas'),
    path('series/', views.Series01.as_view(), name='series'),
    path('agregar_peli/', agregar_peli,name='agregar_peli'),
    path('agregar_series/', agregar_series,name='agregar_series'),
    path('about_me/', about_me,name= 'about_me'),
    path('<int:pk>/eliminar',views.EliminarPeli.as_view(),name='eliminar'),
    path('<int:pk>/eliminar_serie',views.EliminarSerie.as_view(),name='eliminar_serie'),
    path('pelicula/<int:pk>/editar', views.Editar.as_view(),name = 'editar'),
    path('serie/<int:pk>/editar_serie', views.EditarSerie.as_view(),name = 'editar_serie'),
    path('perfil/', perfil, name='perfil'),
    
    
    
    
]
