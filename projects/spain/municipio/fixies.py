#!/usr/bin/python
# -*- coding: utf-8 -*-

provinces = [u'A Coruña', u'Araba', u'Albacete', u'Alicante', u'Almería', u'Asturia',
             u'Ávila', u'Badajoz', u'Baleary', u'Barcelona', u'Burgos', u'Cáceres',
             u'Castellón', u'Ciudad Real', u'Cuenca', u'Girona', u'Grenada', u'Guadalajara',
             u'Guipúzcoa', u'Huelva', u'Huesca', u'Jaén', u'Kadyks', u'Kantabria', u'Kordoba',
             u'La Rioja', u'León', u'Lleida', u'Lugo', u'Madryt', u'Malaga', u'Murcja',
             u'Nawarra', u'Ourense', u'Palencia', u'Las Palmas', u'Pontevedra', u'Salamanka',
             u'Santa Cruz de Tenerife', u'Saragossa', u'Segowia', u'Sewilla', u'Soria',
             u'Tarragona', u'Teruel', u'Toledo', u'Valladolid', u'Vizcaya', u'Walencja',
             u'Zamora']


csv_provinces = [u'Coruña, A', u'Araba/Álava', u'Albacete', u'Alacant/Alicante', u'Almería',
                 u'Asturias', u'Ávila', u'Badajoz', u'Illes Balears', u'Barcelona', u'Burgos',
                 u'Cáceres', u'Castelló/Castellón', u'Ciudad Real', u'Cuenca', u'Girona',
                 u'Granada', u'Guadalajara', u'Gipuzkoa', u'Huelva', u'Huesca', u'Jaén', u'Cádiz',
                 u'Cantabria', u'Córdoba', u'Rioja, La', u'León', u'Lleida', u'Lugo', u'Madrid',
                 u'Málaga', u'Murcia', u'Navarra', u'Ourense', u'Palencia', u'Palmas, Las',
                 u'Pontevedra', u'Salamanca', u'Santa Cruz de Tenerife', u'Zaragoza', u'Segovia',
                 u'Sevilla', u'Soria', u'Tarragona', u'Teruel', u'Toledo', u'Valladolid',
                 u'Bizkaia', u'València/Valencia', u'Zamora']


osm_provinces = [u'A Coruña', u'Álava', u'Albacete', u'Alicante', u'Almería',
                 u'Asturias', u'Ávila', u'Badajoz', u'Illes Balears', u'Barcelona', u'Burgos',
                 u'Cáceres', u'Castellón', u'Ciudad Real', u'Cuenca', u'Girona',
                 u'Granada', u'Guadalajara', u'Gipuzkoa', u'Huelva', u'Huesca', u'Jaén', u'Cádiz',
                 u'Cantabria', u'Córdoba', u'La Rioja', u'León', u'Lleida', u'Lugo', u'Madrid',
                 u'Málaga', u'Murcia', u'Navarra', u'Ourense', u'Palencia', u'Las Palmas',
                 u'Pontevedra', u'Salamanca', u'Santa Cruz de Tenerife', u'Zaragoza', u'Segovia',
                 u'Sevilla', u'Soria', u'Tarragona', u'Teruel', u'Toledo', u'Valladolid',
                 u'Bizkaia', u'Valencia', u'Zamora']

auto_com_gen = {u'Andaluzja' : u'Andaluzji', u'Aragonia' : u'Aragonii', u'Asturia' : u'Asturii',
                u'Baleary' : u'Balearów', u'Estremadura (Hiszpania)' : u'Estramadury',
                u'Galicja (Hiszpania)' : u'Galicji', u'Kantabria' : u'Kantabrii', 
                u'Kastylia i León' : u'Kastylii i León', u'Kastylia-La Mancha' : u'Kastylii-La Mancha',
                u'Katalonia' : u'Katalonii', u'La Rioja (wspólnota autonomiczna)' : u'La Rioja',
                u'Kraj Basków' : u'Kraju Basków', u'Madryt (wspólnota autonomiczna)' : 'Madrytu',
                u'Murcja (wspólnota autonomiczna)' : u'Murcji', u'Nawarra (prowincja)' : u'Nawarry',
                u'Walencja (wspólnota autonomiczna)' : 'Walencji', u'Wyspy Kanaryjskie' : u'Wysp Kanaryjskich'}
