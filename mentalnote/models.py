from django.db import models

# Create your models here.

class Note(models.Model):
	content = models.TextField()
	postedOn = models.DateTimeField()
	
	def __unicode__(self):
		return self.content
