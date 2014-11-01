# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ciudadano(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.get_full_name()

    class Meta:
        app_label = 'backend'

class Delegacion(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'backend'

class Lugar(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.ForeignKey('backend.TipoLugar')
    codigo_postal = models.IntegerField()
    delegacion = models.ForeignKey('backend.Delegacion')

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'backend'

class TipoLugar(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'backend'

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    latitud = models.DecimalField(max_digits=12, decimal_places=8)
    longitud = models.DecimalField(max_digits=12, decimal_places=8)
    lugar = models.ForeignKey('backend.Lugar')
    imagen = models.ImageField(upload_to='img-eventos/')
    votos = models.IntegerField()
    ciudadano = models.ForeignKey('backend.Ciudadano', blank=True, null=True)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    # Used to show how bad this event is, in 1-5 stars
    gravedad = models.IntegerField()

    def __unicode__(self):
        return self.title
        
    class Meta:
        app_label = 'backend'

class EventoVoto(models.Model):
    evento = models.ForeignKey('backend.Evento')
    ciudadano = models.ForeignKey('backend.Ciudadano')
    fecha_voto = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0} by {1}".format(
            evento.__unicode__(), ciudadano.__unicode__())
        
    class Meta:
        app_label = 'backend'
