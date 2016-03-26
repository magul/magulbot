#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# puts coordinates on wikidata
#


# system imports
import sqlite3 as lite
from wikipedia import *

# sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT wikidata, lon, lat from municipio')
data = cur.fetchall()
con.close()

plwiki = getSite('pl', 'wikipedia')
repo = plwiki.data_repository()
for item in data[2:]:
	wd = item[0]
	lon = item[1]
	lat = item[2]
# wikidata
	wd_item = DataPage(repo, wd)
	data = wd_item.get()
	corr_ct = 0
	for claim in data['claims']:
		if claim['m'][1] == 625:
			corr_ct += 1
	if corr_ct == 0:
		wd_item.createclaim(625, '{"latitude":'+str(lat)+', "longitude":'+str(lon)+', "globe":"http://www.wikidata.org/entity/Q2"}', refs={(143, 936)}, raw_value=True)
