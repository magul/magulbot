#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# checking if commons files exist
#

# system imports
from wikipedia import *
import sqlite3 as lite

# configure wiki
commons = getSite('commons', 'commons')

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
#cur.execute(u'SELECT wikidata, flag FROM municipio where flag not like "{{%" and flag not null')
cur.execute(u'SELECT wikidata, commons FROM municipio where commons not like "{{%" and commons not null')

data = cur.fetchall()

print len(data)

# check if file exists
for item in data:
	if not Page(commons, item[1]).exists():
		print item[0], ' => ', item[1]

con.close()
