from django.shortcuts import render
import folium
from services.models import Service


# Create your views here.
def home(request):
    services = Service.objects.all()  # Obtén todos los servicios
    return render(request, "core/home.html", {'services': services})  # Pasa los servicios al template

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")

def contact(request):
    return render(request, "core/contact.html")

def sample(request):
    return render(request, "core/sample.html")




def visita_view(request):
    # Coordenadas de la ubicación
    location = [-35.3071879, -71.5183838]  # Coordenadas correctas

    # Crear el mapa de Folium
    m = folium.Map(location=location, zoom_start=15)

    # Crear el enlace de Google Maps
    google_maps_url = f"https://www.google.com/maps?q={location[0]},{location[1]}"

    # Agregar un marcador en la ubicación con un popup que incluye el enlace
    folium.Marker(
        location,
        popup=(
            f"<strong>Av. San Rafael 335, San Rafael</strong><br>"
            f"<a href='{google_maps_url}' target='_blank'>Ver en Google Maps</a>"
        )
    ).add_to(m)

    # Guardar el mapa como un archivo HTML temporal
    map_html = m._repr_html_()  # Obtiene el HTML del mapa

    # Pasar el mapa a la plantilla
    return render(request, 'core/store.html', {'map_html': map_html})
