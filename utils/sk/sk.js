/* ------------------------------------------------------------------------ *\
    Moduł sprzątania kodu

	Opis:
		http://pl.wikipedia.org/wiki/WP:SK

    Copyright:  ©2007-2011 Maciej Jaros (pl:User:Nux, en:User:EcceNux)
     Licencja:  GNU General Public License v2
		http://opensource.org/licenses/gpl-license.php

	Szczególne podziękowania dla:
	* Wikipedysta:ABach - za zebranie i opracowanie długiej listy elementów do sprzątania
	* Wikipedysta:Malarz pl - za garść kolejnych elementów do sprzątania
	* Wikipedysta:BartekChom - za pomysły i gotowe wyrażenia regularne
	* Wikipedysta:Gregul - za garść wyrażeń regularnych
	* Wikipedysta:PMG - za wytrwałe i szczegółowe testowanie
	* Wikipedysta:ToSter - za testy i pomysły na nowe rozwiązania
	* Wikipedysta:Beau - za inspiracje i poprawki
\* ------------------------------------------------------------------------ */

/* =====================================================
	Object Init
   ===================================================== */
wp_sk = new Object();

/* =====================================================
	Function: wp_sk.cleanup(input)

	Główna funkcja inicjująca i wywołująca funkcję
	czyszczącą
   ===================================================== */
wp_sk.cleanup = function (str)
{
	
	// OMG - IE & Opera fix
	str = str.replace(/\r\n/g, '\n');

	//
	// Wywołanie czyszciciela
	//
	str = str.replace(/\n+$/,''); // bez końcowych enterów
	str = wp_sk.cleaner(str);
	
	//
	// zapisanie zmian
	//
	return str

}

/* =====================================================
	Function: wp_sk.cleaner(str)

	Funkcja czyszcząca podany na wejściu ciąg znaków str.
	Zwraca przetworzony ciąg znaków.
   ===================================================== */
wp_sk.cleaner = function (str)
{
	//
	// ukrywanie obszarów w tagach: nowiki, pre, source i math
	str = wp_sk.nowiki.hide(str);

	//
	// sprzątanie podstawowe
	str = wp_sk.cleanerLinks(str);		// wikilinki
	str = wp_sk.cleanerTpls(str);		// szablony
	str = wp_sk.cleanerWikiVaria(str);	// pozostałe wikiskładniowe

	str = wp_sk.cleanerTXT(str);		// poza składniowe

	if (wp_sk.projectSpecificCleanup) {
		str = wp_sk.projectSpecificCleanup(str);
	}

	//
	// końcowe porządkowanie międzywiki itp
	str = wp_sk.cleanerMagicLinks(str);

	//
	// przywrócenie ukrytych tagów
	str = wp_sk.nowiki.show(str);

	return str;
}

/* =====================================================
	Function: wp_sk.cleanerLinks(str)

	Sprzątanie wikilinków
   ===================================================== */
