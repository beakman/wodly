from django.contrib import admin

from .models import Wod, Exercise

class ExerciseInline(admin.StackedInline):
    model = Exercise
    extra = 0

@admin.register(Wod)
class WodAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'initial_note', 'foot_note', 'is_public')
    inlines = [ExerciseInline, ]