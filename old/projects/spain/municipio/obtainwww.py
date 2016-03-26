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
	for item in list:
# strip white spaces
		key_value = item.strip()
# get key and value
		key = key_value[:key_value.find(u'=')].strip()
		value = key_value[key_value.find(u'=')+1:].strip()
		if len(value) != 0:
			temdict[key.lower()] = value

	return temdict

# system imports
import sqlite3 as lite

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT es_page_text, nr_inscripcion, es_page FROM municipio')
data = cur.fetchall()


for item in data:
	es_text = item[0]
	nr_ins = item[1]
	if es_text.lower().find(u'ficha de localidad de españa') != -1 or es_text.lower().find(u'ficha de entidad subnacional') != -1:
		if es_text.lower().find(u'ficha de localidad de españa') != -1:
			template = exttem(u'ficha de localidad de españa', es_text)
		else:
			template = exttem(u'ficha de entidad subnacional', es_text)
		temdict = tem2dict(template)
# www
		if es_text.lower().find(u'ficha de localidad de españa') != -1 and u'web' in temdict.keys():
			'web: ', temdict[u'web']
			www = temdict[u'web']

		elif u'página web' in temdict.keys():
			'pagina: ', temdict[u'página web']
			www = temdict[u'página web']
		print '==============> ', item[2]
		if www.find(u'[') != -1:
			www = www[www.find(u'[')+1:www.find(u']')]
			print www
			www = www.split()[0]
			print www
			
			cur.execute(u'UPDATE municipio set www = "'+ www + u'" where nr_inscripcion = "' +  nr_ins + '"')



# close sqlite connection
con.close()

