#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain wikidata property and compare it with this in sqlite
#

# system imports
from wikipedia import *
import sqlite3 as lite

# configure wiki
wikidata = getSite('wikidata', 'wikidata')

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
#cur.execute(u'SELECT wikidata, coa, flag, commons, image, es_page FROM municipio where (flag not like "{{%" and flag not null)')
#cur.execute(u'SELECT wikidata, coa, flag, commons, image, es_page FROM municipio where (coa not like "{{%" and coa not null)')
#cur.execute(u'SELECT wikidata, coa, flag, commons, image, es_page FROM municipio where (image not like "{{%" and image not null)')
#cur.execute(u'SELECT wikidata, coa, flag, commons, image, es_page FROM municipio where commons  like "Category:%"')
cur.execute(u'SELECT wikidata, coa, flag, commons, image, es_page FROM municipio where (coa not like "{{%" and coa not null) or (flag not like "{{%" and flag not null) or (image not like "{[%" and image not null) or (commons not like "{{%" and commons not null)')

data = cur.fetchall()

print len(data)

# check wikidata
for item in data:
	wd = item[0]
	coa = (item[1] if item[1] != None else '')
	flag = (item[2] if item[2] != None else '')
	commons = (item[3] if item[3] != None else '')
	image = (item[4] if item[4] != None else '')
	es_page = item[5]

#	print "COA: ", coa
#	print "FLAG: ", flag
#	print "COMMONS: ", commons
#	print "IMAGE: ", image	

	repo = wikidata.data_repository()
	data = DataPage(repo, wd).get()

	sql_upd = u'UPDATE municipio SET '

	for claim in data['claims']:
# coat of arms
		if claim['m'][1] == 94:
			if claim['m'][3].replace('_',' ') != coa.replace('_',' ') and coa != '' and coa != '{{#property:P94}}':
				print (('COA: ' + es_page + ' (' + wd + ') =>' + coa + '  ' + claim['m'][3]).encode('utf-8'))
			else:
				sql_upd += "coa='{{#property:P94}}', "
# flag
		elif claim['m'][1] == 41:
			if claim['m'][3].replace('_',' ') != flag.replace('_',' ') and flag != '' and flag != '{{#property:P41}}':
				print (('FLAG: ' + es_page +  ' (' + wd + ') =>' + flag  + ' != ' + claim['m'][3]).encode('utf-8'))
			else:
				sql_upd += "flag='{{#property:P41}}', "
# commons category
		elif claim['m'][1] == 373:
			if 'Category:'+claim['m'][3].replace('_',' ') != commons.replace('_',' ') and commons != '' and commons !='{{#property:P373}}':
				print (('COMMONS: ' + es_page + ' (' + wd + ') =>' + commons  + ' != ' + claim['m'][3]).encode('utf-8'))
			else:
				sql_upd += "commons='{{#property:P373}}', "					
# image
		elif claim['m'][1] == 18:
			if claim['m'][3].replace('_',' ') != image.replace('_',' ') and image != '' and image != '{{#property:P18}}':
				print (('IMAGE: ' + es_page + ' (' + wd + ') =>' + image  + ' != ' + claim['m'][3]).encode('utf-8'))
			else:
				sql_upd += "image='{{#property:P18}}', "
# phone prefix
		elif claim['m'][1] == 473:
			sql_upd += "phone_pref='{{#property:473}}', "

	if sql_upd[-2] != 'T':
		sql_upd = sql_upd[:-2] + ' where es_page="' + es_page + '"'
#		print '\t\t\t\t', sql_upd
		cur.execute(sql_upd)

con.close()
