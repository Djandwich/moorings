# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 08:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wl_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('current', 'Current'), ('future', 'Future'), ('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='future', max_length=20)),
                ('lodgement_number', models.CharField(blank=True, default='', max_length=9)),
                ('lodgement_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField()),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wl_main.WildlifeLicence')),
                ('proxy_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ret', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wl_returns.Return')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_descriptor', django.contrib.postgres.fields.jsonb.JSONField()),
                ('month_frequency', models.IntegerField(choices=[(-1, 'One off'), (1, 'Monthly'), (3, 'Quarterly'), (6, 'Twice-Yearly'), (12, 'Yearly')], default=-1)),
                ('licence_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wl_main.WildlifeLicenceType')),
            ],
        ),
        migrations.AddField(
            model_name='returnrow',
            name='return_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wl_returns.ReturnTable'),
        ),
        migrations.AddField(
            model_name='return',
            name='return_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wl_returns.ReturnType'),
        ),
    ]
