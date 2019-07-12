# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151025_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotations',
            name='color',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
