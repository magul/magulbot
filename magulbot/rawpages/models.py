# -*- coding: utf-8 -*-

from django.db import models


class RawPage(models.Model):
    wiki_family = models.CharField(max_length=20)
    wiki_lang = models.CharField(max_length=4)
    name = models.CharField(max_length=1000)
    new_id = models.CharField(max_length=15)
    rev_id = models.CharField(max_length=15)
    last_sync = models.DateTimeField()
