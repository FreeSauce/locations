# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0002_auto_20171019_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artpiece',
            name='title',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]