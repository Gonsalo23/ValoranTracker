from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Inicio"),

    # DEBE ESTAR ASÍ:
    path("jugadores/<str:busqueda>/", views.jugadores, name="Jugadores"),
path("sugerencias/", views.sugerencias_busqueda, name="SugerenciasBusqueda"),
]