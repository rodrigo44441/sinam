# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Empresa, Faq, RedesSociales, Nosotros


admin.site.register(Empresa)
admin.site.register(Faq)
admin.site.register(RedesSociales)
admin.site.register(Nosotros)
