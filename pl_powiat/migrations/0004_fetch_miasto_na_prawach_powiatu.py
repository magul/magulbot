# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import pywikibot


def fetch_miasto_na_prawach_powiatu(apps, schema_editor):
    Powiat = apps.get_model("pl_powiat", "Powiat")

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()

    for powiat in Powiat.objects.all():
        powiat_item = pywikibot.ItemPage(repo, powiat.wikidata_id)
        instances = set(
            c.getTarget().title() for c in powiat_item.get()['claims']['P31'])
        if 'Q925381' in instances:
            powiat.miato_na_prawach_powiatu = True
            powiat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pl_powiat', '0003_powiat_miato_na_prawach_powiatu'),
    ]

    operations = [
        migrations.RunPython(fetch_miasto_na_prawach_powiatu)
    ]
