# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-23 04:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0022_auto_20170323_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roster',
            options={'ordering': ('team', 'player__last_name')},
        ),
    ]
