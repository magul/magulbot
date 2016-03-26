# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import pywikibot


def fetch_powiats_entities(apps, schema_editor):
    Powiat = apps.get_model("pl_powiat", "Powiat")
    Wojewodztwo = apps.get_model("pl_wojewodztwo", "Wojewodztwo")

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()

    for wojewodztwo in Wojewodztwo.objects.all():
        woj_item = pywikibot.ItemPage(repo, wojewodztwo.wikidata_id)
        for claim in woj_item.get()['claims']['P150']:
            powiat_item = claim.getTarget()
            Powiat(
                wikidata_id=powiat_item.title(),
                wojewodztwo=wojewodztwo,
                label=powiat_item.get()['labels']['pl']).save()


class Migration(migrations.Migration):

    dependencies = [
        ('pl_powiat', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fetch_powiats_entities)
    ]
