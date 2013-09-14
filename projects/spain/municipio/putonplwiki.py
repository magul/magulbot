#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# put on pl.wiki and add interwiki links
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
        list = template.split(u'\n| ')[1:]
        for idx, item in enumerate(list):
# strip white spaces
                key_value = item.strip()
# get key and value
                if key_value.find(u'=') != -1:
                        key = key_value[:key_value.find(u'=')].strip().lower()
                else:
                        key = idx
                value = key_value[key_value.find(u'=')+1:].strip()
                if len(value) != 0:
                        temdict[key] = value

        return temdict


# if >= 10000 divide number to 3-digit blocs
def divide(number):
	ret_str = ''
	if number > 9999:
		ret_str = str(number%1000).zfill(3)
		number /= 1000
		while number != 0:
			ret_str = str(number%1000).zfill(3) + u' ' + ret_str
			number /= 1000
		while ret_str[0] == u'0':
			ret_str= ret_str[1:]
		return ret_str	
	else:
		return str(number)	

# system imports
from wikipedia import *
import catlib
import sqlite3 as lite
from utils.sk.sk import sk

# bot imports
from fixies import *

# configure plwiki
pllang = 'pl'
plfamily = 'wikipedia'
plwiki = getSite(pllang, plfamily)

# create dict of polish pages of autonomies communities
auto_com = dict()
cat = catlib.Category(plwiki, u'Kategoria:Szablony nawigacyjne - podziały administracyjne wspólnot autonomicznych Hiszpanii')
auto_com_temp = cat.articlesList()
for temp in auto_com_temp:
	text = temp.get()
	value = tem2dict(exttem(u'navbox', text))[u'tytuł'].split(u'[[')[-1].split(u'|')[0]
	for prov in provinces:
		if prov in text:
			auto_com[prov] = value
auto_com[u'Cuenca'] = u'Kastylia-La Mancha'

# create dict of polish pages of provinces
prov = dict()
for province in provinces:
	text = Page(plwiki, u'Szablon:Prowincja ' + province).get()
	value = tem2dict(exttem(u'navbox', text))[u'tytuł'].split(u'[[')[-1].split(u'|')[0]
	prov[province] = value

# get data from sqlite
con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT population, area, commons, image, www, flag, coa, lon, lat, wikidata, other_language, default_sort, other_name, spanish_name, current_plpage, pl_province, db_offset, gov FROM municipio')
data = cur.fetchall()
#data = []
con.close()

# limit edit
max_edits = 5000
edit_ct = 0

# for every row in data
for row in data[6840:]:
# extract data from tuple
	population = row[0]
	area = row[1]
	commons = row[2]
	image = row[3]
	www = row[4]
	flag = row[5]
	coa = row[6]
	lon = row[7]
	lat = row[8]
	wikidata = row[9]
	other_language = row[10]
	default_sort = row[11]
	other_name = row[12]
	spanish_name = row[13]
	pl_page = row[14]
	pl_province = row[15]
	db_offset = row[16]
	gov = row[17]

# get again data directly from wikidata
	repo = plwiki.data_repository()
	data = DataPage(repo, wikidata)
	data = data.get()
	print wikidata
# commons
	if commons != None and u'{{' in commons:
		cl_ct = 0
		for claim in data['claims']:
			if claim['m'][1] == 373:
				cl_ct += 1
		if cl_ct == 1:
			for claim in data['claims']:
				if claim['m'][1] == 373:
                        		commons = u'Category:'+claim['m'][3]
		else:
			print 'commons '+ str(cl_ct) + ' '+ wikidata
			break
# image
	if image != None and u'{{' in image:
		cl_ct = 0
		for claim in data['claims']:
			if claim['m'][1] == 18:
				cl_ct += 1
		if cl_ct == 1:
			for claim in data['claims']:
				if claim['m'][1] == 18:
					image = claim['m'][3]
		else:
			print 'image '+ str(cl_ct) + ' '+ wikidata
			break
# flag
	if flag != None and u'{{' in flag:
		cl_ct = 0
		for claim in data['claims']:
			if claim['m'][1] == 41:
				cl_ct += 1
		if cl_ct == 1:
			for claim in data['claims']:
				if claim['m'][1] == 41:
					flag = claim['m'][3]
		else:
			print 'flag '+ str(cl_ct) + ' '+ wikidata
			break
# coa
	if coa != None and u'{{' in coa:
		cl_ct = 0
		for claim in data['claims']:
			if claim['m'][1] == 94:
				cl_ct += 1
		if cl_ct == 1:
			for claim in data['claims']:
				if claim['m'][1] == 94:
					coa = claim['m'][3]
		else:
			print 'coa '+ str(cl_ct) + ' '+ wikidata
			break

# check if page already exists
	pl_page = Page(plwiki, pl_page)
	if not pl_page.exists():
