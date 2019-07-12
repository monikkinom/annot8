# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151025_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 13, 12, 10, 645954), auto_now_add=True),
            preserve_default=False,
        ),
    ]
