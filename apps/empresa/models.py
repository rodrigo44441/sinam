# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=False)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono1 = models.CharField(max_length=100, blank=True, null=True)
    telefono2 = models.CharField(max_length=100, blank=True, null=True)
    horario = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    mapa = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Datos SINAM"

    def __unicode__(self):
    	return self.nombre


class Faq(models.Model):
    pregunta = models.CharField(max_length=200)
    respuesta = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Compras (FAQ)"
    
    def __unicode__(self):
    	return self.pregunta


class Nosotros(models.Model):
    titulo = models.CharField(max_length=200)
    desarrollo = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Nosotros"
    
    def __unicode__(self):
        return self.titulo



class RedesSociales(models.Model):
    nombre = models.CharField(max_length=25)
    icono = models.CharField(max_length=25) # http://ionicons.com/#cdn
    link = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Redes Sociales"
    
    def __unicode__(self):
        return self.nombre