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
	if len(population) > 4:
		i = 0
		while i * 4 + 3 < len(population):
			population = population[:i * -4 - 3] + ' ' + population[i * -4 - 3:]
			i = i + 1
	if name in populationMunicipalitiesList:
		print name + u' ' + populationMunicipalitiesList[name]
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

# odwzorowanie stron do nazw bulgarskich
municipalitiesPagesDict = {}
for foo in municipalitiesPagesList:
	page = Page(plwiki, foo)
	pagetext = page.get()
	pagetext = pagetext[pagetext.find(u'|nazwa oryginalna') + 1:]
	pagetext = pagetext[:pagetext.find(u'|')]
	i = 0
	for bar in populationMunicipalitiesList:
		if bar in pagetext:
			i = i + 1
	if i == 1:
		for bar in populationMunicipalitiesList:
			if bar in pagetext:
				municipalitiesPagesDict[bar] = foo
	else:
		print foo

# edycja stron
for foo in municipalitiesPagesDict:
	page = Page(plwiki, municipalitiesPagesDict[foo])
	pagetext = page.get()
	beginning = pagetext[:pagetext.find(u'|populacja                         = ')]
	pagetext = pagetext[pagetext.find(u'|populacja                         = '):]
	ending = pagetext[pagetext.find(u'|gęstość'):]
	middle = u'|populacja                         = ' + populationMunicipalitiesList[foo] + u'<ref>{{cytuj stronę | url = http://www.nsi.bg/otrasal.php?otr=19&a1=376&a2=377&a3=378 | tytuł = 6.1.1. Население по области, общини, местоживеене и пол – Данни | autor = Национален статистически институт | data dostępu = 2011-11-15 | data = 2011-04-27 | język = bg}}</ref>'
	middle = middle + '\n' + u' |rok                               = 2010' + '\n '
	pagetext = beginning + middle + ending
	pagetext = pagetext[:pagetext.find(u'{{Obw')] + u'{{Przypisy}}' + '\n' + pagetext[pagetext.find(u'{{Obw'):]
	if pagetext.find(u'{{Obw') == -1:
		print foo
	else:
		page.put(pagetext, u'Uaktualnienie populacji na podstawie danych z Bulgarskiego Urzedu Statystycznego') 
