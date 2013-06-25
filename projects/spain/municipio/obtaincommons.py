#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain links to municipios websites
#

# extract template
def exttem(name, text):
	idx = text.lower().find(name)
	template = text[idx-2:]
	depth = 0
	for idx in range(len(template)):
		if template[idx:idx+2] == '{{':
			depth += 1
		if template[idx:idx+2] == '}}':
			depth -= 1
		if depth == 0:
			break
	return template[2:idx]

# create dictionary from template
def tem2dict(template):
# split using |
	temdict = dict()
	list = template.split(u'|')[1:]
	for idx, item in enumerate(list):
# strip white spaces
		key_value = item.strip()
# get key and value
		if key_value.find(u'=') != -1:
			key = key_value[:key_value.find(u'=')].strip().lower()
		else:
			key = idx
		value = key_value[key_value.find(u'=')+1:].strip()
		if len(value) != 0:
			temdict[key] = value

	return temdict

# system imports
from wikipedia import *
import sqlite3 as lite

# configure es.wiki
eswiki = getSite('es', 'wikipedia')

# names of searched templates
cattemplate = u'Plantilla:Commonscat'
pagetemplate = u'Plantilla:Commons'

catlist = map(Page.title, list(Page(eswiki, cattemplate).getReferences()))
pagelist = map(Page.title, list(Page(eswiki, pagetemplate).getReferences()))

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT nr_inscripcion, es_page, es_page_text FROM municipio where commons is null')
data = cur.fetchall()

nr = 0
for item in data:
	if item[1] in catlist and item[1] in pagelist:
		print "UWAGA!!!! ", item[1]
	elif item[1] in catlist:
		nr += 1
		catdict = tem2dict(exttem(u'commonscat', item[2]))
		if len(catdict) > 0:
			print item[1], ' ==> Category:', catdict[0]
			cur.execute(u'UPDATE municipio SET commons = "Category:' + catdict[0] + u'" where nr_inscripcion = "' + item[0] + u'"')
		else:
			print item[1], ' ==> Category:', item[1]
			cur.execute(u'UPDATE municipio SET commons = "Category:' + item[1] + u'" where nr_inscripcion = "' + item[0] + u'"')			
	elif item[1] in pagelist:
		nr += 1
		pagedict = tem2dict(exttem(u'commons', item[2]))
		if len(pagedict) > 0:
			if 0 in pagedict:
				print item[1], ' ==> ', pagedict[0]
				cur.execute(u'UPDATE municipio SET commons = "' + pagedict[0] + u'" where nr_inscripcion = "' + item[0] + u'"')
			else:
				print item[1], ' ==> ', pagedict[u'nombre']
				cur.execute(u'UPDATE municipio SET commons = "' + pagedict[u'nombre'] + u'" where nr_inscripcion = "' + item[0] + u'"')
		else:
			print item[1], ' ==> ', item[1]
			cur.execute(u'UPDATE municipio SET commons = "' + item[1] + u'" where nr_inscripcion = "' + item[0] + u'"')			

		
# close sqlite connection
con.close()

print nr
