# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pl_wojewodztwo', '0004_fetch_wojewodztwo_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powiat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wikidata_id', models.CharField(max_length=15)),
                ('label', models.CharField(max_length=150)),
                ('wojewodztwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pl_wojewodztwo.Wojewodztwo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]