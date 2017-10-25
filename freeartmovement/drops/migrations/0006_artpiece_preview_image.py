# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import drops.models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0005_auto_20171025_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpiece',
            name='preview_image',
            field=models.ImageField(default='stock/stealth_drop.png', upload_to=drops.models.build_a_path),
        ),
    ]
