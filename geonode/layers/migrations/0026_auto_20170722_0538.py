# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0025_auto_20170629_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='free',
            field=models.BooleanField(default=True, help_text='Keep checked for a free layer'),
        ),
        migrations.AddField(
            model_name='layer',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Declare price of layer'),
        ),
    ]
