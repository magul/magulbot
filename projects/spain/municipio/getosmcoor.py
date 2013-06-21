#! /usr/bin/python
# -*- coding: utf-8 -*-


# system imports
import urllib

places = [u'San Lorenzo de la Parrilla, Cuenca, Castilla-La Mancha, España']


for place in places:
	xml_text = urllib.urlopen('http://nominatim.openstreetmap.org/search/' + place.encode('utf-8') + '?format=xml').read().decode('utf-8')
	if xml_text.count(u'<place place_id') == 1:
		lat = xml_text[xml_text.find(u"lat='"):]
		lat = lat[lat.find(u"'")+1:]
		lat = lat[:lat.find(u"'")]
		lon = xml_text[xml_text.find(u"lon='"):]
		lon = lon[lon.find(u"'")+1:]
		lon = lon[:lon.find(u"'")]
		print place, " => ", lat, ",", lon
	else:
		print u'BŁĄD => ', place
