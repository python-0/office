# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170716_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='size',
        ),
    ]
