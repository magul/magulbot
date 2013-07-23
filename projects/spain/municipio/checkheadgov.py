#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# check es_page's infobox if there is head of gov as a separate page
#


# extract template
def exttemp(name, text):
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
def temp2dict(template):
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
data = []#cur.fetchall()
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


# compare wikidata with eu.wiki
# Espainiako udalerri infotaula
#cur.execute(u'SELECT gov, eu_page_text, es_page, gov_wd from municipio where gov not null and eu_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Espainiako udalerri infotaula') != -1:
		tmpdict = temp2dict(exttemp('espainiako udalerri infotaula', text))
		if 'alkatea' in tmpdict:
			if tmpdict['alkatea'].find(u'[[') == 0:
				eu_gov = tmpdict['alkatea']
				eu_gov = eu_gov[2:] if eu_gov.find(u']]') == -1 else eu_gov[2:eu_gov.find(u']]')]
				gov_page = Page(getSite('eu', 'wikipedia'), eu_gov)
				if gov_page.exists():
					print gov, '==>', eu_gov, '==>', wd_gov, '==>', es
# Bizkaiko udalerri infotaula
#cur.execute(u'SELECT gov, eu_page_text, es_page, gov_wd from municipio where gov not null and eu_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Bizkaiko udalerri infotaula') != -1:
		tmpdict = temp2dict(exttemp('bizkaiko udalerri infotaula', text))
		if 'alkatea' in tmpdict:
			if tmpdict['alkatea'].find(u'[[') == 0:
				eu_gov = tmpdict['alkatea']
				eu_gov = eu_gov[2:] if eu_gov.find(u']]') == -1 else eu_gov[2:eu_gov.find(u']]')]
				gov_page = Page(getSite('eu', 'wikipedia'), eu_gov)
				if gov_page.exists():
					print gov, '==>', eu_gov, '==>', wd_gov, '==>', es
# Nafarroako udalerri infotaula
#cur.execute(u'SELECT gov, eu_page_text, es_page, gov_wd from municipio where eu_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Nafarroako udalerri infotaula') != -1:
		tmpdict = temp2dict(exttemp('nafarroako udalerri infotaula', text))
		if 'alkatea' in tmpdict:
			if tmpdict['alkatea'].find(u'[[') == 0:
				eu_gov = tmpdict['alkatea']
				eu_gov = eu_gov[2:] if eu_gov.find(u']]') == -1 else eu_gov[2:eu_gov.find(u']]')]
				gov_page = Page(getSite('eu', 'wikipedia'), eu_gov)
				if gov_page.exists():
					print gov, '==>', eu_gov, '==>', wd_gov, '==>', es
# Gipuzkoako udalerri infotaula
#cur.execute(u'SELECT gov, eu_page_text, es_page, gov_wd from municipio where eu_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Gipuzkoako udalerri infotaula') != -1:
		tmpdict = temp2dict(exttemp('gipuzkoako udalerri infotaula', text))
		if 'alkatea' in tmpdict:
			if tmpdict['alkatea'].find(u'[[') == 0:
				eu_gov = tmpdict['alkatea']
				eu_gov = eu_gov[2:] if eu_gov.find(u']]') == -1 else eu_gov[2:eu_gov.find(u']]')]
				gov_page = Page(getSite('eu', 'wikipedia'), eu_gov)
				if gov_page.exists():
					print gov, '==>', eu_gov, '==>', wd_gov, '==>', es
# Arabako udalerri infotaula
#cur.execute(u'SELECT gov, eu_page_text, es_page, gov_wd from municipio where eu_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Arabako udalerri infotaula') != -1:
		tmpdict = temp2dict(exttemp('arabako udalerri infotaula', text))
		if 'alkatea' in tmpdict:
			if tmpdict['alkatea'].find(u'[[') == 0:
				eu_gov = tmpdict['alkatea']
				eu_gov = eu_gov[2:] if eu_gov.find(u']]') == -1 else eu_gov[2:eu_gov.find(u']]')]
				gov_page = Page(getSite('eu', 'wikipedia'), eu_gov)
				if gov_page.exists():
					print gov, '==>', eu_gov, '==>', wd_gov, '==>', es

# compare wikidata with ca.wiki
# Infotaula del municipi balear
#cur.execute(u'SELECT gov, ca_page_text, es_page, gov_wd from municipio where gov not null and ca_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Infotaula del municipi balear') != -1:
		tmpdict = temp2dict(exttemp('infotaula del municipi balear', text))
		if 'batle' in tmpdict:
			if tmpdict['batle'].find(u'[[') == 0:
				ca_gov = tmpdict['batle']
				ca_gov = ca_gov[2:] if ca_gov.find(u']]') == -1 else ca_gov[2:ca_gov.find(u']]')]
				gov_page = Page(getSite('ca', 'wikipedia'), ca_gov)
				if gov_page.exists():
					print gov, '==>', ca_gov, '==>', wd_gov, '==>', es
