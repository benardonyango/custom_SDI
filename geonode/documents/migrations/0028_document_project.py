# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('documents', '27_drop_resource_columns_from_document_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(default=1, to='projects.Project'),
        ),
    ]
