# Generated by Django 3.0.4 on 2020-05-09 23:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Category Name', max_length=50)),
                ('category_description', models.TextField(default='-', help_text='Category Description')),
                ('category_date', models.DateTimeField(default=datetime.datetime.now, help_text='Category Date Created')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Slug', populate_from='category_name')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCategories',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Category Name', max_length=50)),
                ('category_description', models.TextField(default='-', help_text='Category Description')),
                ('category_date', models.DateTimeField(default=datetime.datetime.now, help_text='Category Date Created')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Slug', populate_from='category_name')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical categories',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
