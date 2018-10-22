# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-25 05:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0014_auto_20161122_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campgroundpricehistory',
            options={'managed': False, 'ordering': ['-date_start']},
        ),
        migrations.AddField(
            model_name='campsiteclass',
            name='features',
            field=models.ManyToManyField(to='parkstay.Feature'),
        ),
        migrations.AlterField(
            model_name='campsiterate',
            name='campsite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rates', to='parkstay.Campsite'),
        ),
    ]
