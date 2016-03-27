# -*- coding: utf-8 -*-

from django.db import models

from countries import models as countries_models
from generic import models as generic_models


class Wojewodztwo(generic_models.AbstractWikiDataEntity):

    country = models.ForeignKey(countries_models.Poland)
