# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0003_auto_20171105_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artpiece',
            name='uuid',
            field=models.CharField(default='2a861fd4-a947-4420-8e01-57e638bd6707', max_length=36),
        ),
    ]