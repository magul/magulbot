#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# retrive file from website of ministry of finance and public administration
# it is using beatuful soup


# system imports
import sqlite3 as lite
import csv, urllib
from bs4 import BeautifulSoup

# bot imports
from fixies import *


# populate sqlite if there's exact names



con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

for idx, province in enumerate(provinces):
	with open('mun_exp.csv', 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			if row[3].decode("utf-8") == csv_provinces[idx]:
				cur.execute(u'UPDATE municipio set nr_inscripcion="' + row[4].decode("utf-8") + u'" WHERE pl_province="' + province + u'" AND csv_name="' + row[6].decode("utf-8") + u'"')


# retrive data from website and parse it
for i in range(0, 325):
	htmltext = urllib.urlopen('http://ssweb.mpt.es/REL/frontend/inicio/municipios/all/all/'+str(i*25)).read()
	soup = BeautifulSoup(htmltext)
	numbers =  soup.find_all('td', class_="ac")
	names = soup.find_all('td', class_="al")
	for j in range(25):
		print numbers[j*2].get_text().strip()[1:], names[j*4+2].get_text().strip()
		cur.execute(u'UPDATE municipio set www_name="' + names[j*4+2].get_text().strip() + u'" where nr_inscripcion="'+numbers[j*2].get_text().strip()[1:]+u'"')

con.close()
