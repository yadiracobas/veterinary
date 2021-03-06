# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 19:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_type', models.CharField(choices=[('H', 'Casa'), ('W', 'Trabajo'), ('O', 'Otro')], max_length=8, verbose_name='Tipo')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electr\xf3nico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_type', models.CharField(choices=[('M', 'M\xf3vil'), ('W', 'Trabajo'), ('H', 'Casa'), ('P', 'Principal'), ('WF', 'Fax laboral'), ('PF', 'Fax personal'), ('L', 'Localizador'), ('O', 'Otro')], max_length=12, verbose_name='Tipo')),
                ('phone_number', models.CharField(max_length=15, verbose_name='N\xfamero de tel\xe9fono')),
                ('extension', models.CharField(blank=True, max_length=5, verbose_name='Extensi\xf3n')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
