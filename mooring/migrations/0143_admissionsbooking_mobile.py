# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-28 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0142_bookingannualadmission_rego_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionsbooking',
            name='mobile',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
