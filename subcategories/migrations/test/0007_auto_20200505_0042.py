# Generated by Django 3.0.5 on 2020-05-05 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategories', '0006_auto_20200505_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategories',
            name='subcategory_date',
            field=models.CharField(default='05/04/2020 | 20:42:04 PM', help_text='SubCategory Date Created', max_length=50),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='subcategory_date1',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='SubCategory Date Created'),
        ),
    ]
