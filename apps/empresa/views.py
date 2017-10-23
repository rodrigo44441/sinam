# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Faq, Nosotros
#from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class FaqList(ListView):
    model = Faq
    queryset_list = Faq.objects.all().order_by('id').reverese()


class Nosotros(ListView):
    model = Nosotros
    queryset_list = Nosotros.objects.all().order_by('id').reverese()