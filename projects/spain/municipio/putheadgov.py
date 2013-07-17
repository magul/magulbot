#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# create item for head of goverment of municipio and property for item of municipio
#

# system imports
import sqlite3 as lite
from wikipedia import *

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

cur.execute(u'SELECT wikidata, gov_wd, gov, spanish_name from municipio')
data = cur.fetchall()
for item in data[1035:]:
	mun_wd = int(item[0][1:])
	if item[1] != None:
		gov_wd = int(item[1][1:])
	else:
		gov_wd = None
	gov = item[2]
	sp_name = item[3]
	
	mun_page = DataPage(mun_wd)
	mun_item = mun_page.get()

	gov_ct = 0
	for claim in mun_item['claims']:
		if claim['m'][1] == 6:
			gov_ct += 1
	if gov_ct == 0 and gov!=None:
		print mun_wd
		gov_page = DataPage('es', gov)
		while gov_wd == None:
			try:
				gov_wd = int(gov_page.createitem(u'Creating item for alcalde of '+sp_name+', municipality of Spain', value={'labels': { 'es': {'language': 'es', 'value' : gov}, 'en': {'language': 'en', 'value' : gov}, 'pl': {'language': 'pl', 'value' : gov}}, 'sitelinks': {}})[2][u'entity'][u'id'][1:])
			except:
				pass
		gov_page = DataPage(gov_wd)
		gov_page.setitem(summary=u'Spanish description', items={'type': u'description', 'language': 'es', 'value': 'político de España'})
		gov_page.setitem(summary=u'English description', items={'type': u'description', 'language': 'en', 'value': 'Spanish politician'})
		gov_page.setitem(summary=u'Polish description', items={'type': u'description', 'language': 'pl', 'value': 'polityk hiszpański'})
		mun_page.editclaim(6,gov_wd)

con.close()
