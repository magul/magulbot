# -*- coding: utf-8 -*-

from django.db import models

from pl_powiat import models as powiat_models
from generic import models as generic_models


class Gmina(generic_models.AbstractWikiDataEntity):

    powiat = models.ForeignKey(powiat_models.Powiat)
