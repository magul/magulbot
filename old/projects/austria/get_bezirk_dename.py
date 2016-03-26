#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# get population of austrian bezrike
# http://www.statistik.at/web_de/klassifikationen/regionale_gliederungen/politische_bezirke/index.html

# system imports
import csv, urllib
import sqlite3 as lite

# csv init
csv.register_dialect('semi', delimiter=';')
csvfile = open('politische_bezirke_csv_ca._5kb_022948.csv', 'rb')
csvreader = csv.reader(csvfile, dialect='semi')

# sqlite init
con = lite.connect('austria.sqlite', isolation_level=None)
cur = con.cursor()

# main loop
for item in csvreader:
	land_id = unicode(item[0].decode('windows-1252'))
	land_name = unicode(item[1].decode('windows-1252'))
	bezirk_id = unicode(item[2].decode('windows-1252'))
	bezirk_name = unicode(item[3].decode('windows-1252'))
	is_stadt = (u'stadt' if bezirk_name.find(u'(Stadt)') != -1 else u'land')
	bezirk_name = bezirk_name.split(u'(')[0]
	print bezirk_id, bezirk_name, '==>', is_stadt
#	cur.execute("UPDATE land set ziffer='" + land_id + "' where de_name='" + land_name + "'")
	cur.execute("insert into bezirk(de_name, is_stadt, ziffer) values('" + bezirk_name + "', '" + is_stadt + "', '" + bezirk_id + "')")


# closing files
csvfile.close()
con.close()
