# coding=utf-8
from django.contrib import admin
from django.utils.translation import ugettext as _

from generals.admin import CustomPhoneNumberaTabular, CustomEmailTabular
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        return qs.filter(is_staff=True)

    fieldsets = (
        ('Datos personales', {'fields': ('password', 'email', 'identifier','first_name', 'last_name', 'last_mom_name',
                                         'sex','avatar',)
                              }
         ),
        (_('Otros datos'), {'fields': ('created', 'is_active', 'is_staff', 'is_admin', 'groups', 'user_permissions',
                                 )
                      }
         ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name',
                       'is_staff', 'sex', 'password1', 'password2')}
         ),
    )
    readonly_fields = ('created', 'identifier', 'get_avatar_thumb')
    search_fields = ('email', 'first_name', 'last_name', 'last_mom_name', 'identifier')
    list_filter = ('sex','is_active', 'is_staff', 'is_admin',)
    list_display = ('get_avatar_thumb', 'email', 'get_full_name',)
    list_display_links = ('get_avatar_thumb', 'email', 'get_full_name',)
    inlines = [CustomPhoneNumberaTabular, CustomEmailTabular,]

    """funciones"""
    def get_full_name(self, obj):
        return obj.get_full_name

    get_full_name.short_description = 'Nombre completo'

    def get_avatar_thumb(self, obj):
        return obj.get_avatar_thumb
    get_avatar_thumb.short_description = 'Imagen de perfil'
    get_avatar_thumb.allow_tags = True

admin.site.register(User, UserAdmin)