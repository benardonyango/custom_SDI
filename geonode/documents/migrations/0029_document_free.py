# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0028_document_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]
