# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190306_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtypes',
            name='typesort',
            field=models.IntegerField(),
        ),
    ]
