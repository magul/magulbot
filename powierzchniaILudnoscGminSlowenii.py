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
areaSource = unicode(urlopen("http://www.stat.si/letopis/2010/31_10/31-01-10.htm").read(), 'windows-1250', errors =  'ignore')
populationSource = unicode(urlopen("http://www.stat.si/letopis/2010/31_10/31-02-10.htm").read(), 'windows-1250', errors = 'ignore')
source = areaSource

# ustalanie nazw gmin
sourceMunicipalitiesList = {}
while source.find(u'<td height=17 class=xl24') != -1:
	source = source[source.find(u'<td height=17 class=xl24'):]
	source = source[source.find(u'>') + 1:]
	sourceMunicipality = source[:source.find(u'<')]	
	municipality = sourceMunicipality.replace('\n', '')
	municipality = municipality.replace('\r', '')
	while municipality.find('  ') != -1:
		municipality = municipality.replace('  ', ' ')
	if municipality.find('/') != -1:
		municipality = municipality[:municipality.find('/')]
	sourceMunicipalitiesList[municipality] = sourceMunicipality

# ustalanie powierzchni gmin
areasList = {}
for municipality in sourceMunicipalitiesList:
	source = areaSource
	source = source[source.find(sourceMunicipalitiesList[municipality]):]
	source = source[source.find('xl55'):]
	source = source[source.find('>') + 1:source.find('<')]
	areasList[municipality] = source

# ustalenie populacji gmin
populationsList = {}
for municipality in sourceMunicipalitiesList:
	pointer = municipality
	while populationSource.find(pointer) == -1:
		pointer = pointer[:-1]
	source = populationSource[populationSource.find(pointer):]
	source = source[source.find('xl68'):]
	source = source[source.find('>') + 1:source.find('<')]
	if len(source) > 4:
		source = source[:-3] + ' ' + source[-3:]
	populationsList[municipality] = source

# ustalanie stron wiki na podstawie szablonu
wikiPagesList = {}
page = Page(plwiki, u'Szablon:Słowenia')
pagetext = page.get()
for municipality in sourceMunicipalitiesList:
	pointer = municipality
	while pagetext.find(pointer) == -1:
		pointer = pointer[:-1]
	pointer = pagetext.find(pointer)
	wikiPage = pagetext[pagetext.rfind(u'[', 0, pointer) + 1:pagetext.find(u']', pointer)]
	if wikiPage.find(u'|') != -1:
		wikiPage = wikiPage[:wikiPage.find(u'|')]
	wikiPagesList[municipality] = wikiPage

# pozbywanie sie przekierowan stron
for municipality in wikiPagesList:
	page = Page(plwiki, wikiPagesList[municipality])
	while page.isRedirectPage():
		page = Page(plwiki, page.getRedirectTarget().title())
		wikiPagesList[municipality] = page.title()

