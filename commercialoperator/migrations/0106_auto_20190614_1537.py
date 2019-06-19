# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-14 07:37
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0105_auto_20190613_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='admission_number',
            field=models.CharField(blank=True, default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]
