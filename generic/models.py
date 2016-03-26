# -*- coding: utf-8 -*-

from django.db import models


class WikiDataEntity(models.Model):

    class Meta:
        abstract = True

    wikidata_id = models.CharField(max_length=15)
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label
