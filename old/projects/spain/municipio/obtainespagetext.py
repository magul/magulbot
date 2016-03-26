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
cur.execute(u'SELECT es_page FROM municipio where es_page_text is null')
data = cur.fetchall()

for item in data:
	es_page = item[0]
	print es_page
	es_page_ = Page(eswiki, es_page)
	text = es_page_.get()
	text = text.replace("'", "''")


	cur.execute(u"UPDATE municipio SET es_page_text = '" + text + u"' where es_page = '" + es_page.replace("'", "''") + u"'")

# close sqlite connection
con.close()
