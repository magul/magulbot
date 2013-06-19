#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain pages of municipios of spain from es.wiki
#


# system imports
from wikipedia import *
import sqlite3 as lite
import webbrowser

# bot imports
from fixies import *

# configure wiki
eslang = 'es'
family = 'wikipedia'
eswiki = getSite(eslang, family)

# get all references of template
# before that was u'Template:Ficha de localidad de España'
template = Page(eswiki, u'Template:Ficha de entidad subnacional')
es_pages = map(Page.title, list(template.getReferences()))

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()


cur.execute(u'SELECT spanish_name, other_name, nr_inscripcion FROM municipio WHERE es_page IS NULL')

sql_result =  cur.fetchall()

sql_dict = {}

for sql_rec in sql_result:
	for page in es_pages:
		if page.find(sql_rec[0]) == 0:
			if sql_rec[0] in sql_dict.keys():
				value = [page, ]
				value.extend(sql_dict[sql_rec[0]])
				sql_dict[sql_rec[0]] = value
			else:
				sql_dict[sql_rec[0]] = [page, ]
		if (sql_rec[1] != None and page.find(sql_rec[1]) == 0):
			if sql_rec[0] in sql_dict.keys():
				value = [page, ]
				value.extend(sql_dict[sql_rec[0]])
				sql_dict[sql_rec[0]] = value
			else:
				sql_dict[sql_rec[0]] = [page, ]


for key in sql_dict:
	if len(sql_dict[key]) > 1:
		pass
	else:
		for sql_rec in sql_result:
			if key == sql_rec[0]:
				cur.execute(u'UPDATE municipio SET es_page = "' + sql_dict[key][0] + '" WHERE nr_inscripcion = "'+ sql_rec[2] + u'"')
				print key, u' => ', sql_dict[key][0]

# close sqlite connection
con.close()
