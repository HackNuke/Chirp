# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20180128_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='file',
            new_name='profile_photo',
        ),
    ]
