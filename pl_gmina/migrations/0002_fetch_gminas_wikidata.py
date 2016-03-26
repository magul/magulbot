# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import pywikibot


def fetch_gminas_entities(apps, schema_editor):
    Gmina = apps.get_model("pl_gmina", "Gmina")
    Powiat = apps.get_model("pl_powiat", "Powiat")

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()

    for powiat in Powiat.objects.filter(miasto_na_prawach_powiatu=False):
        powiat_item = pywikibot.ItemPage(repo, powiat.wikidata_id)
        for claim in powiat_item.get()['claims']['P150']:
            gmina_item = claim.getTarget()
            Gmina(
                wikidata_id=gmina_item.title(),
                powiat=powiat,
                label=gmina_item.get()['labels']['pl']).save()


class Migration(migrations.Migration):

    dependencies = [
        ('pl_gmina', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fetch_gminas_entities)
    ]