# create template - infobox
		pl_page_text  = u'{{Miejscowość infobox\n'
		pl_page_text += u' |nazwa                        = ' + spanish_name + u'\n'
		pl_page_text += u' |nazwa oryginalna             =\n'
		pl_page_text += u' |zdjęcie                      =' + (u' ' + image + u'\n' if image != None else u'\n')
		pl_page_text += u' |opis zdjęcia                 =\n'
		pl_page_text += u' |herb                         =' + (u' ' + coa + u'\n' if coa != None else u'\n')
		pl_page_text += u' |flaga                        =' + (u' ' + flag + u'\n' if flag != None else u'\n') 
		pl_page_text += u' |dopełniacz nazwy             = ' + spanish_name + u'\n'
		pl_page_text += u' |państwo                      = Hiszpania\n'
		pl_page_text += u' |wariant flagi                =\n'
		pl_page_text += u' |1. jednostka administracyjna = [[' + auto_com[pl_province] + (u'|' + auto_com[pl_province][:auto_com[pl_province].find(u'(')-1] + u']]\n' if u'(' in auto_com[pl_province] else u']]\n')
		pl_page_text += u' |2. jednostka administracyjna = [[' + prov[pl_province] + (u'|' + pl_province + u']]\n' if pl_province != prov[pl_province] else u']]\n')
		pl_page_text += u' |3. jednostka administracyjna =\n'
		pl_page_text += u' |4. jednostka administracyjna =\n'
		pl_page_text += u' |5. jednostka administracyjna =\n'
		pl_page_text += u' |stanowisko zarządzającego    = Alkad\n'
		pl_page_text += u' |zarządzający                 =' + (u' ' + gov if gov != None else u'') + '\n'
		pl_page_text += u' |powierzchnia                 = ' + str(area).replace('.',',') + u'{{r|ssweb}}\n'
		pl_page_text += u' |wysokość                     =\n'
		pl_page_text += u' |rok                          = 2011\n'
		pl_page_text += u' |liczba ludności              = ' + divide(population) + u'{{r|ssweb}}\n'
		pl_page_text += u' |gęstość zaludnienia          = ' + divide(int(round(100*population/area)/100)) + u',' + str(int(round(100*population/area)%100)).zfill(2) + u'\n'
		pl_page_text += u' |numer kierunkowy             =\n'
		pl_page_text += u' |kod pocztowy                 =\n'
		pl_page_text += u' |tablice rejestracyjne        =\n'
		pl_page_text += u' |kod mapy                     = ' + (auto_com[pl_province][:auto_com[pl_province].find(u'(')-1] + u'\n' if u'(' in auto_com[pl_province] else auto_com[pl_province] + '\n')
		pl_page_text += u' |wariant mapy                 =\n'
		pl_page_text += u' |stopniN = ' + str(int(lat)) + u' |minutN = ' + str(int(lat*60)%60) + u' |sekundN = ' + str(int(lat*3600)%60) + u'\n'
		if lon >= 0:
			pl_page_text += u' |stopniE = ' + str(int(lon)) + u' |minutE = ' + str(int(lon*60)%60) + u' |sekundE = ' + str(int(lon*3600)%60) + u'\n'			
		else:
			lon *= -1
			pl_page_text += u' |stopniW = ' + str(int(lon)) + u' |minutW = ' + str(int(lon*60)%60) + u' |sekundW = ' + str(int(lon*3600)%60) + u'\n'
		pl_page_text += u' |opis miejsca                 =\n'
		pl_page_text += u' |commons                      =' + (u' ' + commons  + u'\n' if commons != None else u'\n')
		pl_page_text += u' |wikipodróże                  =\n'
		pl_page_text += u' |www                          =' + (u' ' + www + u'\n}}\n' if www != None else u'\n}}\n')
# body of article
		pl_page_text += u"'''" + spanish_name + u"''' "
		if other_name != None:
			pl_page_text += u'([[język '+ (u'baskijski|baskijski' if other_language == u'b' else u'walencki|walencki') + u"]]: ''" + other_name + "'') " 
		pl_page_text += u'– [[gmina]] w [[Hiszpania|Hiszpanii]], w prowincji [[' + prov[pl_province] + (u'|' + pl_province + u']], ' if pl_province != prov[pl_province] else u']], ')
		print pl_province
		print auto_com[pl_province]
		print auto_com_loc[auto_com[pl_province]]
		if auto_com_loc[auto_com[pl_province]].find(u'wspólnocie') == 0:
			pl_page_text += u'we [[' + auto_com[pl_province] + u'|' + auto_com_loc[auto_com[pl_province]] + u']], '
		else:
			pl_page_text += u'w [[' + auto_com[pl_province] + u'|' + auto_com_loc[auto_com[pl_province]] + u']], '
		pl_page_text += u'o powierzchni ' + str(area).replace('.',',') + u'{{r|ssweb}} km². W 2011 roku gmina liczyła ' + divide(population) + u'{{r|ssweb}} mieszkańców.\n\n'
# references
		pl_page_text += u'== Przypisy ==\n'
		pl_page_text += u'{{Przypisy-lista|\n'
		pl_page_text += u'<ref name=ssweb>{{cytuj stronę | url = http://ssweb.mpt.es/REL/frontend/inicio/municipios/all/all/' + db_offset + u' | tytuł = Datos del registro de Entidades Locales | data dostępu = 2013-06-16 | autor = Ministerio de Hacienda y Administraciones Públicas | język = es}}</ref>\n'
		pl_page_text += u'}}\n\n'
# template and category
		pl_page_text += u'{{Prowincja ' + pl_province + u'}}\n\n'
		pl_page_text += u'{{DEFAULTSORT:' + default_sort + u'}}\n'
		pl_page_text += u'[[Kategoria:Gminy ' + auto_com_gen[auto_com[pl_province]] + u']]\n'		
	
# put page in wikipedia
		print '===================================>', pl_page.title()
# if it's valid with WP:SK
		if sk(text) == text:
			pl_page.put(pl_page_text, u'Bot dodaje artykuł nt. gminy Hiszpanii')
# add interwiki to wikidata
			repo = plwiki.data_repository()
			data = DataPage(repo, wikidata)
			data.setitem(summary=u'adding pl.wiki sitelink', items={'type': u'sitelink', 'site': 'pl', 'title': pl_page.title()})		
# if not valid - print error and break
		else:
			print u'BŁĄD!!!'
			break
# counter
		edit_ct += 1
		if edit_ct == max_edits:
			print u'LICZNIK'
			break

print u'KONIEC'
