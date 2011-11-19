#!/usr/bin/python
# -*- coding: utf-8 -*-

# import bibliotek
import sys, string
from urllib2 import urlopen
from wikipedia import *
from catlib import * 

# ustawienia podstawowe
commonslang = 'commons'
commonsfamily = 'commons'
commonswiki = getSite(commonslang, commonsfamily)
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)
enlang = 'en'
enfamily = 'wikipedia'
enwiki = getSite(enlang, enfamily)

# sciaganie map w kategorii
category = Category(commonswiki, u'Locator_maps_of_municipalities_of_Central_North_Bulgaria')
imageInCategory = category.articlesList()

# dla wszyskich obrazow w kategorii...
for image in imageInCategory:
# zliczanie angielskich stron korzystajacych z mapy
	for page in  image.globalUsage():
		if page.site() == enwiki:
			enPage = page
# ustalanie polskiej strony gminy
	for interwiki in enPage.interwiki():
		if interwiki.site() == plwiki:
			plPage = interwiki
# ustalanie nazwy grafiki, ktora znajduje sie na polskiej wersji
	pagetext = plPage.fullVersionHistory()[-1][3]
	pagetext = pagetext[pagetext.find(u'|mapa'):]
	pagetext = pagetext[pagetext.find(u'=') + 1:]
	pagetext = pagetext[:pagetext.find(u'|')]
	while pagetext[0] == ' ' or pagetext[0] == '\n':
		pagetext = pagetext[1:]
	while pagetext[-1] == ' ' or pagetext[-1] == '\n':
		pagetext = pagetext[:-2]
# sciaganie strony commons obecnej grafiki i spradzanie, czy tworca to Targovishtenec bg
	oldCommonsPage = ImagePage(commonswiki, 'File:' + pagetext)
	if oldCommonsPage.getLatestUploader()[0] == u'Targovishtenec bg':
		pagetext = oldCommonsPage.get()
# jezeli tak, to sprawdzamy, czy nie ma jeszcze szablonu i ewentualnie aktualizujemy
		if pagetext.find(u'{{superseded') == -1:
			pagetext = u'{{superseded|' + image.title(withNamespace = False) + u'}}' + '\n' + pagetext
			oldCommonsPage.put(pagetext, u'Better quality map')
# zmiana mapy na polskiej wiki
	pagetext = plPage.get()
	if pagetext.find(image.title(withNamespace = False)) == -1:
		beginning = pagetext[:pagetext.find(u'|mapa')]
		middle = pagetext[pagetext.find(u'|mapa') + 1:]
		ending = middle[middle.find('|'):]
		middle = '|mapa                              = ' + image.title(withNamespace = False) + '\n '
		pagetext = beginning + middle + ending
		plPage.put(pagetext, u'Mapa lepszej jakości')
