#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain wikidata pages of municipios of spain
#

# system imports
from wikipedia import *
import sqlite3 as lite

# configure wiki
eslang = 'es'
family = 'wikipedia'
eswiki = getSite(eslang, family)

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT es_page FROM municipio where wikidata is null')
data = cur.fetchall()

for item in data:
	es_page = item[0]
	print es_page
	es_page = Page(eswiki, es_page)
	data_page = DataPage(es_page)
	data_page.get()
	data_page =  data_page.title()
	es_page = es_page.title()

	cur.execute(u'UPDATE municipio SET wikidata = "' + data_page + u'" where es_page = "' + es_page + u'"')

# close sqlite connection
con.close()
