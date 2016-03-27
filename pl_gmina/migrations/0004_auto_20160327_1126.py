# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pl_gmina', '0003_auto_20160327_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmina',
            old_name='label',
            new_name='label_abs',
        ),
        migrations.RenameField(
            model_name='gmina',
            old_name='pending_revision',
            new_name='wikidata_id_abs',
        ),
        migrations.RemoveField(
            model_name='gmina',
            name='reviewed_revision',
        ),
        migrations.RemoveField(
            model_name='gmina',
            name='wikidata_id',
        ),
    ]
