# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_code_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='language',
            field=models.CharField(max_length=100, choices=[(b'cpp', b'C++'), (b'python', b'Python'), (b'php', b'PHP'), (b'c', b'C'), (b'java', b'Java'), (b'javascript', b'Javascript'), (b'csharp', b'C#'), (b'python', b'Python'), (b'ruby', b'Ruby'), (b'swift', b'Swift'), (b'objectivec', b'Objective-C'), (b'css', b'CSS'), (b'php', b'Unknown/Text')]),
        ),
    ]