wp_sk.cleanerLinks = function (str)
{
	// [[http://]]→[http://...]
	str = str.replace(/\[\[([a-z]+:\/\/[^\|\]]+)\]\]/g, '[$1]');
	// [[Kto%C5%9B_jaki%C5%9B#co.C5.9B|...]]→[[Ktoś jakiś#coś|...]]
	str = str.replace(/\[\[([^|#\]]*)([^|\]]*)(\||\]\])/g, wp_sk.rLinkdecode);

	// poprawa nazw przestrzeni i drobne okoliczne
	str = str.replace(/\[\[(:?) *(image|grafika|file) *: *([^ ])/gi, function (a,dw,co,l1) {return '[['+dw+'Plik:'+l1.toUpperCase();} );
	str = str.replace(/\[\[(:?) *(category|kategoria) *: *([^ ])/gi, function (a,dw,co,l1) {return '[['+dw+'Kategoria:'+l1.toUpperCase();} );
	str = str.replace(/\[\[ *(:?) *(template|szablon) *: *([^ ])/gi, function (a,dw,co,l1) {return '[[Szablon:'+l1.toUpperCase();} );
	str = str.replace(/\[\[ *(:?) *(special|specjalna) *: *([^ ])/gi, function (a,dw,co,l1) {return '[[Specjalna:'+l1.toUpperCase();} );

	str = str.replace(/\[\[ *:? *[Dd]yskusja( [a-z]*) *: */g, '[[Dyskusja$1:');

	// usunięcie klucza sortowania kat. jeśli w całości jest prefiksem nazwy artykułu lub nazwą artykułu
	if (str.search(/\{\{[ ]*DEFAULTSORT[ ]*:/)==-1)
	{
		str = str.replace(/\[\[(Kategoria:[^\|\[\]\n]+)\|([^\|\[\]\n]+)\]\]/gi,
			function (a,kat,klucz)
			{
				if (wgTitle.indexOf(klucz)==0)
					return '[['+kat+']]'
				;
				return a;
			}
		);
	}

	// zbędne w obrazkach
	str = str.replace(/(\[\[Plik:[^\n\|\]]+?\|thumb)\|right/g, '$1');		// niepotrzebne
	str = str.replace(/(\[\[Plik:[^\n\|\]]+?)\|right(\|thumb)/g, '$1$2');		// niepotrzebne
	str = str.replace(/(\[\[Plik:[^\|\]]+?\|)frame(\|[0-9x]+px)/, '$1thumb$2');	// prawie na pewno błąd
	str = str.replace(/(\[\[Plik:[^\|\]]+\|[^\|\]]+)\.\]\]/, '$1]]');	// kropka
	// -mid spacje
	/* // zawiesza FF w niektórych warunkach, psuje niektóre opisy
	str = str.replace(/(\[\[Plik:[^\|\[\]]+)(\|[^\[\]\{\}]+ [^\[\]\{\}]*)(\|([^\|\[\]]+|[^\|\[\]]+\[\[[^\[\]]+\]\]){7,}\]\])/g, function(a,g1,gmid,gn)
	{
		return g1+ gmid.replace(/\s/g,'') +gn;
	});
	*/

	// usuwanie [[:pl:
	str = str.replace(/\[\[ *:? *pl *: */g, '[[');

	// stare przestrzenie
	str = str.replace(/\[\[Dyskusja Wikipedysty/g, '[[Dyskusja wikipedysty');

	// [[link|| -> [[link|
	str = str.replace(/\[\[ *([^\]\|:]+) *\| *\| */g, '[[$1|');

	//
	// (ro)zwijanie wikilinków
	// [[Link|link]] > [[link]] i [[Link|linka]] > [[link]]a
	//str = str.replace(/\[\[([^|\]])([^|\]]*)\|([^\]])\2([a-zA-ZżółćęśąźńŻÓŁĆĘŚĄŹŃ]*)\]\]/g, function (a, w1_1, w_rest, w2_1, poza)
	str = str.replace(/\[\[([^|\]])([^|\]]*)\|([^\]])\2([a-zżółćęśąźń]*)\]\]/g, function (a, w1_1, w_rest, w2_1, poza)
	{
		return (w1_1.toUpperCase()==w2_1.toUpperCase()) ? '[['+w2_1+w_rest+']]'+poza : a;
	});
	// [[Link|link]]er > [[Link|linker]]
	//str = str.replace(/\[\[([^|\]]+)\|([^|\]]+)\]\]([a-zA-ZżółćęśąźńŻÓŁĆĘŚĄŹŃ]+)/g, '[[$1|$2$3]]');
	str = str.replace(/\[\[([^|\]]+)\|([^|\[\]]+)\]\]([a-zżółćęśąźń]+)/g, '[[$1|$2$3]]');

	// usuwanie spacji w wikilinkach
	str = str.replace(/\[\[ *([^\]\|:]*[^\]\| ]) *\|/g, '[[$1|');
	str = str.replace(/([^ \t\n])\[\[ +/g, '$1 [[');
	str = str.replace(/\[\[ +/g, '[[');
	str = str.replace(/([^ \t\n])\[\[([^\]\|:]+)\| +/g, '$1 [[$2|');
	str = str.replace(/\[\[([^\]\|:]+)\| +/g, '[[$1|');
	str = str.replace(/([^ \|]) +\]\]([^ \t\na-zA-ZżółćęśąźńŻÓŁĆĘŚĄŹŃ])/g, '$1]] $2');
	str = str.replace(/([^ \|]) +\]\]([^a-zA-ZżółćęśąźńŻÓŁĆĘŚĄŹŃ])/g, '$1]]$2');

	// sklejanie skrótów linkowych
	str = str.replace(/m\.? ?\[\[n\.? ?p\.? ?m\.?\]\]/g, 'm [[n.p.m.]]');

	// korekty dat - niepotrzebny przecinek
	str = str.replace(/(\[\[[0-9]+ (stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|września|października|listopada|grudnia)\]\]), (\[\[[0-9]{4}\]\])/g, '$1 $3');

	// linkowanie do wieków
	str = str.replace(/\[\[([XVI]{1,5}) [wW]\.?\]\]/g, '[[$1 wiek|$1 w.]]');
	str = str.replace(/\[\[([XVI]{1,5}) [wW]\.?\|/g, '[[$1 wiek|');
	str = str.replace(/\[\[(III|II|IV|VIII|VII|VI|IX|XIII|XII|XI|XIV|XV|XVIII|XVII|XVI|XIX|XXI|XX)\]\]/g, '[[$1 wiek|$1]]');
	str = str.replace(/\[\[(III|II|IV|VIII|VII|VI|IX|XIII|XII|XI|XIV|XV|XVIII|XVII|XVI|XIX|XXI|XX)\|/g, '[[$1 wiek|');

	// rozwijanie typowych linków
	str = str.replace(/\[\[ang\.\]\]/g, '[[język angielski|ang.]]');
	str = str.replace(/\[\[cz\.\]\]/g, '[[język czeski|cz.]]');
	str = str.replace(/\[\[fr\.\]\]/g, '[[język francuski|fr.]]');
	str = str.replace(/\[\[łac\.\]\]/g, '[[łacina|łac.]]');
	str = str.replace(/\[\[niem\.\]\]/g, '[[język niemiecki|niem.]]');
	str = str.replace(/\[\[pol\.\]\]/g, '[[język polski|pol.]]');
	str = str.replace(/\[\[pl\.\]\]/g, '[[język polski|pol.]]');
	str = str.replace(/\[\[ros\.\]\]/g, '[[język rosyjski|ros.]]');
	str = str.replace(/\[\[(((G|g)iga|(M|m)ega|(K|k)ilo)herc|[GMk]Hz)\|/g, '[[herc|');

	return str;
}
/* =====================================================
	Function: wp_sk.cleanerTpls(str)

	Sprzątanie szablonów
   ===================================================== */
wp_sk.cleanerTpls = function (str)
{
	// niepotrzebna przestrzeń
	str = str.replace(/\{\{ *([Tt]emplate|[Ss]zablon|msg) *: */g, '{{');

	// zbędne spacje w szablonach jedno wierszowych
	str = str.replace(/\{\{[ \t]+([^\n\{\} ]+)[ \t]*\}\}/g, '{{$1}}').replace(/\{\{([^\n\{\}]+)[ \t]+\}\}/g, '{{$1}}');

	// poprawki lang i nowy multilang
	str = str.replace(/\{\{[lL]ang\|cz\}\}/g, '{{lang|cs}}');
	str = str.replace(/\{\{[lL]ang\|dk\}\}/g, '{{lang|da}}');
	str = str.replace(/\{\{[lL]ang\|nb\}\}/g, '{{lang|no}}');
	str = str.replace(/(\{\{lang\|[a-z-]+\}\}[\t ]*){2,10}/g, function(a) {
		return '{{lang'+a.replace(/\{\{lang\|([a-z-]+)\}\}\s*/g, '|$1')+'}}';
	});

	// wciąganie {{lang}} do szablonów cytowania
	str = str.replace(/{{(cytuj [^{}]+?)}} {{lang\|([a-z-]+)}}/gi, '{{$1 | język = $2}}');

	// ujednolicanie nazw szablonów (tabela poniżej)
	str = str.replace(/\{\{([sS]\||)([^{}\n\|]+)(\||\}\})/g, function(a, pre, nazwa, post)
	{
		nazwa = nazwa.toLowerCase();
		if (wp_sk.sz_redirs_tab[nazwa])
		{
			a = '{{'+pre + wp_sk.sz_redirs_tab[nazwa] + post
		}
		return a;
	});

	str = str.replace(/\{\{commons\|Category:/gi, '{{commonscat|');

	// poprawka, bo FF wywala się na czołgach np. http://pl.wikipedia.org/w/index.php?title=T-72&diff=14511491&oldid=14437344
	str = str.replace(/<!--[\s\S]+?-->/g, function(a) {
		a
			.replace(/\{/g,'###comment_klamra_l###')
			.replace(/\}/g,'###comment_klamra_r###')
		;
		return a;
	});
	// uczłowieczanie szablonów
	str = str.replace(/\{\{([^|}]+?[ _]infobo[^|}]+)((?:[^{}]|[^{}][{}][^{}]|\{\{(?:[^{}]|[^{}][{}][^{}]|\{\{[^{}]+\}\})+\}\})+)\}\}/g, wp_sk.rFriendlyIbox);
	// rev poprawki
	str = str.replace(/<!--[\s\S]+?-->/g, function(a) {
		a
			.replace(/###comment_klamra_l###/g, '{')
			.replace(/###comment_klamra_r###/g, '}')
		;
		return a;
	});

	return str;
}
/* =====================================================
	Function: wp_sk.cleanerWikiVaria(str)

	Sprzątanie pozostałych elementów wikiskładni
   ===================================================== */
wp_sk.cleanerWikiVaria = function (str)
{
	// unifikacja nagłówkowa
	str = str.replace(/[ \n\t]*\n'''? *(Zobacz|Patrz) (też|także|również):* *'''?[ \t]*\n[ \t\n]*/gi, '\n\n== Zobacz też ==\n');
	str = str.replace(/[ \n\t]*\n'''? *(Zobacz|Patrz) (też|także|również):* *'''?[ \t]*(.+)/gi, function(a, w1, w2, linki)
	{
		if (linki.indexOf('[')!=-1)
		{
			// add first list el.
			linki = '* ' + linki;
			// next?
			if (linki.indexOf(',')!=-1)
			{
				// escape in-link and in-tpl comma
				var escape_fun = function(a){ return a.replace(/,/g,'<<<#>>>') };
				linki = linki.replace(/\[\[[^\[\]]+\]\]/g, escape_fun);
				linki = linki.replace(/\{\{[^\{\}]+\}\}/g, escape_fun);
				// split
				linki = linki.replace(/,[ \t]*/g, '\n* ');
				// unescape
				linki = linki.replace(/<<<#>>>/g,',');
			}
		}
		return '\n\n== Zobacz też ==\n'+linki;
	});
	str = str.replace(/[ \n\t]*\n(=+) *(Zobacz|Patrz) (też|także|również):* *=+[ \n\t]*/gi, '\n\n$1 Zobacz też $1\n');
	str = str.replace(/[ \n\t]*\n'''? *((Zewnętrzn[ey] )?(Linki?|Łącza|Stron[ay]|Zobacz w (internecie|sieci))( zewn[eę]trzn[aey])?):* *'''?[ \n\t]*/gi, '\n\n== Linki zewnętrzne ==\n');
	str = str.replace(/[ \n\t]*\n(=+) *((Zewnętrzn[ey] )?(Linki?|Łącza|Stron[ay]|Zobacz w (internecie|sieci))( zewn[eę]trzn[aey])?):* *=+[ \n\t]*/gi, '\n\n$1 Linki zewnętrzne $1\n');
	str = str.replace(/[ \n\t]*\n(=+) *([ŹŻZ]r[óo]d[łl]a):* *=+[ \n\t]*/gi, '\n\n$1 Źródła $1\n');

	// nagłówki
	str = str.replace(/(^|\n)(=+) *([^=\n].*?)[ :]*\2(?=\s)/g, '$1$2 $3 $2'); // =a= > = a =, =a:= > = a =
	str = str.replace(/(^|\n)(=+[^=\n]+=+)[\n]{2,}/g, '$1$2\n');	// jeden \n

	
	// przypisy - szablon
	str = str.replace(/\n== Przypisy ==[ \t\n]+<references ?\/>/g, '\n{{Przypisy}}');
	str = str.replace(/\n(={3,}) Przypisy \1[ \t\n]+<references ?\/>/g, '\n{{Przypisy|stopień= $1}}');
	str = str.replace(/\{\{Przypisy\|stopień==/g, '{{Przypisy|stopień= =');
	

	// przypisy - przyprzątnięcia
	/*
	// rozwijamy {{r}}, bo kod niżej pracuje na <ref/>-ach
	str = str.replace(/{{r((?:\|[^|}]+)*)}}/g, function(a, inside) {
		return inside.replace(/\|([^|}]+)/g, function(b, name) {
			// escape'ujemy " w nazwach
			return '<ref name="' + name.replace(/"/g, "\\\"") + '" />';
		});
	});
	*/
	
	str = str.replace(/<(ref[^<>\/]*?)[ ]*><\/ref>/g, "<$1 />");	// puste na pojedynczy
	str = str.replace(/[ \t]+(<ref[ >]|\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, '$1');		// bez białych przed
	// nowe linie przed ref w references
	str = str.replace(/(<references>|\{\{Przypisy[\s\S]*?\|\s*przypisy\s*=|\{\{Uwagi[\s\S]*?\|\s*uwagi\s*=|\{\{Przypisy-lista[\s\S]*?\|\s*l\. kolumn\s*=\s*[0-9]+\s*\|\s*1=|\{\{Przypisy-lista[\s\S]*?\|\s*(1\s*=)|\{\{Przypisy-lista[\s\S]*?\|)((?:<ref name[^<>]+>[\s\S]*?<\/ref>\s*)+)/gi,
		function(a, prerefs, temp_refs, refs)
		{
			refs = refs.replace(/<\/ref><ref/gi, '</ref>\n<ref');
			return prerefs + '\n' + refs;
		}
	);
	// przypisy i interpunkcja
	str = str.replace(/([,])((?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$2$1");	// przecinek
	str = str.replace(/((?:\s|^)[^& ]*);((?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$1$2;");	// średnik
	str = str.replace(/([a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]{5}|[()\[\]{}"”'>])[.]((?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$1$2.");	// długi wyraz lub znak specjalny
	str = str.replace(/([a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ][aeiouyąę])[.]([']*(?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$1$2.");	// krótki z samogłoską
	str = str.replace(/(<\/ref>|\{\{[Rr]\|[^}]+\}\})\.\.(?=\s)/g, '$1.');  // dwukropek poziomy
	
	/*
	// zwijamy z powrotem <ref/> do {{r}}
	str = str.replace(/< *ref *name *= *(?:"([^">\n]+)"|'([^'>\n]+)'|([^\s'"\/]+)) *\/ *>/g, function(a, name1, name2, name3) {
		return "{{r|" + (name1||name2||name3) + "}}";
	});
	// łączymy kolejne wywołania postaci {{r}}{{r}}
	// nie działa dla wywołań z parametrami grupaN=
	str = str.replace(/(\{\{r(\|([^|}]+))+\}\}\s*)+/g, function(refs) {
		return refs.replace(/\}\}\s*\{\{r\|/g, '|');
	});
	*/

	// fakty i interpunkcja
	str = str.replace(/([,])(\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$2$1");	// przecinek
	str = str.replace(/((?:\s|^)[^& ]*);(\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$1$2;");	// średnik
	str = str.replace(/([a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]{5}|[()\[\]{}"”'>])[.](\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$1$2.");	// długi wyraz lub znak specjalny
	str = str.replace(/([a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ][aeiouyąę])[.](\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$1$2.");	// krótki z samogłoską

	// listy ze spacjami
	str = str.replace(/(\n[#*:;]+)(?![ \t\n#*:;{]|if[a-z]* ?:|switch ?:|time ?:|rel2abs ?:|titleparts ?:)/g, '$1 ');

	// rozwijanie linków w listach
	str = str.replace(/\n\*[ \t]*\[(http:\/\/[^ \n\]]+)\]/g, "\n* [$1 $1]");

	// galerie fix cooked by ToSter
	str = str.replace(/<gallery([^\n>]*)>([\s\S]+?)<\/gallery>/gi, function(a, opcje, zaw) {
		zaw = zaw.replace(/\n(Image|Grafika|File):/gi, '\nPlik:');
		return "<gallery" + opcje + ">" + zaw + "</gallery>";
	});


	return str;
}
/* =====================================================
	Function: wp_sk.cleanerTXT(str)

	Sprzątanie nie związane bezpośrednio z wikiskładnią
   ===================================================== */
wp_sk.cleanerTXT = function (str)
{
	// usuwanie unikodowych znaków sterujących
	str = str.replace(/[\u200B\uFEFF\u200E]/g, '');

	// korekty dat
	// występuje w interwiki (hr)
	//str = str.replace(/([0-9])\. *(stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|września|października|listopada|grudnia)/g, '$1 $2')	// niepotrzebna kropka
	str = str.replace(/([^0-9])0([0-9]) *(stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|września|października|listopada|grudnia)/g, '$1$2 $3')	// niepotrzebne 0

	// poprawkowate różne (kolejność jest istotna!)
	str = str.replace(/&deg;/g, '°');
	str = str.replace(/&sum;/g, '∑');
	str = str.replace(/&larr;/g, '←');
	str = str.replace(/&rarr;/g, '→');
	str = str.replace(/&uarr;/g, '↑');
	str = str.replace(/&darr;/g, '↓');
	str = str.replace(/&dagger;/g, '†');
	str = str.replace(/<sup>o<\/sup>/g, '°');

	str = str.replace(/([0-9]) (%|‰|°)(?!C)/g, '$1$2'); // bez x °C
	str = str.replace(/([0-9]) (%|‰|°)(?!F)/g, '$1$2'); // bez x °F
	str = str.replace(/([0-9])(°[CF])/g, '$1 $2'); // spacja

	str = str.replace(/<\/?br ?\/?>/gi, '<br />');

	// dopisanie kropki itp
	str = str.replace(/ (tzw|tzn) /g, ' $1. ');
	str = str.replace(/([ \n])ok\.([0-9])/g, '$1ok. $2');
	//str = str.replace(/([ \n])ok ([^ ])/g, '$1ok. $2');
	str = str.replace(/ d\/s /g, ' ds. ');
	str = str.replace(/ wg\. /g, ' wg ');

	// sklejanie skrótów
	str = str.replace(/m\.? ?(npm|n[. ]{1,3}p[. ]{1,3}m\.?)/g, 'm n.p.m.');
	str = str.replace(/ m\. in\./g, ' m.in.');
	str = str.replace(/ o\. o\./g, ' o.o.');

	// Sprawy wagi Państwowej ;-)
	str = str.replace(/(gmina wiejska w powiecie [a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\-]+ województwa [a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\-]+) II Rzeczpospolitej/g, '\1 II Rzeczypospolitej');

	return str;
}

/* =====================================================
	Function: wp_sk.cleanerMagicLinks(str)

	Sprzątanie końcowe magicznych linków i elementów
	powiązanych - międzywiki, medale dla nich i kategorie.
   ===================================================== */
wp_sk.cleanerMagicLinks = function (str)
{
	// zbieranie
	str = wp_sk.cat.gather(str);
	str = wp_sk.iWiki.gather(str);
	str = wp_sk.iWikiFA.gather(str);
	str = wp_sk.iWikiGA.gather(str);
	str = wp_sk.iWikiFL.gather(str);

	// usuwanie pozostawionych przy zbieraniu i innych wielokrotnych, pustych wierszy
	str = str.replace(/[\n]{3,}/g, '\n\n');

	// wstawienie na koniec (call not copy to have "this")
	str = str.replace(/\s*$/, function(a) {return wp_sk.cat.output(a)});
	str = str.replace(/\s*$/, function(a) {return wp_sk.iWikiFA.output(a)});
	str = str.replace(/\s*$/, function(a) {return wp_sk.iWikiGA.output(a)});
	str = str.replace(/\s*$/, function(a) {return wp_sk.iWikiFL.output(a)});
	str = str.replace(/\s*$/, function(a) {return wp_sk.iWiki.output(a)});

	return str;
}

/* =====================================================
	Funkcje wspomagające porządkowanie           {START}
   ----------------------------------------------------- */
//
// Sprzątanie infoboksów
//
wp_sk.rFriendlyIbox = function (a,nazwa,zaw)
{
	if (zaw.indexOf('<!--')!=-1 || zaw.indexOf('=')==-1 || zaw.indexOf('\n')==-1)
	{
		return a;
	}
	nazwa = nazwa.replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");	// trim

	//
	// escapowanie parametrów
	//
	// wewnętrzne szablony
	zaw = zaw.replace(/<<<(#+)>>>/g,'<<<#$1>>>');
	zaw = zaw.replace(/\{\{(([^\{\}]+)?(\{\{[^\{\}]+\}\})?)*\}\}/g,function(a){ return a.replace(/\|/g,'<<<#>>>') });
	// wewnętrzne linki
	zaw = zaw.replace(/\[\[[^\]]+\]\]/g,function(a){ return a.replace(/\|/g,'<<<#>>>') });

	//
	// sprzątanie
	//
	// del pustych
	zaw = zaw.replace(/\|\s*(?=\|)/g, function(a) {return (a.indexOf('\n')==-1)?'':'\n'}).replace(/\|\s*$/g, "");
	zaw = zaw.replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");	// trim
	// przeniesienie | na początek wiersza
	zaw = '\n'+zaw+'\n';
	zaw = zaw.replace(/\s*\|(\s*)/g, function(a, post)
	{
		if (a.indexOf('\n')==-1)
		{
			return a;
		}
		else if (post.indexOf('\n')==-1)
		{
			return '\n |'+post;
		}
		else
		{
			return '\n | ';
		}
	});

	//
	// odescapowanie
	zaw = zaw.replace(/<<<#>>>/g,'|').replace(/<<<#(#+)>>>/g,'<<<$1>>>');

	//
	// Zakończenie
	//
	return '{{'+nazwa.substring(0,1).toUpperCase()+nazwa.substring(1)+zaw+'}}';
}
//
// Dekodowanie linków
//
wp_sk.rLinkdecode = function(a,name,anchor,end)
{
	try
	{
		name=decodeURIComponent(name)
		anchor=decodeURIComponent(anchor.replace(/\.([0-9A-F]{2})/g,'%$1'))
		a='[['+name+anchor+end;
	}
	catch(err){}

	a = a.replace(/802\x11/g, '802.11');
	return a.replace(/_/g,' ');
}
/* -----------------------------------------------------
	Funkcje wspomagające porządkowanie          {KONIEC}
   ===================================================== */

/* =====================================================
	Klasy wspomagające porządkowanie             {START}
   ----------------------------------------------------- */
/* =====================================================
	Class: wp_sk.nowiki

	Ukrywanie obszarów w tagach: nowiki, pre, source i math

	.hide(str)
		ukrywanie tagów specjalnych wraz z ich wnętrzami
	.show(str)
		przywrócenie ukrytych tagów
   ===================================================== */
//
// object init
//
wp_sk.nowiki = new Object();

//
// .hide(str)
//
wp_sk.nowiki.hide = function(str)
{
	//
	// escapowanie przed nowikowe
	str = str.replace(/<<<(#*[0-9]+)>>>/g, '<<<#$1>>>');

	//
	// właściwe ukrywanie
	var re = /<(nowiki|pre|source|math|includeonly|noinclude)(|[ \t\n][^>]*)>/g;
	var m;
	wp_sk.nowiki.tags = new Array();
	// póki znaleziono tag otwierający
	for (var t_i = 0; (m=re.exec(str))!=null; t_i++)
	{
		var start, end, re_end;

		start = m.index;

		// odszukanie końca: </tag([ \t\n]*)>
		re_end = new RegExp("</"+m[1]+"([ \t\n]*)>", "g")
		m = re_end.exec(str.substring(re.lastIndex));
		end = (m==null) ? str.length : re.lastIndex+re_end.lastIndex;

		// dopisanie do tablicy zawartości
		wp_sk.nowiki.tags[t_i] = str.substring(start,end);

		// zamiana całości znalezionego obszaru na: <<<indeks>>>
		str = str.substring(0,start)+"<<<"+t_i+">>>"+str.substring(end);

		// szukanie od startu, bo część znaków już usunięto
		re.lastIndex = start;
	}

	return str;
}
//
// .show(str)
//
wp_sk.nowiki.show = function(str)
{
	// tagi
	str = str.replace(/<<<([0-9]+)>>>/g, function (a, i)
	{
		return wp_sk.nowiki.tags[i];
	});
	// odescapowanie nowikowe
	str = str.replace(/<<<(#*[0-9]+)>>>/g, '<<<#$1>>>');

	return str;
}

/* =====================================================
	Class: wp_sk.cat

	Zbieranie, porządkowanie i wstawianie kategorii

	.gather(str)
		zbieranie kategorii ze str ze zwrotem nowego str
	.output(a)
		porządkuje i zwraca wikitekst z kategoriami;
		parametr a jest nieistotny
	.getDefSort()
		zwraca wyrażenie regularne dla defaultsort
	.newDefSort()
		szukanie nowego (najpopularniejszego) defaultsort

	.art_def_sort
		znaleziony w artykule defaultsort
	.def_sort
		wybrany dla artykułu defsort
	.arr
		tablica z kategoriami ('nazwa|sorotwanie')
	.arr_i
		indeks pomocniczy, a także liczba elementów w arr
   ===================================================== */
// object init
wp_sk.cat = new Object();
//
// .gather(str)
//
wp_sk.cat.gather = function(str)
{
	//
	// zbiórka i kasowanie
	wp_sk.cat.arr = new Array();
	wp_sk.cat.arr_i = 0;
	wp_sk.cat.art_def_sort = '';
	str = str.replace(/\{\{DEFAULTSORT:([^\{\}]+|\{\{[^\{\}]+\}\})\}\}(?:[ \t]+\n)?/g, function(a, ds){wp_sk.cat.art_def_sort=ds; return ''});
	str = str.replace(/(?:\n[ \t]+)?\[\[Kategoria:([^\]\[]+)\]\](?:[ \t]+\n)?/g, function(a, cat){wp_sk.cat.arr[wp_sk.cat.arr_i++]=cat; return ''});
	wp_sk.cat.def_sort = wp_sk.cat.art_def_sort;

	return str;
}
function PolishCollator() {
	// Source: https://pl.wiktionary.org/wiki/MediaWiki:Gadget-sk.js
	var orderArray = ['aä', 'ą', 'ã', 'á', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'oö', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'uü', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż'];
	var orderHash = {};

	// Prepare orderHash
	for ( var i = 0; i < orderArray.length; i++ ) {
		var items = orderArray[i].split( '' );
		for ( var j = 0; j < items.length; j++ ) {
			orderHash[items[j]] = i;
		}
	}

	/**
	 * Compares two strings.
	 */
	this.compare = function( a, b ) {
		var len = Math.min( a.length, b.length );
		a = a.toLocaleLowerCase();
		b = b.toLocaleLowerCase();

		for ( var i = 0; i < len; i++ ) {
			var aValue = orderHash[a.charAt( i )];
			var bValue = orderHash[b.charAt( i )];

			if ( aValue == null || bValue == null ) {
				return a.charAt( i ).localeCompare( b.charAt( i ) );
			} else if ( aValue > bValue ) {
				return 1;
			} else if ( aValue < bValue ) {
				return -1;
			}
		}
		if ( a.length < b.length ) {
			return -1;
		} else if ( a.length > b.length ) {
			return 1;
		} else {
			return 0;
		}
	};

	return this;
}

//
// .output(a)
//
wp_sk.cat.output = function (a)
{
	if (wp_sk.cat.arr_i==0)
	{
		return a;
	}
	var str = mw.config.get( 'wp-sk-categories-head', '\n' );

	//
	// sortowanie (jeśli dostępna odpowiednia funkcja)
	if ( mw.config.get( 'wp-sk-sort-categories', false ) ) {
		var collator = new PolishCollator();
		wp_sk.cat.arr.sort( function( a, b ) {
			return collator.compare( a, b );
		} );
	}

	//
	// ustawienie regexp dla defaultsort (wg starego lub znalezionego)
	var reDefSort = wp_sk.cat.getDefSort();

	//
	// zbędne spacje
	for (var i=0; i<wp_sk.cat.arr_i; i++)
	{
		if (/^.+\| $/.test(wp_sk.cat.arr[i]) == false)
		{
			wp_sk.cat.arr[i] = wp_sk.cat.arr[i].replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");	// trim
		}
	}

	//
	// "wyświetlanie" kategorii
	if (reDefSort!="") // jeśli jest jakiś defaultsort
	{
		str += '\n{{DEFAULTSORT:'+wp_sk.cat.def_sort+'}}';
		for (var i=0; i<wp_sk.cat.arr_i; i++)
		{
			// jeśli nie było defaultsort i puste, to dodajemy domyślne, żeby nie psuć
			if (!wp_sk.cat.art_def_sort.length && wp_sk.cat.arr[i].indexOf('|')==-1)
			{
				str += '\n[[Kategoria:'+wp_sk.cat.arr[i]+'|{{PAGENAME}}]]';
			}
			else
			{
				wp_sk.cat.arr[i] = wp_sk.cat.arr[i].replace(reDefSort,'');	// usuwanie klucza
				str += '\n[[Kategoria:'+wp_sk.cat.arr[i]+']]';
			}
		}
	}
	else
	{
		for (var i=0; i<wp_sk.cat.arr_i; i++)
		{
			str += '\n[[Kategoria:'+wp_sk.cat.arr[i]+']]';
		}
	}

	return str;
}
//
// .getDefSort()
//
wp_sk.cat.getDefSort = function ()
{
	//
	// wybieramy klucz sortowania
	if (wp_sk.cat.art_def_sort.length)
	{
		wp_sk.cat.def_sort = wp_sk.cat.art_def_sort;
	}
	// szukanie nowego jeśli liczba kategorii jest większa od 1
	else if (wp_sk.cat.arr_i>1)
	{
		wp_sk.cat.def_sort = wp_sk.cat.newDefSort();
	}

	var reDefSort="";
	if (wp_sk.cat.def_sort!="")
	{
		// zamiana na regexp (żeby uniknąć częściowych dopasowań)
		reDefSort = wp_sk.cat.def_sort.replace(/([(){}\[\]\\|.*?$^])/g, '\\$1');
		reDefSort = new RegExp('\\|'+reDefSort+'$');
	}

	return reDefSort;
}
//
// .newDefSort()
//
wp_sk.cat.newDefSort = function ()
{
	var def_sort = '';

	//
	// sprawdzenie, czy wybrano jakiś klucz sortowania w kategoriach
	var sort_i;
	for (sort_i=0; sort_i<wp_sk.cat.arr_i && wp_sk.cat.arr[sort_i].indexOf('|')<0; sort_i++);

	//
	// liczenie kategorii z kluczami
	var total_sort_num = 0;	// całkowita liczba kluczy sortowania
	for (var i = sort_i; i<wp_sk.cat.arr_i; i++)	// zaczynamy od już znalezionego
	{
		if (wp_sk.cat.arr[i].indexOf('|')>0)
			total_sort_num++;
	}
	//
	// jeśli mało kluczy (byłoby dużo {{PAGENAME}}), to bez domyślnego klucza
	if (total_sort_num*2<wp_sk.cat.arr_i) //<50%
	{
		return '';
	}

	//
	// jeśli wybrano jakieś sorotwanie, to szukamy nowego klucza (wg popularności)
	if (sort_i!=wp_sk.cat.arr_i)
	{
		//
		//
		var def_sort_num = 0;
		var def_sort_forbiden = ['!', ' ', '*', '+'];
		for (var i = sort_i; i<wp_sk.cat.arr_i; i++)	// zaczynamy od już znalezionego
		{
			var j, tmp_def_sort, tmp_def_sort_re, tmp_def_sort_num;

			// dochodzimy do klucza kandydującego
			for (j = i; j<wp_sk.cat.arr_i && wp_sk.cat.arr[j].indexOf('|')<0; j++);
			if (j==wp_sk.cat.arr_i)
				break;
			i = j;

			// klucz
			tmp_def_sort = wp_sk.cat.arr[j].substr(wp_sk.cat.arr[j].indexOf('|')+1);
			if (def_sort == tmp_def_sort)	// już był
			{
				continue;
			}
			// zamiana na regexp (żeby uniknąć częściowych dopasowań)
			tmp_def_sort_re = tmp_def_sort.replace(/([(){}\[\]\\|.*?$^])/g, '\\$1');	// escapowanie znaków regexpowych
			tmp_def_sort_re = new RegExp('\\|'+tmp_def_sort_re+'$');

			// liczenie wystąpień
			var tmp_def_sort_num=1;
			for (j++; j<wp_sk.cat.arr_i; j++)
			{
				if (tmp_def_sort_re.test(wp_sk.cat.arr[j]))
				{
					tmp_def_sort_num++;
				}
			}

			// kandydyjący = nowy?
			if (tmp_def_sort_num<2 || def_sort_num > tmp_def_sort_num)
			{
				continue;
			}
			if (tmp_def_sort_num*2>wp_sk.cat.arr_i || def_sort_forbiden.indexOf(tmp_def_sort)<0) //>50% || nie niedozwolone
			{
				def_sort_num = tmp_def_sort_num;
				def_sort = tmp_def_sort;
			}
		}
	}

	return def_sort;
}

/* =====================================================
	Class: wp_sk.iWiki

	Zbieranie, porządkowanie i wstawianie interwiki

	.gather(str)
		zbieranie interwiki ze str ze zwrotem nowego str
	.output(a)
		porządkuje i zwraca wikitekst z interwiki;
		parametr a jest nieistotny
	.comp(a, b)
		porównuje a z b i zwraca wartość odpowiednią
		dla funkcji sort()

	.order
		tablica z językami ustawionymi wg kolejności
		wg której mają być sortowane interwiki
	.arr
		tablica z interwiki ([język, artykuł])
	.arr_i
		indeks pomocniczy, a także liczba elementów w arr
   ===================================================== */
// object init
wp_sk.iWiki = new Object();
//
// .gather(str)
//
wp_sk.iWiki.gather = function(str)
{
	wp_sk.iWiki.arr = new Array();
	wp_sk.iWiki.arr_i = 0;
	str = str.replace(
		// wg: http://meta.wikimedia.org/wiki/List_of_Wikipedias
		/\[\[\s*([a-z\-]+)\s*:([^\]\|\[]+)\]\](?:[ \t]+\n)?/gi,
		function (a, lang, art)
		{
			lang = lang.toLowerCase(); // [[DE:blah]]
			// wg: http://svn.wikimedia.org/svnroot/mediawiki/trunk/phase3/maintenance/interwiki.sql
			if (wp_sk.iWiki.order.indexOf(lang) >= 0) // czy na pewno interwiki
			{
				wp_sk.iWiki.arr[wp_sk.iWiki.arr_i] = new Array(lang,art);
				wp_sk.iWiki.arr_i++;
				return '';
			}
			else
			{
				return a;
			}
		}
	);

	return str;
}
//
// .output(a)
//
wp_sk.iWiki.output = function (a)
{
	if (wp_sk.iWiki.arr_i==0)
	{
		return a;
	}
	var str = '\n';

	wp_sk.iWiki.arr.sort(wp_sk.iWiki.comp); // alfabetycznie wg kodu literowego
	for (var i=0; i<wp_sk.iWiki.arr_i; i++)
	{
		str += '\n[['+wp_sk.iWiki.arr[i][0]+':'+wp_sk.iWiki.arr[i][1]+']]';
	}

	return str;
}
//
// .comp(a,b)
//
wp_sk.iWiki.comp = function (a, b)
{
	if (wp_sk.iWiki.order.indexOf(a[0]) < wp_sk.iWiki.order.indexOf(b[0]))
	{
		return -1;
	}
	else if (wp_sk.iWiki.order.indexOf(a[0]) > wp_sk.iWiki.order.indexOf(b[0]))
	{
		return 1;
	}
	// else
	return 0;
}
// wg <del>http://meta.wikimedia.org/wiki/Interwiki_sorting_order#By_order_of_alphabet.2C_based_on_local_language</del>
// Pomoc:Interwiki
wp_sk.iWiki.order = [
            'ace', 'kbd', 'af', 'ak', 'als', 'am', 'ang', 'ab', 'ar', 'an',
            'arc', 'roa-rup', 'frp', 'as', 'ast', 'gn', 'av', 'ay', 'az', 'bm',
            'bn', 'bjn', 'zh-min-nan', 'nan', 'map-bms', 'ba', 'be', 'be-x-old',
            'bh', 'bcl', 'bi', 'bg', 'bar', 'bo', 'bs', 'br', 'bxr', 'ca', 'cv',
            'ceb', 'cs', 'ch', 'cbk-zam', 'ny', 'sn', 'tum', 'cho', 'co', 'cy',
            'da', 'dk', 'pdc', 'de', 'dv', 'nv', 'dsb', 'dz', 'mh', 'et', 'el',
            'eml', 'en', 'myv', 'es', 'eo', 'ext', 'eu', 'ee', 'fa', 'hif',
            'fo', 'fr', 'fy', 'ff', 'fur', 'ga', 'gv', 'gag', 'gd', 'gl', 'gan',
            'ki', 'glk', 'gu', 'got', 'hak', 'xal', 'ko', 'ha', 'haw', 'hy',
            'hi', 'ho', 'hsb', 'hr', 'io', 'ig', 'ilo', 'bpy', 'id', 'ia', 'ie',
            'iu', 'ik', 'os', 'xh', 'zu', 'is', 'it', 'he', 'jv', 'kl', 'kn',
            'kr', 'pam', 'krc', 'ka', 'ks', 'csb', 'kk', 'kw', 'rw', 'rn', 'sw',
            'kv', 'kg', 'ht', 'ku', 'kj', 'ky', 'mrj', 'lad', 'lbe', 'lo', 'ltg',
            'la', 'lv', 'lb', 'lez', 'lt', 'lij', 'li', 'ln', 'jbo', 'lg', 'lmo', 'hu',
            'mk', 'mg', 'ml', 'mt', 'mi', 'mr', 'xmf', 'arz', 'mzn', 'ms', 'cdo',
            'mwl', 'mdf', 'mo', 'mn', 'mus', 'my', 'nah', 'na', 'fj', 'nl',
            'nds-nl', 'cr', 'ne', 'new', 'ja', 'nap', 'ce', 'frr', 'pih', 'no',
            'nb', 'nn', 'nrm', 'nov', 'ii', 'oc', 'mhr', 'or', 'om', 'ng', 'hz',
            'uz', 'pa', 'pi', 'pfl', 'pag', 'pnb', 'pap', 'ps', 'koi', 'km',
            'pcd', 'pms', 'tpi', 'nds', 'pl', 'tokipona', 'tp', 'pnt', 'pt',
            'aa', 'kaa', 'crh', 'ty', 'ksh', 'ro', 'rmy', 'rm', 'qu', 'rue',
            'ru', 'sah', 'se', 'sm', 'sa', 'sg', 'sc', 'sco', 'stq', 'st', 'nso',
            'tn', 'sq', 'scn', 'si', 'simple', 'sd', 'ss', 'sk', 'sl', 'cu',
            'szl', 'so', 'ckb', 'srn', 'sr', 'sh', 'su', 'fi', 'sv', 'tl', 'ta',
            'kab', 'roa-tara', 'shi', 'tt', 'te', 'tet', 'th', 'ti', 'tg', 'to', 'chr',
            'chy', 've', 'tr', 'tk', 'tw', 'udm', 'bug', 'uk', 'ur', 'ug', 'za',
            'vec', 'vep', 'vi', 'vo', 'fiu-vro', 'wa', 'zh-classical', 'vls', 'war',
            'wo', 'wuu', 'ts', 'yi', 'yo', 'zh-yue', 'diq', 'zea', 'bat-smg',
            'zh', 'zh-tw', 'zh-cn',
]

/* =====================================================
	Class: wp_sk.iWikiFA | iWikiGA | iWikiFL

	Zbieranie, porządkowanie i wstawianie interwikowych
	szablonów Featured Articles

	.gather(str)
		zbieranie szablonów FA ze str ze zwrotem nowego str
	.output(a)
		porządkuje i zwraca wikitekst z szablonami FA;
		parametr a jest nieistotny

	.arr
		tablica z szablonami FA ([język, artykuł])
	.arr_i
		indeks pomocniczy, a także liczba elementów w arr
   ===================================================== */
// object init
wp_sk.iWikiFA = {
	're': /\{\{[Ll]ink FA\|([a-z\-]{2,3}|simple|ru-sib|be-x-old|zh-yue|map-bms|zh-min-nan|nds-nl|bat-smg|zh-classical|fiu-vro|roa-rup|tokipona|cbk-zam|roa-tara)\}\}(?:[ \t]+\n)?/g,
	'out_szablon' : 'Link FA'
}
//
// .gather(str)
//
wp_sk.iWikiFA.gather = function(str)
{
	var arr = new Array();
	var arr_i = 0;
	// wg: http://meta.wikimedia.org/wiki/List_of_Wikipedias
	str = str.replace(
		this.re,
		function (a, lang)
		{
			// wg: http://svn.wikimedia.org/svnroot/mediawiki/trunk/phase3/maintenance/interwiki.sql
			if (wp_sk.iWiki.order.indexOf(lang) >= 0) // czy na pewno interwiki
			{
				arr[arr_i] = lang;
				arr_i++;
				return '';
			}
			else
			{
				return a;
			}
		}
	);
	this.arr = arr;
	this.arr_i = arr_i;

	return str;
}
//
// .output(a)
//
wp_sk.iWikiFA.output = function (a)
{
	if (this.arr_i==0)
	{
		return a;
	}
	var str = '\n';

	this.arr.sort(wp_sk.iWiki.comp); // alfabetycznie wg kodu literowego // funkcja wspólna wp_sk.iWiki
	for (var i=0; i<this.arr_i; i++)
	{
		str += '\n{{'+this.out_szablon+'|'+this.arr[i]+'}}';
	}

	return str;
}

//
// iWikiGA
//
// object init
wp_sk.iWikiGA = {
	're': /\{\{[Ll]ink GA\|([a-z\-]{2,3}|simple|ru-sib|be-x-old|zh-yue|map-bms|zh-min-nan|nds-nl|bat-smg|zh-classical|fiu-vro|roa-rup|tokipona|cbk-zam|roa-tara)\}\}(?:[ \t]+\n)?/g,
	'out_szablon' : 'Link GA'
}
// rest as above
wp_sk.iWikiGA.gather = wp_sk.iWikiFA.gather;
wp_sk.iWikiGA.output = wp_sk.iWikiFA.output;

//
// iWikiFL
//
// object init
wp_sk.iWikiFL = {
	're': /\{\{[Ll]ink FL\|([a-z\-]{2,3}|simple|ru-sib|be-x-old|zh-yue|map-bms|zh-min-nan|nds-nl|bat-smg|zh-classical|fiu-vro|roa-rup|tokipona|cbk-zam|roa-tara)\}\}(?:[ \t]+\n)?/g,
	'out_szablon' : 'Link FL'
}
// rest as above
wp_sk.iWikiFL.gather = wp_sk.iWikiFA.gather;
wp_sk.iWikiFL.output = wp_sk.iWikiFA.output;


/* -----------------------------------------------------
	Klasy wspomagające porządkowanie            {KONIEC}
   ===================================================== */

/* =====================================================
	Function: Array.prototype.indexOf(elt)

	Dostępna normalnie: Gecko>1.8b2
   ===================================================== */
if (!Array.prototype.indexOf)
{
	Array.prototype.indexOf = function(elt /*, from*/)
	{
		var len = this.length;

		var from = Number(arguments[1]) || 0;
		from = (from < 0) ? Math.ceil(from) : Math.floor(from);
		if (from < 0)
			from += len;

		for (; from < len; from++)
		{
			if (from in this && this[from] === elt)
				return from;
		}
		return -1;
	};
}

/* =====================================================
	ujednolicanie szablonów wg:
	http://pl.wikipedia.org/wiki/Wikiprojekt:Sprz%C4%85tanie_szablon%C3%B3w/redirecty#linkowane
   ===================================================== */
/*
! bez  'nobots' : 'Bots',
	re_obj.s = new Array(/(?:^|\n)#[ {]+noredirect\|Szablon:([^}]+)[^\[]+[\[]+Szablon:([^\]]+).+/g, /\n#.+/g);
	re_obj.r = new Array(function(a,from,to) {if (from=='Nobots') {return '';} else return "\n\t'"+from.toLowerCase().replace('\\','\\\\').replace("'","\\'")+"' : '"+to.replace('\\','\\\\').replace("'","\\'")+"',";}, '');
*/ // 2011-08-11
wp_sk.sz_redirs_tab = {
	'!w' : '!wrap',
	'+-' : '±',
	'-' : 'Clear',
	'@' : 'E-mail',
	'aktorka erotyczna infobox' : 'Aktor erotyczny infobox',
	'animanga infobox/footer' : 'Animanga infobox/Stopka',
	'animanga infobox/header' : 'Animanga infobox/Nagłówek',
	'animanga infobox/header2' : 'Animanga infobox/Nagłówek2',
	'bez zmian' : 'Stagnacja',
	'bezpodpisu' : 'Podpisuj',
	'braklicencji' : 'Brak licencji',
	'brakopisu' : 'Brak licencji',
	'bull' : '•',
	'bullet' : '•',
	'chem/disp0aa' : 'Chem/disp0A0',
	'coord' : 'Koordynaty',
	'cytuj czasopismo' : 'Cytuj pismo',
	'dwinfoautora' : 'DWQ',
	'dead link' : 'Martwy link',
	'disambigp' : 'Przekierowanie',
	'dopracowania' : 'Dopracować',
	'done' : 'Zrobione',
	'dot' : '·',
	'dp' : 'Dodaj pozwolenie',
	'dyskusjapodpis' : 'Podpisuj',
	'ek' : 'ek',
	'edit' : 'Edytuj',
	'ekspresowe kasowanko' : 'Ek',
	'fakt/d' : 'Fd',
	'fb r2 header' : 'Fb r header',
	'formuła 1/oznaczenia' : 'Sporty motorowe/Oznaczenia',
	'fs end' : 'Skład piłkarski koniec',
	'fs mid' : 'Skład piłkarski środek',
	'fs player' : 'Skład piłkarski',
	'fs start' : 'Skład piłkarski start',
	'glowny' : 'Główny artykuł',
	'gmedal' : 'Ilustracja medalowa',
	'icd-10' : 'ICD10',
	'icd-9' : 'ICD9',
	'icd-o' : 'ICDO',
	'legend' : 'Legenda',
	'mapa lokalizacyjna/sco' : 'Mapa lokalizacyjna/SCT',
	'mapa lokalizacyjna/usa-hi' : 'Mapa lokalizacyjna/US-HI',
	'mapa lokalizacyjna/wyspy kanaryjskie' : 'Mapa lokalizacyjna/ES-CN',
	'mapa lokalizacyjna/świat polityczna' : 'Mapa lokalizacyjna/Świat',
	'mediavideo' : 'Wideo',
	'middot' : '·',
	'mistrzowie olimpijscy w piłce nożnej' : 'Mistrzowie olimpijscy w piłce nożnej mężczyzn',
	'multilang' : 'Lang',
	'nor' : 'Twórczość własna',
	'nieaktualne' : 'Aktualizacja',
	'nogmedal' : 'Ilustracji odebrano medal',
	'nowa linia' : 'clear',
	'odp' : 'Open Directory Project',
	'og' : 'Dodaj licencję',
	'or' : 'Twórczość własna',
	'osw' : 'Ostatnie stabilne wydanie',
	'otw' : 'Ostatnie testowe wydanie',
	'opisujgrafiki' : 'Dodaj licencję',
	'poczsdu' : 'DNU',
	'poczsduinfo' : 'DNUinfo',
	'poczsduplus' : 'poczSdUplus',
	'poczsdu' : 'DNU',
	'poczekalnia' : 'DNU',
	'poprawić' : 'Dopracować',
	'projektpoczsdu' : 'DNUinfo',
	'rpr' : 'Reprezentant piłki ręcznej',
	'sduinfo' : 'SDUinformacja',
	'sduplus' : 'SdUplus',
	'seealso' : 'Zobacz też',
	'symbol' : 'PD-symbol',
	'testad' : 'Spam',
	'testki' : 'TestK',
	'testn' : 'Test3',
	'testnie' : 'TestG',
	'testp' : 'Test3',
	'testpov' : 'TestPOV0',
	'testspam' : 'Spam',
	'testw' : 'Test2',
	'testlink0' : 'Testlink',
	'testż' : 'TestG',
	'topopraw' : 'To popraw',
	'unk' : 'Unknown',
	'urlop' : 'Odpoczynek',
	'usuń' : 'Ek',
	'w' : 'wrap',
	'wedycji' : 'W edycji',
	'wedycji2' : 'W edycji 2',
	'wiadomości' : 'Aktualności',
	'wikiquote' : 'Wikicytaty',
	'wikisource' : 'Wikiźródła',
	'wikisource-cat' : 'Wikiźródła kat',
	'wikisource-krotki' : 'Wikiźródła krótki',
	'wikisource autor' : 'Wikiźródła autor',
	'witaj-en' : 'Welcome',
	'witaj-fr' : 'Bienvenue',
	'witajip' : 'Anonim',
	'zasada w jednym zdaniu' : 'W skrócie',
	'zdjęcie tyg' : 'Ilustracja na medal',
	'zzw' : 'Zgodnie z Wikietykietą',
	'\\w' : '\\wrap',
	'·w' : '·wrap',
	'święta infobox' : 'Święty infobox',
	'–w' : '–wrap',
	'•w' : '•wrap'
};
