from django.forms import models, widgets

from .models import Wod, Exercise


class WodForm(models.ModelForm):

    """
    Represents a form to the WODs.
    """
    class Meta:
        model = Wod
        exclude = ('user',)


class ExerciseForm(models.ModelForm):

    """
    Represents a form to the Exercises.
    """
    class Meta:
        model = Exercise
        fields = '__all__'

ExerciseFormSet = models.inlineformset_factory(
    Wod, Exercise, form=ExerciseForm, extra=1, fields=('wod', 'description',))
