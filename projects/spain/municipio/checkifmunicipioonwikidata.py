#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# check if it's really municipio of spain on wikidata
#


# system imports
import sqlite3 as lite
from wikipedia import *

# sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT es_page, wikidata, es_page_text from municipio')
data = cur.fetchall()
con.close()

plwiki = getSite('pl', 'wikipedia')
repo = plwiki.data_repository()
edit_ct = 0
for item in data:
	wd = item[1]
	es = item[0]
	text = item[2]
# wikidata
	wd_item = DataPage(repo, wd)
	data = wd_item.get()
	instanceof = []
	for claim in data['claims']:
		if claim['m'][1] == 31 or claim['m'][1] == 132:
			instanceof.append(claim['m'][3]['numeric-id'])

	if not 2074737 in instanceof and not 5055981 in instanceof:
		if text.find(u'[[Categoría:Municipios') != -1:
			wd_item.editclaim(31, 2074737, refs={(143, 8449)})
			edit_ct += 1
	if edit_ct == 10000:
		break
