from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel

from wodly.users.models import User


class Wod(TimeStampedModel):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wods')
    initial_note = models.TextField(blank=True)
    foot_note = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wods:detail', (), {
            'username': self.user.username,
            'pk': self.id,
        })



class Exercise(TimeStampedModel):

    """ Exercises will be written inline: 8 Deadlifts (155/105 lbs) """

    wod = models.ForeignKey(Wod)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('exercise:detail', kwargs={'id': self.id})
