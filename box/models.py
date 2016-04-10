from __future__ import unicode_literals

from django.db import models

from wodly.users.models import User

class Box():
	name = models.CharField(_("BOX name"), blank=True, max_length=255)
	city = models.CharField(_("City"), blank=True, max_length=255)
	user = models.ForeignKey(User)

	def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('box:detail', kwargs={'id': self.id})