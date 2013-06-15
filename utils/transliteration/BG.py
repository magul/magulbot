#!/usr/bin/python
# -*- coding: utf-8 -*-

# wymiana wszystkich elementow ciagu
def transliterationBG ( input ):
# tworzenie tabeli transliteracji
	transliterationDict = {u'А':u'A', u'а':u'a', u'Б':u'B', u'б':u'b', u'В':u'W',
	u'в':u'w', u'Г':u'G', u'г':u'g', u'Д':u'D', u'д':u'd', u'Е':u'E',
	u'е':u'e', u'Ж':u'Ż', u'ж':u'ż', u'З':u'Z', u'з':u'z', u'И':u'I',
	u'и':u'i', u'Й':u'J', u'й':u'j', u'К':u'K', u'к':u'k', u'Л':u'L',
	u'л':u'l', u'М':u'M', u'м':u'm', u'Н':u'N', u'н':u'n', u'О':u'O',
	u'о':u'o', u'П':u'P', u'п':u'p', u'Р':u'R', u'р':u'r', u'С':u'S',
	u'с':u's', u'Т':u'T', u'т':u't', u'У':u'U', u'у':u'u', u'Ф':u'F',
	u'ф':u'f', u'Х':u'Ch', u'х':u'ch', u'Ц':u'C', u'ц':u'c', u'Ч':u'Cz',
	u'ч':u'cz', u'Ш':u'Sz', u'ш':u'sz', u'Щ':u'Szt', u'щ':u'szt', u'Ъ':u'Y',
	u'ъ':u'y', u'Ь':u'J', u'ь':u'j', u'Ю':u'Ju', u'ю':u'ju', u'Я':u'Ja',
	u'я':u'ja'}
	output = u''	

# petla po wszystkich elementach lancucha
	for foo in range(len(input)):
# znaki spoza bulgarskiego alfabetu
		if not (input[foo] in transliterationDict):
			output = output + input[foo]
# szczegolne przypadki 
		elif input[foo] == u'Л':
			if (foo+1 < len(input)) and (input[foo+1] == u'е' or input[foo+1] == u'и' or input[foo+1] == u'я' or input[foo+1] == u'ю'):
				output = output + u'L'
			else:
				output = output + u'Ł'
		elif input[foo] == u'л':
			if (foo+1 < len(input)) and (input[foo+1] == u'е' or input[foo+1] == u'и' or input[foo+1] == u'я' or input[foo+1] == u'ю'):
				output = output + u'l'
			else:
                                output = output + u'ł'
		elif input[foo] == u'ъ':
			if foo < len(input):
				output = output + u'y'
# przypadek ogolny
		else:
			output = output + transliterationDict[input[foo]]
# zwrocenie wyniku
	return output
