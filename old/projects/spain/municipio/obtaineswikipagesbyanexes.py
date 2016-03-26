#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain pages of municipios of spain from es.wiki
#


# function check row for occurence of name of municipio
def in_row(row, name):
	return (row.find(u'[['+name) != -1 or row.find(u'|'+name+u']]') != -1 or row.find(u'('+name+u')') != -1 or row.find(u'| '+name) != -1 or row.find(u"(''"+name+"'')") != -1)


# system imports
from wikipedia import *
import sqlite3 as lite

# bot imports
from fixies import *

# configure plwiki
pllang = 'pl'
family = 'wikipedia'
eslang = 'es'
plwiki = getSite(pllang, family)
eswiki = getSite(eslang, family)

# download es.wiki anex of municipies
whole_anex_text = Page(eswiki, u'Anexo:Municipios de España').get()
whole_anex_text = whole_anex_text[whole_anex_text.find(u'== Municipios por provincia =='):whole_anex_text.find(u'== Municipios más poblados ==')]

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

unsuccess=0

for province in provinces:
# get name of province's pl_page
	page = Page(plwiki, u'Szablon:Prowincja ' + province)
	pagetext = page.get()
	pagetext = pagetext[pagetext.find(u'tytuł'):]
	pl_prov_page = pagetext[pagetext.find(u'[[')+2:pagetext.find(u'|')]
# get province anex's es_page
	pl_prov_page = Page(plwiki, pl_prov_page)
	data = DataPage(pl_prov_page)
	interwikis = data.interwiki()
	for interwiki in interwikis:
		if interwiki.site == eswiki:
			es_prov_name = interwiki.title()
	if es_prov_name.find(u'(') != -1:
		es_prov_name = es_prov_name[:es_prov_name.find(u'(')-1]
	if es_prov_name.lower().find(u'provincia de') != -1:
		es_prov_name = es_prov_name[13:]
	if es_prov_name.lower().find(u'principado de') != -1:
                es_prov_name = es_prov_name[14:]
	place_in_whole = whole_anex_text.find(es_prov_name)
	anex = whole_anex_text[whole_anex_text.rfind(u'[[', 0, place_in_whole)+2:whole_anex_text.find(u'|', place_in_whole)]
	anex_page = Page(eswiki, anex)
	while anex_page.isRedirectPage():
		anex_page = anex_page.getRedirectTarget()
	anex_text = anex_page.get()
# get rows in wikitable
	table_start = anex_text.rfind(u'wikitable')
	table_end = anex_text.find(u'|}', table_start)
	anex_table = anex_text[table_start:table_end]
	rows = anex_table.split(u'|-')

# get all municipios for province
	cur.execute(u'SELECT spanish_name, other_name, nr_inscripcion FROM municipio where pl_province="' + province + u'" and es_page is null')
	sql_result = cur.fetchall()
	for sql_rec in sql_result:
		sp = sql_rec[0]
		ot = sql_rec[1]
		row_nr = -1
		rows_ct = 0
# check rows in wikitable for them
		for idx, row in enumerate(rows):
			if in_row(row, sp) or (ot != None and in_row(row, ot)):
				row_nr = idx
				rows_ct += 1
		if rows_ct != 1:
			unsuccess += 1
# if they appear only once, then get page title
		else:
			es_page = rows[row_nr]
			es_page = es_page[es_page.find(u'[[')+2:]
			while es_page.find(u':') != -1 and es_page.find(u':') < es_page.find(u']]'):
				es_page = es_page[es_page.find(u'[[')+2:]
			es_page = es_page[:min(es_page.find(u']]'), es_page.find(u'|'))]
			es_page = Page(eswiki, es_page)
			while es_page.isRedirectPage():
				es_page = es_page.getRedirectTarget()
# if page has a template
			template = Page(eswiki, u'Template:Ficha de localidad de España')
			templates = es_page.getTemplates()
			if template in templates:
				es_page = es_page.title()
				cur.execute(u'UPDATE municipio set es_page="' + es_page + u'" where nr_inscripcion = "' + sql_rec[2] + u'"')
			else:
				unsuccess += 1
			


#print unsuccess
print 'UNSUCCESSFULL => ', unsuccess

# close sqlite connection
con.close()
