# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


def insert_poland(apps, schema_editor):
    Poland = apps.get_model("countries", "Poland")
    Poland(wikidata_id='Q36').save()


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_poland)
    ]
