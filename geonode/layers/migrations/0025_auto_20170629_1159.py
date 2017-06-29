# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('layers', '24_to_26'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='project',
            field=models.ForeignKey(default=1, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='display_order',
            field=models.IntegerField(default=1, help_text='specifies the order in which attribute should be displayed             in identify results', verbose_name='display order'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='visible',
            field=models.BooleanField(default=True, help_text='specifies if the attribute should be displayed in identify             results', verbose_name='visible?'),
        ),
    ]
