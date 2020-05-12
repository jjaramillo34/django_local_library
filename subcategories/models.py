from __future__ import unicode_literals
from django_extensions.db.fields import AutoSlugField
from simple_history.models import HistoricalRecords
from categories.models import Categories
from django.db import models
from datetime import datetime
import arrow

# Create your models here.
def my_slugify_function(content):
    return content.replace('_', '-').lower()

class SubCategories(models.Model):
	"""docstring for Main"""
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	category_name = models.CharField(max_length=50, help_text='Category Name')
	subcategory_name = models.CharField(max_length=50, help_text='SubCategory Name')
	subcategory_description = models.TextField(default='-', help_text='SubCategory Description')
	subcategory_date = models.DateTimeField(default=datetime.now, help_text="SubCategory Date Created")
	slug = AutoSlugField(populate_from='subcategory_name', help_text="Slug")
	history_subcat = HistoricalRecords()
	
	def __str__ (self):
		return self.subcategory_name

	class Meta:
		ordering = ['subcategory_name']