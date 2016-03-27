# -*- coding: utf-8 -*-

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class AbstractWikiDataEntity(models.Model):

    class Meta:
        abstract = True

    wikidata_id_abs = models.CharField(max_length=15)
    label_abs = models.CharField(max_length=150)

    def __str__(self):
        return self.label_abs


class WikiDataEntity(models.Model):

    wikidata_id = models.CharField(max_length=15)
    label = models.CharField(max_length=150)
    reviewed_revision = models.CharField(max_length=15)
    pending_revision = models.CharField(max_length=15)

    def __str__(self):
        return self.label


class PendingReview(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    review_object = GenericForeignKey()
