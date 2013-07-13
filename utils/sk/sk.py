#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# usign pyexecjs to check pages using WP:SK
#

# system import
import execjs
from wikipedia import *

js_date =  '2013-04-29T13:25:43Z'
js_local_date = '2012-04-15T17:17:21Z'

# check function
def sk(text):
# check if most actual version
	plwiki = getSite('pl', 'wikipedia')
	if Page(plwiki, 'MediaWiki:Gadget-sk.js').getVersionHistory()[0][1] != js_date:
		print 'MediaWiki:Gadget-sk.js IS OUT OF DATE'
	if Page(plwiki, 'MediaWiki:Gadget-sk-local.js').getVersionHistory()[0][1] != js_local_date:
		print 'MediaWiki:Gadget-sk-local.js IS OUT OF DATE'
# read js code...
	f = open('sk.js', 'r')
	js_code = f.read().decode('utf-8')
	f.close()
# ... and compile it
	js_exec = execjs.compile(js_code)
# actual check
	return js_exec.call("wp_sk.cleaner", text)

