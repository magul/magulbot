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

for idx, province in enumerate(provinces):
	if plwiki_count[idx] != csv_count[idx]:
		print province + u' => plwiki: ' + str(plwiki_count[idx]) + u', csv: ' + str(csv_count[idx])
