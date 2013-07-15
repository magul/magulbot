#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# check es_page's infobox if there is head of gov as a separate page
#


# system imports
import sqlite3 as lite

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
# Ficha de localidad de Espana
cur.execute(u'SELECT es_page_text , es_page from municipio where es_page_text like "%Ficha de localidad%"')
data = cur.fetchall()
print len(data)


cur.execute(u'SELECT es_page_text , es_page from municipio where es_page_text like "%Ficha de entidad% subn%"')
data = cur.fetchall()
print len(data)

con.close()
