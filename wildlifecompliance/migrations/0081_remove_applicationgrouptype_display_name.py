# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-18 02:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0080_auto_20180912_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationgrouptype',
            name='display_name',
        ),
    ]