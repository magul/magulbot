#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain coat of arms and flags from es.wiki templates
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


escudo = 0
bandera = 0
no_e = [u'Coats of arms of None.svg', u'no', u'si']
no_b = [u'no', u'Flag of None.svg', u'Missing flag.png']
e_dict = dict()
b_dict = dict()
for item in data:
	es_text = item[0]
	nr_ins = item[1]
	if es_text.lower().find(u'ficha de localidad de españa') != -1 or es_text.lower().find(u'ficha de entidad subnacional') != -1:
		if es_text.lower().find(u'ficha de localidad de españa') != -1:
			template = exttem(u'ficha de localidad de españa', es_text)
		else:
			template = exttem(u'ficha de entidad subnacional', es_text)
		temdict = tem2dict(template)
# for coa
		if u'escudo' in temdict.keys() and not (temdict[u'escudo'] in no_e):
			escudo += 1
			if temdict[u'escudo'] in e_dict.keys():
				e_dict[temdict[u'escudo']] = e_dict[temdict[u'escudo']]+1
			else:
				e_dict[temdict[u'escudo']] = 1
			cur.execute(u'UPDATE municipio set coa = "'+ temdict[u'escudo'] + u'" where nr_inscripcion = "' +  nr_ins + '"')
# for flag
		if u'bandera' in temdict.keys() and not (temdict[u'bandera'] in no_b):
			bandera += 1
                        if temdict[u'bandera'] in b_dict.keys():
                                b_dict[temdict[u'bandera']] = b_dict[temdict[u'bandera']]+1
                        else:
                                b_dict[temdict[u'bandera']] = 1
			cur.execute(u'UPDATE municipio set flag = "'+ temdict[u'bandera'] + u'" where nr_inscripcion = "' +  nr_ins + '"')
	else:
		print item[2]

# close sqlite connection
con.close()

print "COAT OF ARMS"
for key in e_dict:
	if e_dict[key] > 1:
		print key
print "FLAG"
for key in b_dict:
	if b_dict[key] > 1:
		print key



print 'ESCUDO: ', escudo, ', BANDERA: ', bandera
