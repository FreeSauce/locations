# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0002_hint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artpiece',
            name='uuid',
            field=models.CharField(default='<function uuid4 at 0x1022889d8>', max_length=36),
        ),
    ]
