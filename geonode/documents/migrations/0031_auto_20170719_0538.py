# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0030_document_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='project',
            field=models.ForeignKey(default=1, to='projects.Project', help_text='Associated project'),
        ),
    ]
