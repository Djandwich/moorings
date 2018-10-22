# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-06 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0020_create_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='/home/corporateict.domain/briank/apps/work/ledger-parkstay/media/Parkstay/CampgroudImages')),
                ('campground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='parkstay.Campground')),
            ],
        ),
    ]
