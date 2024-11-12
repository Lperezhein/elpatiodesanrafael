from django.urls import path
from . import views

urlpatterns = [
    #paths del core
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('sample/', views.sample, name="sample"),
    path('visita/', views.visita_view, name='visita'),  # Ruta para la vista con el mapa
]