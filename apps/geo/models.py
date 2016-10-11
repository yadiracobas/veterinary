# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from userprofiles.models import User

"""Ejemplo:
            Country: Estados Unidos
            State: Florida
            County: Miami-Dade
            TownShip: Hialeah
 """


class Country(models.Model):
    country_code = models.CharField(max_length=100, db_index=True, verbose_name=_('Código'))
    country_name = models.CharField(max_length=100, db_index=True, verbose_name=_('País'))


class State(models.Model):
    city_name = models.CharField(max_length=100, verbose_name=_('Estado'), db_index=True)
    country = models.ForeignKey(Country, verbose_name=_('País'))
    phone_prefix = models.CharField(verbose_name=_('Prefijo de número de teléfono'), max_length=20, blank=True,
                                    null=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class County(models.Model):
    county_name = models.CharField(verbose_name='Condado', max_length=100, db_index=True)
    city = models.ForeignKey(State, verbose_name='Estado')

    class Meta:
        verbose_name = 'Condado'
        verbose_name_plural = 'Condados'


class TownShip(models.Model):
    town_name = models.CharField(max_length=100, verbose_name='Ciudad/Municipio', db_index=True)
    county = models.ForeignKey(County, verbose_name='Condado')
    zip_code = models.CharField(max_length=5, verbose_name='Código postal')

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'


class Address(models.Model):
    interior_num = models.CharField(verbose_name='Número interior', blank=True, null=True, max_length=5)
    exterior_num = models.CharField(verbose_name='Número exterior', max_length=5)
    street = models.CharField(max_length=100, verbose_name='Calle principal')
    town_ship = models.ForeignKey(TownShip, verbose_name='Localidad')
    type_direction = models.CharField(verbose_name='Tipo', help_text='Casa, trabajo, otro', max_length=10)
    user = models.ForeignKey(User)
