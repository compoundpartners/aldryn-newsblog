# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0024_newsblogjsrelatedplugin_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogjsrelatedplugin',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
    ]
