# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria, Articulo
#from .forms import AddCategory


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'precio', 'orden', 'activo')
	list_display_links = ('id', 'nombre')
	#filter_vertical = ('activo')
	list_filter = ('activo', 'categoria')
	search_fields = ('nombre', 'descripcion')
	list_editable = ('orden',)


admin.site.register(Categoria)
#admin.site.register(Articulo)

'''class AdminCategoria(admin.ModelAdmin):
	form = AddCategory
	class Meta:
		model = Categoria
'''