# Infotaula del municipi basc
#cur.execute(u'SELECT gov, ca_page_text, es_page, gov_wd from municipio where gov not null and ca_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Infotaula del municipi basc') != -1:
		tmpdict = temp2dict(exttemp('infotaula del municipi basc', text))
		if 'alcalde' in tmpdict:
			if tmpdict['alcalde'].find(u'[[') == 0:
				ca_gov = tmpdict['alcalde']
				ca_gov = ca_gov[2:] if ca_gov.find(u']]') == -1 else ca_gov[2:ca_gov.find(u']]')]
				gov_page = Page(getSite('ca', 'wikipedia'), ca_gov)
				if gov_page.exists():
					print gov, '==>', ca_gov, '==>', wd_gov, '==>', es
# Infotaula del municipi valencià
#cur.execute(u'SELECT gov, ca_page_text, es_page, gov_wd from municipio where gov not null and ca_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Infotaula del municipi valencià') != -1:
		tmpdict = temp2dict(exttemp(u'infotaula del municipi valencià', text))
		if 'alcalde' in tmpdict:
			if tmpdict['alcalde'].find(u'[[') == 0:
				ca_gov = tmpdict['alcalde']
				ca_gov = ca_gov[2:] if ca_gov.find(u']]') == -1 else ca_gov[2:ca_gov.find(u']]')]
				gov_page = Page(getSite('ca', 'wikipedia'), ca_gov)
				if gov_page.exists():
					print gov, '==>', ca_gov, '==>', wd_gov, '==>', es
# Infotaula del municipi aragonès
#cur.execute(u'SELECT gov, ca_page_text, es_page, gov_wd from municipio where gov not null and ca_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Infotaula del municipi aragonès') != -1:
		tmpdict = temp2dict(exttemp(u'infotaula del municipi aragonès', text))
		if 'alcalde' in tmpdict:
			if tmpdict['alcalde'].find(u'[[') == 0:
				ca_gov = tmpdict['alcalde']
				ca_gov = ca_gov[2:] if ca_gov.find(u']]') == -1 else ca_gov[2:ca_gov.find(u']]')]
				gov_page = Page(getSite('ca', 'wikipedia'), ca_gov)
				if gov_page.exists():
					print gov, '==>', ca_gov, '==>', wd_gov, '==>', es
# Infotaula del municipi català
#cur.execute(u'SELECT gov, ca_page_text, es_page, gov_wd from municipio where gov not null and ca_page_text not null')
data = []#cur.fetchall()
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Infotaula del municipi català') != -1:
		tmpdict = temp2dict(exttemp(u'infotaula del municipi català', text))
		if 'alcalde' in tmpdict:
			tmpdict['alcalde'] = tmpdict['alcalde'].replace("''", "")
			if tmpdict['alcalde'].find(u'[[') == 0:
				ca_gov = tmpdict['alcalde']
				ca_gov = ca_gov[2:] if ca_gov.find(u']]') == -1 else ca_gov[2:ca_gov.find(u']]')]
				gov_page = Page(getSite('ca', 'wikipedia'), ca_gov)
				if gov_page.exists() and wd_gov == None:
					print gov, '==>', ca_gov, '==>', wd_gov, '==>', es
# Infotaula del municipi espanyol
cur.execute(u'SELECT gov, ca_page_text, es_page, gov_wd from municipio where gov not null and ca_page_text not null')
data = cur.fetchall()
i = 0
for item in data:
	es = item[2]
	text = item[1]
	gov = item[0]
	wd_gov = item[3]
	if text.find(u'Infotaula del municipi espanyol') != -1:
		tmpdict = temp2dict(exttemp(u'infotaula del municipi espanyol', text))
		if 'dirigent1' in tmpdict:
			tmpdict['dirigent1'] = tmpdict['dirigent1'].replace("''", "")
			if tmpdict['dirigent1'].find(u'[[') == 0:
				ca_gov = tmpdict['dirigent1']
				ca_gov = ca_gov[2:] if ca_gov.find(u']]') == -1 else ca_gov[2:ca_gov.find(u']]')]
				gov_page = Page(getSite('ca', 'wikipedia'), ca_gov)
				if gov_page.exists() and wd_gov == None:
					print gov, '==>', ca_gov, '==>', wd_gov, '==>', es
print i

con.close()

