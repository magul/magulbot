#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# check es_page's infobox if there is head of gov as a separate page
#


# system imports
import sqlite3 as lite

con = lite.connect('municipio.sqlite', isolation_level=None)
cur = con.cursor()
cur.execute(u'SELECT eu_page_text , es_page from municipio where eu_page_text not null and eu_page_text like "%Espainiako udalerri infotaula%"')
data = cur.fetchall()
con.close()

temp_dict = dict()

for i in data:
	item = i[0]
	while item.find(u'{{') != -1:
		item = item[item.find(u'{{')+2:]
		key = item[:(item.find(u'|') if (item.find(u'|') != -1 and item.find(u'|') < item.find(u'}}')) else item.find(u'}}'))]
		item = item[2:]
		key = key.strip()
		if key in temp_dict.keys():
			temp_dict[key] += 1
		else:
			temp_dict[key] = 1


new_dict = dict()
for i in temp_dict:
	if temp_dict[i] in new_dict:
		new_dict[temp_dict[i]][len(new_dict[temp_dict[i]]):] = [i]
	else:
		new_dict[temp_dict[i]] = [i,]

for i in sorted(new_dict):
	print i, '==>', new_dict[i]
