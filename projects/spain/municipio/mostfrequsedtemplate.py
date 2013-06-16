#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain municipios of spain form plwiki and insert them in sqlite using municipios of province template
#


# system imports
from wikipedia import *
import sqlite3 as lite
import operator

# configure plwiki
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)

# get every plpage frm sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT current_plpage from municipio')
data = cur.fetchall()
con.close()

template_count = dict()

# count every temaplate on existing pages
for item in data:
	page = Page(plwiki, item[0])
	if page.exists:
		page_list = page.getTemplates()
		for template in page_list:
			if not (template.title()[8:] in template_count):
				template_count[template.title()[8:]] = 0
			template_count[template.title()[8:]] += 1


sorted_templates = sorted(template_count.iteritems(), key=operator.itemgetter(1))

for item in sorted_templates:
	print item
