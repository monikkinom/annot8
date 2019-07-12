# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_annotations_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotations',
            name='color',
            field=models.CharField(max_length=100, choices=[(b'marked', b'Green'), (b'marked2', b'Red'), (b'marked3', b'Yellow')]),
        ),
    ]
