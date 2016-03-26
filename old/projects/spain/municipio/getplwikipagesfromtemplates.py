#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain municipios of spain form plwiki and insert them in sqlite using municipios of province template
#


# system imports
from wikipedia import *
import sqlite3 as lite

# bot imports
from fixies import *

# configure plwiki
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)

# init municipio list
plpage_plprovince = []

# download templates of municipalies for every province
for province in provinces:
	page = Page(plwiki, u'Szablon:Prowincja ' + province)
	pagetext = page.get()

# find every plpage for municipio in templates
	pagetext = pagetext[pagetext.find(u'spis1'):pagetext.rfind(u'</div>')]
	muns = pagetext.split(u' • ')
	for idx, item in enumerate(muns):
		muns[idx] = item[item.find(u'[[')+2:item.find(u']]') if item.find(u'|')==-1 else item.find(u'|')]

# check for redirections	
	for idx, item in enumerate(muns):
		page = Page(plwiki, item)
		while page.isRedirectPage():
			print item + u' => ' + page.getRedirectTarget().title()
			item = page.getRedirectTarget().title()
			page = Page(plwiki, item)
		muns[idx] = item
	for item in muns:
		plpage_plprovince.append([item, province])

# write to sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
for result in plpage_plprovince:
	cur.execute(u'INSERT INTO municipio (current_plpage, pl_province) VALUES("'+result[0]+'", "'+result[1]+'")')
con.close()
