# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_code_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('code', models.ForeignKey(to='app.Code')),
            ],
        ),
    ]
