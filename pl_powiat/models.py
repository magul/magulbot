# -*- coding: utf-8 -*-

from django.db import models

from pl_wojewodztwo import models as wojewodztwo_models
from generic import models as generic_models


class Powiat(generic_models.AbstractWikiDataEntity):

    wojewodztwo = models.ForeignKey(wojewodztwo_models.Wojewodztwo)
    miasto_na_prawach_powiatu = models.BooleanField()
