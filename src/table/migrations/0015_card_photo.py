# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-30 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0014_remove_card_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='photo',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]