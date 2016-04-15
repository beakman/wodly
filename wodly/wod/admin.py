from django.contrib import admin

from .models import Wod

@admin.register(Wod)
class WodAdmin(admin.ModelAdmin):
    fields = ('title', 'user')