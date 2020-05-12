from __future__ import unicode_literals
from django_extensions.db.fields import AutoSlugField
from simple_history.models import HistoricalRecords
from import_export import resources
from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
def my_slugify_function(content):
    return content.replace('_', '-').lower()

class Categories(models.Model):
	"""docstring for Main"""
	category_name = models.CharField(max_length=50, help_text='Category Name')
	category_description = models.TextField(default='-', help_text='Category Description')
	#category_date = models.DateField(default=datetime.now, help_text="Category Date Created")
	category_date = models.DateTimeField(default=timezone.now, help_text="Category Date Created")
	slug = AutoSlugField(populate_from='category_name', help_text="Slug")
	history_cat= HistoricalRecords()
	
	def __str__ (self):
		return self.category_name

class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories 
        fields = ('id', 'category_name', 'category_description', 'slug',)
