# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='文件名称')),
                ('file', models.FileField(upload_to='files', verbose_name='上传')),
                ('desc', models.TextField(verbose_name='文件描述')),
            ],
            options={
                'verbose_name_plural': '资料维护',
            },
        ),
    ]