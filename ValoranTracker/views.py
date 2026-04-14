from idlelib.rpc import request_queue

from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, JsonResponse

from ValoranTracker.models import Jugador


def index(request):
    return render(request, 'inicio.html')

def jugadores(request):
    import urllib.parse
    busqueda = request.GET.get('q')
    busqueda_limpia = urllib.parse.unquote(busqueda)
    jugadores = []

    if "#" in busqueda_limpia:
        # Separamos "GonsaloMK" de "RBB"
        nickname_part, tag_part = busqueda_limpia.split("#", 1)
        # Buscamos en la BD el objeto que coincida con ambos
        jugador_obj = get_object_or_404(Jugador, nickname__iexact=nickname_part, tag__iexact=tag_part)
    else:
        jugador_obj = get_object_or_404(Jugador, nickname__iexact=busqueda_limpia)

        # Enviamos el objeto a perfil.html
    return render(request, 'busqueda_jugadores.html', {'jugador': jugador_obj})


def sugerencias_busqueda(request):
    query = request.GET.get('q', '')
    if query:
        # Buscamos jugadores que empiecen por lo que se ha escrito
        # icontains busca en cualquier parte, startswith solo al principio
        jugadores = Jugador.objects.filter(nickname__icontains=query)[:5]
        results = [f"{j.nickname}#{j.tag}" for j in jugadores]
    else:
        results = []

    return JsonResponse({'status': 'ok', 'results': results})