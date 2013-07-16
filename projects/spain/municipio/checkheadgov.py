#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# check es_page's infobox if there is head of gov as a separate page
#


# extract template
def exttem(name, text):
	idx = text.lower().find(u'{{'+name)
	template = text[idx:]
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
import sqlite3 as lite
from wikipedia import *

eswiki = getSite('es','wikipedia')

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
# Ficha de localidad de Espana
cur.execute(u'SELECT es_page_text , es_page, gov from municipio where es_page_text like "%Ficha de localidad%"')
data = cur.fetchall()
for item in data:
	tempasdict = tem2dict(exttem(u'ficha de localidad', item[0]))
	if u'alcalde' in tempasdict:
		alcalde = tempasdict[u'alcalde']
	elif u'alcaldesa' in tempasdict:
		alcalde = tempasdict[u'alcaldesa']
	else:
		continue
	if u'[['==alcalde[:2]:
		alcalde = alcalde[2:]
		if alcalde.find(u']]')!= -1:
			alcalde = alcalde[:alcalde.find(u']]')]
		if Page(eswiki, alcalde).exists():
			print item[2], '==>', alcalde



cur.execute(u'SELECT es_page_text , es_page from municipio where es_page_text like "%Ficha de entidad subn%"')
data = cur.fetchall()

con.close()
