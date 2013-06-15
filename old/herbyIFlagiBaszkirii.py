#!/usr/bin/python
# -*- coding: utf-8 -*-

# import bibliotek
import sys, string
from urllib2 import urlopen
from wikipedia import *
from catlib import * 

# ustawienia podstawowe
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)

# sciaganie szablonu i ustalanie stron kazdego regionu
page = Page(plwiki, u'Szablon:Baszkiria')
pagetext = page.get()
pagetext = pagetext[pagetext.find(u'<div>'):pagetext.find(u'</div>')]
districtPlPages = []
while pagetext.find(u'[[') != -1:
	districtPlPages.append(pagetext[pagetext.find('[[') + 2:pagetext.find(u'|')])
	pagetext = pagetext[pagetext.find(u'|') + 1:]

# glowna petla programu
for district in districtPlPages:
# sciaganie strony polskiej...
	plpage = Page(plwiki, district)
	plpagetext = plpage.get()
# ...ustalanie miejsc na herb i flage w infoboksie...
	if plpagetext.find(u'{{Jednostka administracyjna infobox') == -1:
		print 'NIE MA INFOBOKSU: ' + district
	else:
		begining = plpagetext[:plpagetext.find(u' |herb')]
		ending = plpagetext[plpagetext.find(u' |mapa'):]
# ...znajdowanie rosyjskiej strony...
		interwikis = plpage.interwiki()
		for interwiki in interwikis:
			if interwiki.site() == getSite('ru', 'wikipedia'):
				rupage = interwiki
		rupagetext = rupage.get()		
# ...ustalanie nazw plikow herbu i flagi...
		coa = rupagetext[rupagetext.find(u'|Герб') + 1:]
		coa = coa[coa.find(u'=') + 1:coa.find(u'|')]
		while coa[0] == ' ' or coa[0] == '\n':
			coa = coa[1:]
		while coa[-1] == ' ' or coa[-1] == '\n':
			coa = coa[:-1]
		flag = rupagetext[rupagetext.find(u'|Флаг') + 1:]
		flag = flag[flag.find(u'=') + 1:flag.find(u'|')]
		while flag[0] == ' ' or flag[0] == '\n':
			flag = flag[1:]
		while flag[-1] == ' ' or flag[-1] == '\n':
			flag = flag[:-1]
		if flag.find(u'{{') != -1:
			flag = flag[:flag.find(u'{')]
# ...dodawania szablonu svg na commons dla coa...
		commons = getSite('commons', 'commons')
		coaPage = Page(commons, u'File:' + coa)		
		coapagetext = coaPage.get()
		if coapagetext.find(u'{{SVG') == -1:
			coapagetext = u'{{SVG|coat of arms}}' + '\n' + coapagetext
			coaPage.put(coapagetext, u'should be converted to SVG')
# ...dodawanie szablonu svg na commons dla flagi...
		flagPage = Page(commons, u'File:' + flag)		
		flagpagetext = flagPage.get()
		if flagpagetext.find(u'{{SVG') == -1:
			flagpagetext = u'{{SVG|flag}}' + '\n' + flagpagetext
			flagPage.put(flagpagetext, u'should be converted to SVG')
# ...dodawania herbu i flagi do polskiej wiki
		plpagetext = begining + u' |herb                              = ' + coa + '\n'
		plpagetext = plpagetext + u' |flaga                             = ' + flag + '\n' + ending
		plpage.put(plpagetext, u'Dodano herb i flage na podstawie ru.wiki')
