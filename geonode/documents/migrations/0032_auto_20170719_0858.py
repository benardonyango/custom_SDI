# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0031_auto_20170719_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='free',
            field=models.BooleanField(default=True, help_text='Uncheck for a commercialised document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Declare price of document'),
        ),
    ]
