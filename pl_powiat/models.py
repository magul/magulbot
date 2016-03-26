# -*- coding: utf-8 -*-

from django.db import models

from pl_wojewodztwo import models as wojewodztwo_models
from generic import models as generic_models


class Powiat(generic_models.WikiDataEntity):

    wojewodztwo = models.ForeignKey(wojewodztwo_models.Wojewodztwo)
