# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 01:36
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('licence', '0001_initial'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('lodged', 'Lodged')], max_length=20, verbose_name='Application State')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(to='accounts.Document')),
                ('licence_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='licence.LicenceType')),
            ],
        ),
    ]