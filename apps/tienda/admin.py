# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria, Articulo
#from .forms import AddCategory



admin.site.register(Categoria)
admin.site.register(Articulo)

'''class AdminCategoria(admin.ModelAdmin):
	form = AddCategory
	class Meta:
		model = Categoria
'''