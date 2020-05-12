# Generated by Django 3.0.4 on 2020-05-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20200509_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='category_date_human',
        ),
        migrations.RemoveField(
            model_name='historicalcategories',
            name='category_date_human',
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_date',
            field=models.DateTimeField(default='May 09 2020 20:12:46', help_text='Category Date Created'),
        ),
        migrations.AlterField(
            model_name='historicalcategories',
            name='category_date',
            field=models.DateTimeField(default='May 09 2020 20:12:46', help_text='Category Date Created'),
        ),
    ]
