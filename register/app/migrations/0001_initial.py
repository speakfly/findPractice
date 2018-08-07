# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emial', models.EmailField(max_length=254)),
                ('position', models.CharField(default='实习 java', max_length=20)),
                ('addr', models.CharField(default='广州', max_length=20)),
                ('salary', models.IntegerField(default=3000)),
            ],
        ),
    ]
