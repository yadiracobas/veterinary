# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, help_text='N\xfamero de cliente', primary_key=True, serialize=False, verbose_name='Identificador')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('last_mom_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Materno')),
                ('sex', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=20, verbose_name='Sexo')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Foto de perfil')),
                ('device_token', models.CharField(blank=True, max_length=200, null=True, verbose_name='Token de dispositivo')),
                ('device_type', models.CharField(blank=True, help_text='Android o IOS', max_length=30, null=True, verbose_name='Tipo de dispositivo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Miembro desde')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Administrador')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super Usuario')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='auth.Group', verbose_name='Grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_permissions', to='auth.Permission', verbose_name='Permisos')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]