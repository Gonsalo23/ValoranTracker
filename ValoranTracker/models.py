from django.db import models

# Create your models here.
class Jugador(models.Model):

    RANGO_CHOICES = (
        ('HIE', 'Hierro'),
        ('BRO', 'Bronce'),
        ('PLA', 'Plata'),
        ('ORO', 'Oro'),
        ('PLAT', 'Platino'),
        ('DIA', 'Diamante'),
        ('ASC', 'Ascendente'),
        ('INM', 'Inmortal'),
        ('RAD', 'Radiante'),
    )

    AGENTE_FAVORITO_CHOICES = (
        # Duelistas
        ('Jett', 'Jett'),
        ('Phoenix', 'Phoenix'),
        ('Neon', 'Neon'),
        ('Raze', 'Raze'),
        ('Reyna', 'Reyna'),
        ('Yoru', 'Yoru'),
        ('Iso', 'Iso'),

        # Iniciadores
        ('Breach', 'Breach'),
        ('Gekko', 'Gekko'),
        ('KAY/O', 'KAY/O'),
        ('Skye', 'Skye'),
        ('Sova', 'Sova'),
        ('Fade', 'Fade'),

        # Controladores
        ('Astra', 'Astra'),
        ('Brimstone', 'Brimstone'),
        ('Harbor', 'Harbor'),
        ('Omen', 'Omen'),
        ('Viper', 'Viper'),
        ('Clove', 'Clove'),
        ('Miks', 'Miks'),  # Miks como Controlador

        # Centinelas
        ('Chamber', 'Chamber'),
        ('Cypher', 'Cypher'),
        ('Killjoy', 'Killjoy'),
        ('Sage', 'Sage'),
        ('Deadlock', 'Deadlock'),
        ('Vyse', 'Vyse'),
        ('Veto', 'Veto'),  # Veto como Centinela
    )

    nickname = models.CharField(max_length=16)
    tag = models.CharField(max_length=5)
    rango = models.CharField(max_length=16, choices=RANGO_CHOICES)
    nivel = models.IntegerField()
    agente_favorito = models.CharField(max_length=16, choices=AGENTE_FAVORITO_CHOICES)

class Partida(models.Model):

    MAPA_CHOICES = (
        ('Corrode', 'Corrode'),
        ('Split', 'Split'),
        ('Sunset', 'Sunset'),
        ('Lotus', 'Lotus'),
        ('Haven', 'Haven'),
        ('Ascent', 'Ascent'),
        ('Breeze', 'Breeze'),
        ('Fracture', 'Fracture'),
        ('Icebox', 'Icebox'),
        ('Bind', 'Bind'),
        ('Pearl', 'Pearl'),
    )


    mapa = models.CharField(max_length=16, choices=MAPA_CHOICES)
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



