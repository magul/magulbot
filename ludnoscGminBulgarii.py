#!/usr/bin/python
# -*- coding: utf-8 -*-

# import bibliotek
import sys, string
from urllib2 import urlopen
from wikipedia import *
from transliteracja import BG

# ustawienia podstawowe
mylang = 'pl'
family = 'wikipedia'
plwiki = getSite(mylang, family)

# sciaganie danych zrodlowych
areaSource = unicode(urlopen('http://www.nsi.bg/otrasal.php?otr=19&a1=376&a2=377&a3=378').read(), 'windows-1251', errors =  'ignore')
print areaSource

# ustalanie nazw gmin
sourceMunicipalitiesList = {}

