# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import pywikibot


def fetch_wojewodztwo_names(apps, schema_editor):
    Wojewodztwo = apps.get_model("pl_wojewodztwo", "Wojewodztwo")

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()

    for wojewodztwo in Wojewodztwo.objects.all():
        wojewodztwo_item = pywikibot.ItemPage(repo, wojewodztwo.wikidata_id)
        wojewodztwo.label = wojewodztwo_item.get()['labels']['pl']
        wojewodztwo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pl_wojewodztwo', '0003_wojewodztwo_label'),
    ]

    operations = [
        migrations.RunPython(fetch_wojewodztwo_names)
    ]
