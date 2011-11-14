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
source = unicode(urlopen('http://www.nsi.bg/otrasal.php?otr=19&a1=376&a2=377&a3=378').read(), 'windows-1251', errors =  'ignore')

# ustalanie nazw gmin
populationMunicipalitiesList = {}
source.replace('\n', '')
source = source[source.find(u'Общо за страната'):]
source = source[:source.find(u'</tbody>')]
while source.find(u'<td class="left') != -1:
	source = source[source.find(u'<td class="left'):]
	name = source[source.find(u'>') + 1:source.find(u'</td>')]
	source = source[source.find(u'</td>'):]
	source = source[source.find(u'<td'):]
	source = source[source.find(u'>') + 1:]
	population = source[:source.find(u'<')]
	population = population.replace(u'&nbsp;', '')
	populationMunicipalitiesList[name] = population

# ustalenie szablonow wiki dla okregow
districtsTemplatesList = []
page = Page(plwiki, u'Szablon:Bułgaria')
pagetext = page.get()
pagetext = pagetext[pagetext.find(u'spis1'):pagetext.find(u'kategoria')]
while pagetext.find(u'[[') != -1:
	districtsTemplatesList.append(u'Szablon:O' + pagetext[pagetext.find(u'[[') + 3:pagetext.find(u'|')])
	pagetext = pagetext[pagetext.find(u'|') + 1:]
	
# ustalenie stron wiki dla gmin
municipalitiesPagesList = []
for foo in districtsTemplatesList:
	page = Page(plwiki, foo)
	pagetext = page.get()
	pointer = pagetext.find(u'Gmina ')
	while pointer != -1:
		municipalitiesPagesList.append(pagetext[pagetext.rfind(u'[[', 0, pointer) + 2:pagetext.find(u'|', pointer)])
		pagetext = pagetext[pagetext.find(u'Gmina ') + 1:]
		pointer = pagetext.find(u'Gmina ')

print len(municipalitiesPagesList)

for foo in municipalitiesPagesList:
	page = Page(plwiki, foo)
	pagetext = page.get()
	pagetext = pagetext[pagetext.find(u'|nazwa oryginalna') + 1:]
	pagetext = pagetext[:pagetext.find(u'|')]
	i = 0
	for bar in populationMunicipalitiesList:
		if bar in pagetext:
			i = i + 1
	if i != 1:
		print foo + ' ' + str(i)
