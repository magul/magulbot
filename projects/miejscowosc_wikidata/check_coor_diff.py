#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script check the difference beteween pl.wiki and wikidata in the matter of coordinates for infoboks miejscowość
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


import pwb, csv
from pywikibot import *

s = Site('pl', 'wikipedia')
r = s.data_repository()

t = Page(s, u'Szablon:Miejscowość infobox')
lp = t.getReferences()

f = open('csv.csv', 'wb')
csvw = csv.writer(f, delimiter=';', quotechar='"')

#dont_check = [u'Castellón de la Plana']

for pl_page in lp:
    text = pl_page.get()
    if pl_page.namespace() == 0:
        print pl_page
        tmp = tem2dict(exttem(u'miejscowość infobox', text))
        degN = (tmp['stopnin'] if 'stopnin' in tmp else '')
        degS = (tmp['stopnis'] if 'stopnis' in tmp else '')
        degE = (tmp['stopnie'] if 'stopnie' in tmp else '')
        degW = (tmp['stopniw'] if 'stopniw' in tmp else '')
        minN = (tmp['minutn'] if 'minutn' in tmp else '')
        minS = (tmp['minuts'] if 'minuts' in tmp else '')
        minE = (tmp['minute'] if 'minute' in tmp else '')
        minW = (tmp['minutw'] if 'minutw' in tmp else '')
        secN = (tmp['sekundn'] if 'sekundn' in tmp else '')
        secS = (tmp['sekunds'] if 'sekunds' in tmp else '')
        secE = (tmp['sekunde'] if 'sekunde' in tmp else '')
        secW = (tmp['sekundw'] if 'sekundw' in tmp else '')
        wd_page = ItemPage.fromPage(pl_page)
        if wd_page.exists():
            wd_page.get()
            wd_page_title = wd_page.title()
            print wd_page
            if 'p625' in wd_page.claims:
                wd_coor = wd_page.claims['p625'][0].getTarget()
                wd_lon = wd_coor.lon
                wd_lat = wd_coor.lat
            else:
                wd_lon = ''
                wd_lat = ''
        else:
            wd_lon = ''
            wd_lat = ''
            wd_page_title = ''
        csvw.writerow([pl_page.title().encode('utf-8'), wd_page_title, degN, minN, secN, degS, minS, secS, degE, minE, secE, degW, minW, secW, wd_lat, wd_lon]) 

f.close()
