from __future__ import unicode_literals
from django_extensions.db.fields import AutoSlugField
from simple_history.models import HistoricalRecords
from import_export import resources
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class News(models.Model):
	"""docstring for Main"""
	article_name = models.CharField(max_length=50, help_text='Article Name')
	article_short = models.TextField()
	article_body = models.TextField()
	article_date = models.CharField(max_length=50, help_text='Article Date')
	article_picture_name = models.TextField()
	article_picture_url = models.TextField(default="-")
	article_author = models.CharField(max_length=50, help_text="Article Author")
	
	article_views = models.IntegerField(default=0)
	article_status = models.CharField(max_length=30,default='-')
	article_percentage = models.IntegerField(default=0)
	article_live = models.BooleanField(default='False', help_text="Article Live Switch")
	article_date_created = models.DateTimeField(default=timezone.now, help_text="Article Date Created")
	
	article_category = models.CharField(max_length=50, default='-')
	article_subcategory = models.CharField(max_length=50, default='-')

	article_image_size = models.CharField(max_length=20, default='-')

	slug = AutoSlugField(populate_from='article_name', help_text="Slug")

	history_news = HistoricalRecords()

	def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('news', args=[str(self.slug)])

	def __str__ (self):
		return self.article_name