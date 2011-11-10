#!/usr/bin/python
# -*- coding: utf-8 -*-

# import podstawowych skryptow z katalogu pywikipedia
import sys
# otwieranie pliku i umieszczanie kolejnych linii w kolejnych alementach listy
f = open('bulgaria.in','r')
listaMiejscowosci = f.readlines()

# tworzenie tabel transliteracji
alfabetBulgarski = [u'А', u'а', u'Б', u'б', u'В', u'в', u'Г', u'г', u'Д', u'д', u'Е', u'е', u'Ж', u'ж', u'З', u'з', u'И', u'и', u'Й', u'й', u'К', u'к', u'Л', u'л', u'М', u'м', u'Н', u'н', u'О', u'о', u'П', u'п', u'Р', u'р', u'С', u'с', u'Т', u'т', u'У', u'у', u'Ф', u'ф', u'Х', u'х', u'Ц', u'ц', u'Ч', u'ч', u'Ш', u'ш', u'Щ', u'щ', u'Ъ', u'ъ', u'Ь', u'ь', u'Ю', u'ю', u'Я', u'я', u' ']
alfabetPolski = [u'A', u'a', u'B', u'b', u'W', u'w', u'G', u'g', u'D', u'd', u'E', u'e', u'Ż', u'ż', u'Z', u'z', u'I', u'i', u'J', u'j', u'K', u'k', u'L', u'l', u'M', u'm', u'N', u'n', u'O', u'o', u'P', u'p', u'R', u'r', u'S', u's', u'T', u't', u'U', u'u', u'F', u'f', u'Ch', u'ch', u'C', u'c', u'Cz', u'cz', u'Sz', u'sz', u'Szt', u'szt', u'Y', u'y', u'J', u'j', u'Ju', u'ju', u'Ja', u'ja', u' ']

# tworzenie listy miejscowosci po polsku i bulgarsku
for miejscowoscBulgarski in listaMiejscowosci:
	miejscowoscBulgarski = miejscowoscBulgarski[:-1]
	miejscowoscBulgarski = unicode(miejscowoscBulgarski, "utf-8")
	miejscowoscPolski = unicode('', "utf-8")
# wymiana wszystkich elementow ciagu
	for foo in range(len(miejscowoscBulgarski)):
		if miejscowoscBulgarski[foo] == u'Л':
			if (foo+1 < len(miejscowoscBulgarski)) and (miejscowoscBulgarski[foo+1] == u'е' or miejscowoscBulgarski[foo+1] == u'и' or miejscowoscBulgarski[foo+1] == u'я' or miejscowoscBulgarski[foo+1] == u'ю'):
				miejscowoscPolski = miejscowoscPolski + u'L'
			else:
				miejscowoscPolski = miejscowoscPolski + u'Ł'
		elif miejscowoscBulgarski[foo] == u'л':
			if (foo+1 < len(miejscowoscBulgarski)) and (miejscowoscBulgarski[foo+1] == u'е' or miejscowoscBulgarski[foo+1] == u'и' or miejscowoscBulgarski[foo+1] == u'я' or miejscowoscBulgarski[foo+1] == u'ю'):
				miejscowoscPolski = miejscowoscPolski + u'l'
			else:
                                miejscowoscPolski = miejscowoscPolski + u'ł'
		elif miejscowoscBulgarski[foo] == u'ъ':
			if foo < len(miejscowoscBulgarski):
				miejscowoscPolski = miejscowoscPolski + u'y'
		else:
			miejscowoscPolski = miejscowoscPolski + alfabetPolski[alfabetBulgarski.index(miejscowoscBulgarski[foo])]
#		print miejscowoscBulgarski[foo]
	print u'* [['+ miejscowoscPolski +u"]] ([[Język bułgarski|bułg.]]: ''" + miejscowoscBulgarski + u"''),"
#	print u'[[Gmina '+miejscowoscPolski+u'|'+miejscowoscPolski+u']] • '
#	print u'[['+miejscowoscPolski+u']] • '

