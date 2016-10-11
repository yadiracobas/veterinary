from django.contrib import admin

from userprofiles.models import User
from .models import CustomEmail, CustomPhoneNumber


class CustomPhoneNumberaTabular(admin.TabularInline):
    model = CustomPhoneNumber

class CustomEmailTabular(admin.TabularInline):
    model = CustomEmail


admin.site.register(CustomPhoneNumber)
admin.site.register(CustomEmail)

