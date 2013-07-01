#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# retrive db offset from www
# it is using beatuful soup


# system imports
import sqlite3 as lite
import csv, urllib
from bs4 import BeautifulSoup

# bot imports
from fixies import *

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

# retrive data from website and parse it
for i in range(238, 325):
	htmltext = urllib.urlopen('http://ssweb.mpt.es/REL/frontend/inicio/municipios/all/all/'+str(i*25)).read()
	soup = BeautifulSoup(htmltext)
	numbers =  soup.find_all('td', class_="ac")
	for j in range(25):
		cur.execute(u'SELECT db_offset FROM municipio where nr_inscripcion="'+numbers[j*2].get_text().strip()[1:]+u'"')
		if numbers[j*2].get_text().strip()[1:] != u'1510013' and numbers[j*2].get_text().strip()[1:] != u'1520018' and  cur.fetchall()[0][0] == None:
			cur.execute('UPDATE municipio set db_offset="'+ str(i*25) + u'" where nr_inscripcion="'+numbers[j*2].get_text().strip()[1:]+u'"')
			print 'UPDATE: ' , numbers[j*2].get_text().strip()[1:]
		else:
			print u'=======================================> ERROR: ', numbers[j*2].get_text().strip()[1:]
		

con.close()
