# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField(editable=False)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('destacado', models.BooleanField(default=False)),
                ('orden', models.IntegerField(default=0)),
                ('image1', models.ImageField(blank=True, upload_to='article_img')),
                ('image2', models.ImageField(blank=True, upload_to='article_img')),
                ('image3', models.ImageField(blank=True, upload_to='article_img')),
                ('image4', models.ImageField(blank=True, upload_to='article_img')),
                ('image5', models.ImageField(blank=True, upload_to='article_img')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Categoria'),
        ),
    ]
