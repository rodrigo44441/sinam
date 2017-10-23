# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=25, unique=True, null=False)

    def __unicode__(self):
    	return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField(editable=False)
    descripcion = models.TextField(blank=True)
    precio= models.DecimalField(decimal_places = 2, default=0.00, max_digits = 12)
    categoria = models.ForeignKey(Categoria)
    destacado = models.BooleanField(default=False)
    orden = models.IntegerField(default = 0)
    activo = models.BooleanField(default=True)
    mp = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='article_img', blank=True)
    image2 = models.ImageField(upload_to='article_img', blank=True)
    image3 = models.ImageField(upload_to='article_img', blank=True)
    image4 = models.ImageField(upload_to='article_img', blank=True)
    image5 = models.ImageField(upload_to='article_img', blank=True)
   
    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.categoria).lower().replace(' ','_'), slugify(self.nombre))).lower().replace(' ','_')
        super(Articulo, self).save(*args, **kwargs)

    def __unicode__(self):
    	return self.slug