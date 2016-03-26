# -*- coding: utf-8 -*-

from django.db import models


class WikiDataEntity(models.Model):

    class Meta:
        abstract = True

    wikidata_id = models.CharField(max_length=15)
