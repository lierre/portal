# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='twitter',
        ),
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
