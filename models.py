from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
import random
import string

class Participant(models.Model):
	first_name = models.CharField(max_length=60)	
	last_name = models.CharField(max_length=60)
	birthday = models.DateField(auto_now=False)
	email = models.EmailField(unique=True)
	contact = models.CharField(max_length=32)
	media = models.FileField(upload_to='participant-media/%Y/%B/%d')
	time = models.DateTimeField(auto_now=True, editable=False)	
	confirmed = models.BooleanField(default=False, editable=False)
	key = models.CharField(max_length=32, editable=False)

	def participant_media(self):
		return mark_safe('<a href="#" data-url="%s" class="view">View</a>') % self.media.url
	
	participant_media.allow_tags = True

	def age(self):
		b_data = self.birthday
		b_yr = b_data.year
		b_mo = b_data.month
		b_dy = b_data.day
		birthday = datetime(b_yr, b_mo, b_dy)
		age = int((datetime.now() - birthday).days / 365.2425)

		return age

	def save(self, *args, **kwargs):
		'''
		On save: generate key which will be sent in email
		'''
		self.key = ''.join(random.choice(string.letters) for i in xrange(32))
		super(Participant, self).save(*args, **kwargs)
		return self

	def __unicode__(self):
		return self.email_plural = 'Participants'

	def __unicode__(self):
		return self.email