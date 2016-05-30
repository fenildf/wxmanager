# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgType', models.IntegerField(default=0)),
                ('msgId', models.CharField(default='', max_length=256)),
                ('CreateTime', models.IntegerField(default=0)),
                ('msg', models.CharField(default='', max_length=4096)),
                ('content', models.CharField(default='', max_length=2048)),
                ('group_name', models.CharField(default='', max_length=256)),
                ('user', models.CharField(default='', max_length=256)),
                ('to_user', models.CharField(default='', max_length=256)),
            ],
        ),
    ]