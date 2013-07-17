#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# get pl.wiki page and wikidata for austrian lands
#

# function that get all links from text
def get_links(text):
	links = []
	while text.find(u'[[') != -1:
		text = text[text.find(u'[[')+2:]
		if text.find(u'|') != -1:
			links.append(text[:min(text.find(u']]'),text.find(u'|'))])
		else:
			links.append(text[:text.find(u']]')])
	return links

# system imports
from wikipedia import *
import sqlite3 as lite

# configure plwiki
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)

# get pages from template
template = Page(plwiki, 'Szablon:Austria')
text = template.get()
text = text[text.find(u'<div>'):text.find(u'</div>')]
pages = get_links(text)

print pages
# init wikidata
wd = []
repo = plwiki.data_repository()

# fix redirects, get navs and wikidata
for idx, item in enumerate(pages):
# redirects
	page = Page(plwiki, item)
	while page.isRedirectPage():
		page = page.getRedirectTarget()
	pages[idx] = page.title()
# wikidata
	wd_page = DataPage(page)
	wd_page.get()
	wd.append(wd_page.title())

print wd

# write to sqlite
con = lite.connect('austria.sqlite', isolation_level=None)
cur = con.cursor()
for idx, item in enumerate(pages):
	cur.execute(u'INSERT INTO land (pl_page, wd) VALUES("'+item+'", "'+wd[idx]+'")')
con.close()
