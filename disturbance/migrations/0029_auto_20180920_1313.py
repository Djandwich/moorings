# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-20 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0028_auto_20180911_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='compliance',
            name='reminder_sent',
            field=models.BooleanField(default=False),
        ),
        # migrations.AlterField(
        #     model_name='proposaltype',
        #     name='name',
        #     field=models.CharField(choices=[('Disturbance', 'Disturbance'), ('Apiary', 'Apiary')], default='Disturbance', max_length=24, verbose_name='Application name (eg. Disturbance, Apiary)'),
        # ),
    ]