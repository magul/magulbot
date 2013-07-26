#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# resolve problem of duplication of head of gov of municipalities
# pywikibot-core
#

import pwb
from pywikibot import *

s = Site('wikidata', 'wikidata')
r = s.data_repository()
p = Page(s, u'Wikidata:Requests for permissions/Bot/MagulBot 4').get()

links = []
p = p[p.find(u"Q11916413"):]
while p.find(u'[[') != -1:
	p = p[p.find(u'[[')+2:]
	links.append(p[:p.find(u']]')])
links = links[:-2]

i = 0
while i != len(links):
	origin = ItemPage(r, links[i+1])
	duplicate = ItemPage(r, links[i])
	origin.get()
	duplicate.get()
	news = {}
	olds = {}
	for label in duplicate.labels:
		if not label in origin.labels:
			news[label]=duplicate.labels[label]
	if len(news) > 0:
		origin.editLabels(news)
	news = {}
	olds = {}
	for aka in duplicate.aliases:
		if not aka in origin.aliases:
			news[aka]=duplicate.aliases[aka]
	if len(news) > 0:
		origin.editAliases(news)
#	print duplicate.sitelinks
	mun_wd = None
	for j in duplicate.backlinks():
		if j.title()[0] == 'Q':
			mun_wd = ItemPage(r, j.title())
	mun_wd.get()
	print mun_wd.title()
	mun_wd.removeClaims(mun_wd.claims['p6'])

	mun_wd.addClaim(Claim(r, 'p6', ).setTarget(origin))

#	sitelinks = dict(origin.sitelinks.items() + duplicate.sitelinks.items())
	i += 2
