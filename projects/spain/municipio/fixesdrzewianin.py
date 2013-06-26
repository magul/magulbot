#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# apply fixes pioted out by Drzewianin
#

# system imports
from wikipedia import *
import catlib
import sqlite3 as lite

# bot imports
from fixies import *

# configure plwiki
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)

# get data from sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT spanish_name, current_plpage FROM municipio')
data = cur.fetchall()
con.close()

for row in data:
	spanish_name = row[0]
	pl_page = row[0]
	pl_page = Page(plwiki, pl_page)
	if pl_page.exists() and not pl_page.isRedirectPage():
		print pl_page.title()
		text = pl_page.get()
		text_old = text
		text = text.replace(u' |dopełniacz nazwy             = \n |państwo', u' |dopełniacz nazwy             = ' + spanish_name + u'\n |państwo')
		text = text.replace(u'  - gmina w', u' – gmina w')
		if text_old != text:
			pl_page.put(text, u'Fixes thx to Drzewianin (Dyskusja_wikipedysty:Magul#Gminy_hiszpa.C5.84skie)')
