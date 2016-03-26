#! /usr/bin/python
# -*- coding: utf-8 -*-


# system imports
import urllib
import sqlite3 as lite
from bs4 import BeautifulSoup

# bot import
from fixies import *

# open sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
# 1. www_name
# 2. spanish_name, province alava, alicante, castelon, valencia
# 3. other_name with trunkated province names
# 4. name in two languages
cur.execute(u'select spanish_name, pl_province, nr_inscripcion from municipio where lat is null')
data = cur.fetchall()


unsucc = 0
# for every municipio
for item in data:
# and for every province
	for idx, province in enumerate(provinces):
		if province == item[1]:
			name = item[0]
			link = 'http://nominatim.openstreetmap.org/search/' + name.encode('utf-8') + ', ' + osm_provinces[idx].encode('utf-8')  + ', España?format=xml'
			xml_text = urllib.urlopen(link).read().decode('utf-8')
			soup = BeautifulSoup(xml_text)
# before class = boundary, type = administrative and class = place, type=city and class = place, type = village
			places = soup.find_all('place', class_="place", type="city" )
			if len(places) == 1:
				cur.execute(u'UPDATE municipio set lat=' + places[0]['lat'] + u', lon=' + places[0]['lon'] + u' where nr_inscripcion = "' + item[2] + u'"')
			elif len(places) > 1:
				same = 1
				lat = places[0]['lat']
				lon = places[0]['lon']
				for place in  places:
					if place['lat'] != lat or place['lon'] != lon:
						same = 0

				if same == 1:
					cur.execute(u'UPDATE municipio set lat=' + places[0]['lat'] + u', lon=' + places[0]['lon'] + u' where nr_inscripcion = "' + item[2] + u'"')
				else:
					unsucc += 1
					print len(places), u'BŁĄD => ', item[0], ', ', osm_provinces[idx]
			else:
				unsucc += 1
				print len(places), u'BŁĄD => ', item[0], ', ', osm_provinces[idx]

# close sqlite
con.close()


print 'UNSUCCESS => ', unsucc
