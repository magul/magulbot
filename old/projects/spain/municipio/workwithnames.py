#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# this script retrive spanish and other language names from official typonyme
#


# function deling with prefixes after coma
def deal_with_prefix(origin_name = u''):
	if origin_name == None:
		return None
	elif origin_name.find(u', ') == -1:
		return origin_name
	else:
		prefix = origin_name[origin_name.find(u', ')+2:]
		prefix = prefix[0].upper()+prefix[1:]
		name = origin_name[:origin_name.find(u', ')]
		if prefix == u"L'":
			name = prefix+name
		else:
			name = prefix+u' '+name
		return name
#
# main program
#
# system imports
import sqlite3 as lite
import csv

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT nr_inscripcion, www_name from municipio where spanish_name is null')
data = cur.fetchall()

for item in data:
# split spanish name and other name
	other_name = None
	name = item[1]
	number = item[0]
	if name.find(u'/') != -1:
		spanish_name = name[:name.find(u'/')]
		other_name = name[name.find(u'/')+1:]
	else:
		spanish_name = name
# find default sort (prefix after coma, with first letter capitalized)
	if spanish_name.find(u', ') != -1:
		default_sort = spanish_name[:spanish_name.find(u', ')+2] + spanish_name[spanish_name.find(u', ')+2].upper()+spanish_name[spanish_name.find(u', ')+3:]
	else:
		default_sort = spanish_name

# moving prefix to the beginnig of name
	spanish_name = deal_with_prefix(spanish_name)
	other_name = deal_with_prefix(other_name)

	if other_name == None:
		cur.execute(u'UPDATE municipio set default_sort = "' + default_sort + '", spanish_name = "' + spanish_name + u'" where nr_inscripcion = "' + number + u'"')
	else:
		cur.execute(u'UPDATE municipio set default_sort = "' + default_sort + '", spanish_name = "' + spanish_name + u'", other_name = "' + other_name + '" where nr_inscripcion = "' + number + u'"')

	print spanish_name

con.close()


