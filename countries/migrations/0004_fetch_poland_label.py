# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import pywikibot


def fetch_poland_name(apps, schema_editor):
    Poland = apps.get_model("countries", "Poland")
    poland = Poland.objects.get()

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    poland_item = pywikibot.ItemPage(repo, poland.wikidata_id)
    poland.label = poland_item.get()['labels']['pl']
    poland.save()


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_poland_label'),
    ]

    operations = [
        migrations.RunPython(fetch_poland_name)
    ]
