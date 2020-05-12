from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Categories

# Register your models here.

class CategoriesAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Categories, CategoriesAdmin)

