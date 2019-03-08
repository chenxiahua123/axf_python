# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': '注册用户信息',
            },
        ),
    ]
