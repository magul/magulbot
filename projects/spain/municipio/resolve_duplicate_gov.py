#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# resolve problem of duplication of head of gov of municipalities
# pywikibot-core
#

import pwb
from pywikibot import *
import sqlite3 as lite


s = Site('wikidata', 'wikidata')
r = s.data_repository()
p = Page(s, u'Wikidata:Requests for permissions/Bot/MagulBot 4').get()

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

links = []
p = p[p.find(u"Q11916413"):]
while p.find(u'[[') != -1:
	p = p[p.find(u'[[')+2:]
	links.append(p[:p.find(u']]')])
links = links[:-2]

i = 0
while i != len(links):
	origin = ItemPage(r, links[i+1])
	duplicate = ItemPage(r, links[i])
	origin.get()
	duplicate.get()

	cur.execute("SELECT wikidata from municipio where gov='"+duplicate.labels['en'].replace("'", "''")+"'")
	data = cur.fetchone()
	mun_wd = ItemPage(r, data[0])
#	print duplicate.title(), '==>', mun_wd
#	c = Claim(r, 'p6', origin.title())
#	c.setTarget(origin)
#	mun_wd.addClaim(c)
	print duplicate.title(), '|'
	i += 2
