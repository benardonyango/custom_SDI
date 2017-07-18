# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0029_document_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
