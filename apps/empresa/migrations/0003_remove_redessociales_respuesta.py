# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 00:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20170928_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redessociales',
            name='respuesta',
        ),
    ]
