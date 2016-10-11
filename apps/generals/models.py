# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from userprofiles.models import User


class CustomPhoneNumber(models.Model):
    choices_phone_type = (
        ('M', _('Móvil')),
        ('W', _('Trabajo')),
        ('H', _('Casa')),
        ('P', _('Principal')),
        ('WF', _('Fax laboral')),
        ('PF', _('Fax personal')),
        ('L', _('Localizador')),
        ('O', _('Otro'))
    )
    phone_type = models.CharField(verbose_name=_('Tipo'), choices=choices_phone_type, max_length=12)
    phone_number = models.CharField(verbose_name=_('Número de teléfono'), max_length=15)
    extension = models.CharField(verbose_name=_('Extensión'), blank=True, max_length=5)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("phone_type","phone_number", "user")
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'


class CustomEmail(models.Model):
    choices_email_type = (
        ('H', _('Casa')),
        ('W', _('Trabajo')),
        ('O', _('Otro'))
    )
    email_type = models.CharField(verbose_name=_('Tipo'), choices=choices_email_type, max_length=8)
    email = models.EmailField(verbose_name=_('Correo electrónico'), max_length=255, unique=True)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('email_type', 'email', 'user')
        verbose_name = 'Correo electrónico'
        verbose_name_plural = 'Correos electrónicos'