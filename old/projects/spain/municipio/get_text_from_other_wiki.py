#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# get text of pages of munisipality from other spanish wikis
#

# system imports
import sqlite3 as lite
from wikipedia import *

# init sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

# sqlite select
cur.execute(u'SELECT wikidata from municipio WHERE not (eu_page_text not null or ca_page_text not null or gl_page_text not null or an_page_text not null or ast_page_text not null or ext_page_text not null)')
data = cur.fetchall()

# create sites
wd_site = getSite('wikidata', 'wikidata').data_repository()
langs = ['eu', 'ca', 'gl', 'an', 'ast', 'ext']
others = {}
for lang in langs:
	others[lang] = getSite(lang, 'wikipedia')
# main loop
for item in data:
	texts = {}
	wd_page = DataPage(wd_site, item[0])
	wd_page.get()
	iws = wd_page.interwiki()
	print iws
	for iw in iws:
		if iw.site() in others.values():
			texts[iw.site().code+'_page_text'] = iw.get().replace("'", "''")
	if len(texts) > 0:
		upd_st = u'UPDATE municipio set '
		for lang in texts:
			upd_st += lang + u" = '" + texts[lang] + "',"
		upd_st = upd_st[:-1] + u" WHERE wikidata='" + item[0] + "'"
		cur.execute(upd_st)

con.close
