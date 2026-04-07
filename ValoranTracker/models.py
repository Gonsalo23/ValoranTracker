from django.db import models

# Create your models here.
class Jugador(models.Model):
    nickname = models.CharField(max_length=16)
    tag = models.CharField(max_length=5)
    rango = models.CharField(max_length=16)
    nivel = models.IntegerField()
    agente_favorito = models.CharField(max_length=16)

class Partida(models.Model):

    mapa = models.CharField(max_length=16)
    kills = models.IntegerField()
    muertes = models.IntegerField()
    asistencias = models.IntegerField()
    resultado = models.CharField(max_length=16)
    fecha = models.DateTimeField()

class Estadisticas(models.Model):

    kills_totales = models.IntegerField()
    muertes_totales = models.IntegerField()
    asistencias_totales = models.IntegerField()
    winrate = models.FloatField()



