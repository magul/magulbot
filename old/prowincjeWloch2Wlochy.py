#!/usr/bin/python
# -*- coding: utf-8 -*-

# import bibliotek
import sys, string
from wikipedia import *

# ustawienia podstawowe
mylang = 'pl'
family = 'wikipedia'
plwiki = getSite(mylang, family)

# sciaganie listy stron linkujacych do Szablon:Prowincje Włoch
page = Page(plwiki, u'Szablon:Prowincje_Włoch')
prowincjeWlochReferences = list(page.getReferences())

for reference in prowincjeWlochReferences:
	if reference.title().find(':') == -1:
		pagetext = reference.get()
		pagetext = pagetext.replace(u'Prowincje Włoch}}', u'Włochy}}')
		reference.put(pagetext, u'zmieniono navibox z "Prowincje Włoch" na "Włochy"')
