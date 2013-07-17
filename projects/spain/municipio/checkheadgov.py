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
#cur.execute(u'SELECT es_page_text , es_page, gov from municipio where es_page_text like "%Ficha de localidad%"')
data = []#cur.fetchall()
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
		es_page = Page(eswiki, alcalde)
		if es_page.exists():
			while es_page.isRedirectPage():
				es_page = es_page.getRedirectTarget()
			data_page = DataPage(es_page)
			data_page.get()
			cur.execute(u'UPDATE municipio set gov_wd="'+data_page.title()+'" where es_page="'+item[1]+'"')
#Ficha de entidad subn
#cur.execute(u'SELECT es_page_text , es_page, gov from municipio where es_page_text like "%Ficha de entidad subn%"')
data = []#cur.fetchall()
for item in data:
	tempasdict = tem2dict(exttem(u'ficha de entidad subn', item[0]))
	alcalde = tempasdict[u'dirigentes_nombres']
	if alcalde.find(u'[[') == 0:
		alcalde = alcalde[2:]
		if alcalde.find(u']]') != -1:
			alcalde = alcalde[:alcalde.find(u']]')]
		es_page = Page(eswiki, alcalde)
		if es_page.exists():
			while es_page.isRedirectPage():
				es_page = es_page.getRedirectTarget()
			data_page = DataPage(es_page)
			data_page.get()
			print es_page.title()
			print data_page.title()
			cur.execute(u'UPDATE municipio set gov_wd="'+data_page.title()+'" where es_page="'+item[1]+'"')

# compare es.wiki with wikidata
repo = eswiki.data_repository()
cur.execute(u'SELECT wikidata, gov_wd, gov from municipio')
data = cur.fetchall()
for item in data:
	sql_mun = item[0]
	if item[1]!=None:
		sql_alc = int(item[1][1:])
	else:
		sql_alc = None
	wd = DataPage(repo, item[0]).get()
	wd_alc = None
	claim_ct = 0
	for claim in wd['claims']:
		if claim['m'][1] == 6:
			claim_ct += 1
			wd_alc = claim['m'][3]['numeric-id']
	if claim_ct > 1:
		print sql_mun, '===> too much alcalde for municipio'
		continue
	if wd_alc != sql_alc and wd_alc != None:
		print sql_mun, '===> alcalde not equal:', (sql_alc if sql_alc!=None else u'None'), '!=', wd_alc, '(in database:', item[2], ')'

con.close()
