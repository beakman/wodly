from __future__ import unicode_literals

from django.db import models

from core.models import TimeStampedModel

from wodly.users.models import User

class Wod(TimeStampedModel):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User)

	def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wod:detail', kwargs={'id': self.id})

class Exercise():
	wod = models.ForeignKey(Wod)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)

	def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exercise:detail', kwargs={'id': self.id})