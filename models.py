import random
import string
from django.db import models
from django.contrib.auth.models import User, UserManager

class Participant(User):
	confirmation_code = models.CharField(max_length=32)
	time = models.DateTimeField(auto_now=True)
	confirmed = models.BooleanField(default=False)
	key = models.CharField(max_length=32)

	def save(self, *args, **kwargs):
		'''
		On save generate key which will be sent in email
		'''
		self.key = ''.join(random.choice(string.letters) for i in xrange(32))
		super(Participant, self).save(*args, **kwargs)
		return self

	class Meta:
		verbose_name = 'Participant'
		verbose_name_plural = 'Participants'

	def __unicode__(self):
		return self.email

	