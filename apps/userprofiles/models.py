# coding=utf-8
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError (_("El correo electrónico es necesario"))
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self.create_user(email,
                                first_name=first_name,
                                last_name=last_name,
                                password=password,
                                **extra_fields)
        user.save(using=self._db)
        return user


def _user_has_perm(user, perm, obj):
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False


class User(AbstractBaseUser):

    """datos generales"""
    email = models.EmailField(verbose_name=_('Nombre de usuario'), max_length=50,unique=True, db_index=True)
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('Identificador'),
                                  help_text=_('Número de cliente'), max_length=6)
    first_name = models.CharField(verbose_name=_('Nombre'), max_length=50)
    last_name = models.CharField(verbose_name=_('Apellido Paterno'), max_length=50)
    last_mom_name = models.CharField(verbose_name=_('Apellido Materno'), max_length=50, blank=True, null=True)
    sex_options = (('F', _('Femenino')), ('M', _('Masculino')))
    sex = models.CharField(verbose_name=_('Sexo'), max_length=20, choices=sex_options)
    avatar = models.ImageField(verbose_name=_('Foto de perfil'), upload_to='avatars/', null=True, blank=True)

    """datos de contacto"""
    device_token = models.CharField(verbose_name=_('Token de dispositivo'),null=True, blank=True, max_length=200)
    device_type = models.CharField(verbose_name=_('Tipo de dispositivo'), null=True, blank=True, max_length=30,
                                   help_text=_('Android o IOS'))

    """datos de administración"""
    created = models.DateTimeField(verbose_name=_('Miembro desde'), editable=False, auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Actualizado', editable=False, auto_now=True)
    is_active = models.BooleanField(verbose_name=_('Activo'), default=True)
    is_admin = models.BooleanField(verbose_name=_('Administrador'), default=False)
    is_superuser = models.BooleanField(verbose_name=_('Super Usuario'), default=False)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)
    groups = models.ManyToManyField(Group, verbose_name=_('Grupos'), blank=True, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('Permisos'), blank=True,
                                              related_name='user_permissions')
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'sex']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __unicode__(self):
        return self.email

    @property
    def get_full_name(self):
        last_mom_name = ''
        if self.last_mom_name:
            last_mom_name = self.last_mom_name
        return '%s %s %s' % (self.first_name, self.last_name, last_mom_name)

    @property
    def get_short_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        if self.is_superuser:
            return True
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        return True

    def get_avatar_thumb(self, obj):
        if obj.avatar:
            return mark_safe(u'<img src="'+str(self.avatar.url)+'" />')
        return '(Sin imagen)'