# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151025_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotations',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]
