# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('sname', models.CharField(help_text='Short name for project, example KCEP or CCRP', max_length=30, null=True, blank=True)),
                ('organization', models.CharField(max_length=150)),
                ('start_date', models.DateField(default=django.utils.timezone.now, help_text='Please define the date that the project was initiated')),
                ('end_date', models.DateField(help_text='Leave blank if project is still continuing', null=True, blank=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='ON', max_length=2, choices=[('ON', 'Ongoing'), ('CP', 'Completed')])),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
