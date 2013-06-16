#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# compare results from plwiki in sqlite with csv file exported from ministry of finance and public administration
#


# system imports
import sqlite3 as lite
import csv

# bot imports
from fixies import *

# count municipios by provinces from plwiki
plwiki_count=[]
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
for province  in provinces:
	cur.execute(u'SELECT COUNT(*) from municipio where pl_province="'+province+u'"')
	plwiki_count.append(cur.fetchone()[0])
con.close()

# count municipios by provinces from csv
csv_count = [0 for _ in csv_provinces]
for idx, province in enumerate(csv_provinces):
	with open('mun_exp.csv', 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			if row[3].decode("utf-8") == province:
				csv_count[idx] += 1

# write in stdout all differences in number of municipios
for idx, province in enumerate(provinces):
	if plwiki_count[idx] != csv_count[idx]:
		print province + u' => plwiki: ' + str(plwiki_count[idx]) + u', csv: ' + str(csv_count[idx])

# populate sqlite if there's exact names
successcount = 0
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
for idx, province in enumerate(provinces):
	with open('mun_exp.csv', 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			if row[3].decode("utf-8") == csv_provinces[idx]:
				cur.execute(u'SELECT COUNT(*) from municipio where pl_province="'+province+u'" and current_plpage="'+row[6].decode("utf-8")+u'" and csv_name IS NULL')
				if cur.fetchone()[0] == 1:
					successcount += 1
					cur.execute(u'UPDATE municipio set csv_name="'+row[6].decode("utf-8")+u'" where pl_province="'+province+u'" and current_plpage="'+row[6].decode("utf-8")+u'"  and csv_name IS NULL')

con.close()
print u"EXACT SUCCESSES: " + str(successcount)
