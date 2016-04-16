# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User
from wodly.wod.models import Wod

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class WodInline(admin.StackedInline):
    model = Wod
    extra = 0

@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    inlines = [WodInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "wod":
            kwargs["queryset"] = Wod.objects.filter(user=request.user)
        return super(UserAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
