#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# obtain images from es.page
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

# check if it's correct image
def correct(name):
	global image
	image_page = Page(commons, name)
	if image_page.exists():
		while image_page.isRedirectPage():
			image_page = image_page.getRedirectTarget()
		image = image_page.title()
		categories = image_page.categories()
		ismap = 0
		for cat in categories:
			if cat.title().lower().find(u'maps ') != -1:
				ismap = 1
		if ismap == 0:
			return True
		else:
			return False
	else:
		return False



# system imports
import sqlite3 as lite
from wikipedia import *


# configure common
commons = getSite('commons', 'commons')

nr_images = 0
# open sqlite connection
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT es_page_text, nr_inscripcion, es_page FROM municipio where image is null')
data = cur.fetchall()


row = 0
for item in data:
	row += 1
	es_text = item[0]
	nr_ins = item[1]
	if es_text.lower().find(u'ficha de localidad de españa') != -1 or es_text.lower().find(u'ficha de entidad subnacional') != -1:
		if es_text.lower().find(u'ficha de localidad de españa') != -1:
			template = exttem(u'ficha de localidad de españa', es_text)
		else:
			template = exttem(u'ficha de entidad subnacional', es_text)
		temdict = tem2dict(template)
# image with wiki link
		if u'imagen' in temdict.keys():
			image = temdict[u'imagen']
# try as a wiki link
			if image.find(u'[[') != -1:
				image = image[image.find(u'[[')+2:]
				if image.find(u']]') != -1:
					image = image[:image.find(u']]')]
				image = u'File:'+image.split(u':')[1]
				if correct(image):
					print row, ' : ', image, ' => ', Page(commons, image).categories()
 					cur.execute(u"UPDATE municipio SET image = '"+image[image.find(u':')+1:].replace("'", "''")+u"' where nr_inscripcion = '" + nr_ins +u"'")
					nr_images += 1
# try simple image
			elif image.find(u'{{') == -1:
				image = u'File:'+image
				if correct(image):
					print row, ' : ', image, ' => ', Page(commons, image).categories()
 					cur.execute(u"UPDATE municipio SET image = '"+image[image.find(u':')+1:].replace("'", "''")+u"' where nr_inscripcion = '" + nr_ins +u"'")
					nr_images += 1
# montage
			else:
				if image.lower().find(u'{{montaje fotográfico') != -1:
					image = temdict['foto1a']
					if image.find(u'{{!}}') != -1:
						image = image.split(u'{{!}}')[0]
					if correct(image):
						print row, ' : ', image, ' => ', Page(commons, image).categories()
	 					cur.execute(u"UPDATE municipio SET image = '"+image[image.find(u':')+1:].replace("'", "''")+u"' where nr_inscripcion = '" + nr_ins +u"'")
						nr_images += 1
# close sqlite connection
con.close()


print nr_images
