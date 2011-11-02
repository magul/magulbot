#!/usr/bin/python
# -*- coding: utf-8 -*-

# import bibliotek
import sys, string
from urllib2 import urlopen
from wikipedia import *

# ustawienia podstawowe
mylang = 'pl'
family = 'wikipedia'
plwiki = getSite(mylang, family)

# sciaganie danych zrodlowych
areaSource = urlopen("http://www.stat.si/letopis/2010/31_10/31-01-10.htm").read().encode('utf-8')
populationSource = urlopen("http://www.stat.si/letopis/2010/31_10/31-02-10.htm").read()

# ustalanie nazw gmin
municipalitiesList = []
#while areaSource.find(u'<td height=17 class=xl24') != -1:
#	areaSource = areaSource[areaSource.find(u'<td height=17 class=xl24'):]
#	areaSource = areaSource[areaSource.find(u'>'):]
#	print areaSource[:areaSource.find(u'<')]

