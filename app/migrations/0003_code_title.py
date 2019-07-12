# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='title',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
