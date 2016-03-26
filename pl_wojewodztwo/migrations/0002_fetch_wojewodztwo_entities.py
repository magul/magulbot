# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import pywikibot


def fetch_wojewodztwo_entities(apps, schema_editor):
    Wojewodztwo = apps.get_model("pl_wojewodztwo", "Wojewodztwo")
    Poland = apps.get_model("countries", "Poland")
    poland = Poland.objects.get()

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    poland_item = pywikibot.ItemPage(repo, poland.wikidata_id)
    for claim in poland_item.get()['claims']['P150']:
        Wojewodztwo(
            wikidata_id=claim.getTarget().title(),
            country=poland).save()


class Migration(migrations.Migration):

    dependencies = [
        ('pl_wojewodztwo', '0001_initial'),
        ('countries', '0002_insert_poland_entity'),
    ]

    operations = [
        migrations.RunPython(fetch_wojewodztwo_entities)
    ]
