#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# get area and population from csv exported from ministry of finance and puclic administration
#


# system imports
import sqlite3 as lite
import csv

# bot imports
from fixies import *

# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()

# get population and adrea and density from csv ...
with open('mun_exp.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		nr_ins = row[4]
		area = row[8].replace(",", ".")
		pop = row[9]
		den = row[10].replace(",", ".")
		if float(den) != round(float(pop)/float(area), 2):
			print nr_ins, "|", area, "|", pop, "|", den, " =? ", float(pop)/float(area)
# ... and write them to sqlite
		else:
			cur.execute(u'UPDATE municipio SET population = ' + pop + u', area = ' + area + u' WHERE nr_inscripcion = ' + nr_ins )
	
# close sqlite connection
con.close()
