# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20160927_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='facilitator',
            name='slug',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tool',
            name='slug',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='training',
            name='slug',
            field=models.CharField(max_length=200),
        ),
    ]
