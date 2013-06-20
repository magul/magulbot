#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# check if it's real es_page
#


# system imports
from wikipedia import *
import sqlite3 as lite
import webbrowser


# bot imports
from fixies import *

# configure wiki
eslang = 'es'
pllang = 'pl'
enlang = 'en'
family = 'wikipedia'
eswiki = getSite(eslang, family)
plwiki = getSite(pllang, family)
enwiki = getSite(enlang, family)

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()


es_problems = []
en_problems = []
# get es_wiki pages of provinces
for province in provinces:
	pl_prov_templ = Page(plwiki, u'Szablon:Prowincja ' + province)
	pagetext = pl_prov_templ.get()
        pagetext = pagetext[pagetext.find(u'tytuł'):]
        pl_prov_page = pagetext[pagetext.find(u'[[')+2:pagetext.find(u'|')]
	print pl_prov_page
	pl_prov_iw = Page(plwiki, pl_prov_page).interwiki()
	for i in pl_prov_iw:
		if eswiki == i.site():
			es_prov = i
		if enwiki == i.site():
			en_prov = i
	while es_prov.isRedirectPage():
		es_prov = es_prov.getRedirectTarget()
	while en_prov.isRedirectPage():
		en_prov = en_prov.gerRedirectTarget()

# get referebces
	es_ref =  map(Page.title, list(es_prov.getReferences()))
	en_ref = map(Page.title, list(en_prov.getReferences()))
	cur.execute(u'SELECT es_page FROM municipio WHERE pl_province = "' + province + u'"')
	data = cur.fetchall()
	for item in data:
		if not (item[0] in es_ref):
			es_problems.append(item[0])
		es_page = Page(eswiki, item[0])
		es_page_in = es_page.interwiki()
		for i in es_page_in:
			if enwiki == i.site():
				en_page = i.title()
		if not (en_page in en_ref):
			en_problems.append(item[0])
			webbrowser.open(u'https://es.wikipedia.org/wiki/' + es_page.title())
	print 'ES: ', len(es_problems), '      | EN: ', len(en_problems)

		
# close sqlite connection
con.close()


print "============================================================================================="
print 'ES'
for item in es_problems:
	print item
print len(es_problems)

print 'EN'
for item in en_problems:
	print item
print len(en_problems)
