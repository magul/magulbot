#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtaining head of goverment
#


# system imports
import sqlite3 as lite
import csv, urllib

# bot imports
from fixies import *

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute('SELECT wikidata, www_name, pl_province, es_page_text FROM municipio WHERE gov IS NULL')
data = cur.fetchall()

# open csv and start parsing
ct = 0
for item in data:
	thereisnot = True
	with open('headofgoverment.csv', 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			if unicode(row[0], 'utf-8') == item[2] and unicode(row[1],'utf-8') == item[1]:
				mayor = (unicode(row[2], 'utf-8') + ' ' + unicode(row[3], 'utf-8') + ' ' + unicode(row[4], 'utf-8')).strip()
				listofm = map(unicode.lower, mayor.split())
				mayor = u''
				for i in listofm:
					if i!='y' and i!=u'las' and i!=u'de' and i!=u'del' and i!='la' and i!=u'los' and i!='i':
						i = i.title()
					mayor += i + ' '
				mayor = mayor.strip()
				if len(mayor)!=0:
					print 'UPDATE municipio SET gov="'+mayor+'" WHERE wikidata="'+item[0]+'"'
					cur.execute('UPDATE municipio SET gov="'+mayor+'" WHERE wikidata="'+item[0]+'"')
print ct
# close sqlite
con.close()
