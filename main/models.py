from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Main(models.Model):
	"""docstring for Main"""
	name = models.CharField(max_length=30)
	about = models.TextField()

	fb = models.CharField(default="/", max_length=50)	
	tw = models.CharField(default="/", max_length=50)
	lk = models.CharField(default="/", max_length=50)

	tel = models.CharField(default="/", max_length=30)
	link = models.CharField(default="/",max_length=50)

	set_name = models.CharField(default="/", max_length=30)

	def __str__ (self):
		return self.set_name + " | " + str(self.pk)