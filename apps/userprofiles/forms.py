# coding=utf-8
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("No manera de ver la contraseña del usuario, "
                                                    "pero se puede cambiar la contraseña utilizando <a href=\"password/\">este formulario</a>."))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'sex', )

    def clean_password(self):
        return self.initial["password"]