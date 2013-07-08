/* =====================================================
	ujednolicanie szablon�w wg:
	http://pl.wikipedia.org/wiki/Wikiprojekt:Sprz%C4%85tanie_szablon%C3%B3w/redirecty#linkowane
   ===================================================== */
/*
! bez  'nobots' : 'Bots',
	re_obj.s = new Array(/(?:^|\n)#[ {]+noredirect\|Szablon:([^}]+)[^\[]+[\[]+Szablon:([^\]]+).+/g, /\n#.+/g);
	re_obj.r = new Array(function(a,from,to) {if (from=='Nobots') {return '';} else return "\n\t'"+from.toLowerCase().replace('\\','\\\\').replace("'","\\'")+"' : '"+to.replace('\\','\\\\').replace("'","\\'")+"',";}, '');
*/ // 2011-08-11
wp_sk.sz_redirs_tab = {
	'!w' : '!wrap',
	'+-' : '.',
	'-' : 'Clear',
	'@' : 'E-mail',
	'aktorka erotyczna infobox' : 'Aktor erotyczny infobox',
	'animanga infobox/footer' : 'Animanga infobox/Stopka',
	'animanga infobox/header' : 'Animanga infobox/Nag��wek',
	'animanga infobox/header2' : 'Animanga infobox/Nag��wek2',
	'bez zmian' : 'Stagnacja',
	'bezpodpisu' : 'Podpisuj',
	'braklicencji' : 'Brak licencji',
	'brakopisu' : 'Brak licencji',
	'bull' : '.',
	'bullet' : '.',
	'chem/disp0aa' : 'Chem/disp0A0',
	'coord' : 'Koordynaty',
	'cytuj czasopismo' : 'Cytuj pismo',
	'dwinfoautora' : 'DWQ',
	'dead link' : 'Martwy link',
	'disambigp' : 'Przekierowanie',
	'dopracowania' : 'Dopracowa�',
	'done' : 'Zrobione',
	'dot' : '.',
	'dp' : 'Dodaj pozwolenie',
	'dyskusjapodpis' : 'Podpisuj',
	'ek' : 'ek',
	'edit' : 'Edytuj',
	'ekspresowe kasowanko' : 'Ek',
	'fakt/d' : 'Fd',
	'fb r2 header' : 'Fb r header',
	'formu�a 1/oznaczenia' : 'Sporty motorowe/Oznaczenia',
	'fs end' : 'Sk�ad pi�karski koniec',
	'fs mid' : 'Sk�ad pi�karski �rodek',
	'fs player' : 'Sk�ad pi�karski',
	'fs start' : 'Sk�ad pi�karski start',
	'glowny' : 'G��wny artyku�',
	'gmedal' : 'Ilustracja medalowa',
	'icd-10' : 'ICD10',
	'icd-9' : 'ICD9',
	'icd-o' : 'ICDO',
	'legend' : 'Legenda',
	'mapa lokalizacyjna/sco' : 'Mapa lokalizacyjna/SCT',
	'mapa lokalizacyjna/usa-hi' : 'Mapa lokalizacyjna/US-HI',
	'mapa lokalizacyjna/wyspy kanaryjskie' : 'Mapa lokalizacyjna/ES-CN',
	'mapa lokalizacyjna/�wiat polityczna' : 'Mapa lokalizacyjna/�wiat',
	'mediavideo' : 'Wideo',
	'middot' : '.',
	'mistrzowie olimpijscy w pi�ce no�nej' : 'Mistrzowie olimpijscy w pi�ce no�nej m�czyzn',
	'multilang' : 'Lang',
	'nor' : 'Tw�rczo�� w�asna',
	'nieaktualne' : 'Aktualizacja',
	'nogmedal' : 'Ilustracji odebrano medal',
	'nowa linia' : 'clear',
	'odp' : 'Open Directory Project',
	'og' : 'Dodaj licencj�',
	'or' : 'Tw�rczo�� w�asna',
	'osw' : 'Ostatnie stabilne wydanie',
	'otw' : 'Ostatnie testowe wydanie',
	'opisujgrafiki' : 'Dodaj licencj�',
	'poczsdu' : 'DNU',
	'poczsduinfo' : 'DNUinfo',
	'poczsduplus' : 'poczSdUplus',
	'poczsdu' : 'DNU',
	'poczekalnia' : 'DNU',
	'poprawi�' : 'Dopracowa�',
	'projektpoczsdu' : 'DNUinfo',
	'rpr' : 'Reprezentant pi�ki r�cznej',
	'sduinfo' : 'SDUinformacja',
	'sduplus' : 'SdUplus',
	'seealso' : 'Zobacz te�',
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
	'test�' : 'TestG',
	'topopraw' : 'To popraw',
	'unk' : 'Unknown',
	'urlop' : 'Odpoczynek',
	'usu�' : 'Ek',
	'w' : 'wrap',
	'wedycji' : 'W edycji',
	'wedycji2' : 'W edycji 2',
	'wiadomo�ci' : 'Aktualno�ci',
	'wikiquote' : 'Wikicytaty',
	'wikisource' : 'Wiki�r�d�a',
	'wikisource-cat' : 'Wiki�r�d�a kat',
	'wikisource-krotki' : 'Wiki�r�d�a kr�tki',
	'wikisource autor' : 'Wiki�r�d�a autor',
	'witaj-en' : 'Welcome',
	'witaj-fr' : 'Bienvenue',
	'witajip' : 'Anonim',
	'zasada w jednym zdaniu' : 'W skr�cie',
	'zdj�cie tyg' : 'Ilustracja na medal',
	'zzw' : 'Zgodnie z Wikietykiet�',
	'\\w' : '\\wrap',
	'.w' : '.wrap',
	'�wi�ta infobox' : '�wi�ty infobox',
	'.w' : '.wrap',
	'.w' : '.wrap'
};

// <nowiki>
/* ------------------------------------------------------------------------ *\
    Modu� sprz�tania kodu

	Opis:
		http://pl.wikipedia.org/wiki/WP:SK

    Copyright:  .2007-2011 Maciej Jaros (pl:User:Nux, en:User:EcceNux)
     Licencja:  GNU General Public License v2
		http://opensource.org/licenses/gpl-license.php

	Szczeg�lne podzi�kowania dla:
	* Wikipedysta:ABach - za zebranie i opracowanie d�ugiej listy element�w do sprz�tania
	* Wikipedysta:Malarz pl - za gar�� kolejnych element�w do sprz�tania
	* Wikipedysta:BartekChom - za pomys�y i gotowe wyra�enia regularne
	* Wikipedysta:Gregul - za gar�� wyra�e� regularnych
	* Wikipedysta:PMG - za wytrwa�e i szczeg�owe testowanie
	* Wikipedysta:ToSter - za testy i pomys�y na nowe rozwi�zania
	* Wikipedysta:Beau - za inspiracje i poprawki
\* ------------------------------------------------------------------------ */

//
// Modu�y zewn�trzne dla projekt�w siostrzanych
//
if ( ( typeof sel_t ) !== 'object' ) {
	mw.loader.load( '//pl.wikipedia.org/w/index.php?action=raw&ctype=text/javascript&title=MediaWiki:Gadget-sel_t.js' );
}

/* =====================================================
	Object Init
   ===================================================== */

if ( typeof( wp_sk_show_as_button ) === 'undefined' ) {
	window.wp_sk_show_as_button = true;
}
if ( typeof( wp_sk_redir_enabled ) === 'undefined' ) {
	window.wp_sk_redir_enabled = false;
}

if (window.wp_sk)
{
	alert('B��d krytyczny - konflikt nazw!\n\nJeden ze skrypt�w u�ywa ju� nazwy wp_sk jako zmienn� globaln�.');
}
window.wp_sk = new Object();
wp_sk.version = '2.7.31a';

/* =====================================================
	Function: wp_sk.debug(htxt)

	Wy�wietlenie komunikatu html je�li debug aktywny
   ===================================================== */
wp_sk.debug = function (htxt)
{
	if (typeof wp_sk_debug_enabled!='undefined' && wp_sk_debug_enabled && typeof nux_debug=='function')
	{
		nux_debug(htxt);
	}
}

/* =====================================================
	Function: wp_sk.button()

	Dodaje przycisk sprz�tania
   ===================================================== */
wp_sk.button = function() {
	var that = this;
	mw.loader.using( "ext.gadget.lib-toolbar", function() {
		toolbarGadget.addButton( {
			title: 'Sprz�tanie kodu (wer. ' + that.version + ')',
			alt: 'SK',
			id: 'wp_sk_img_btn',
			oldIcon: '//upload.wikimedia.org/wikipedia/commons/2/2e/Button_broom.png',
			newIcon: '//commons.wikimedia.org/w/thumb.php?f=Broom%20icon.svg&w=22',
			onclick: function() {
				that.cleanup( document.getElementById( 'wpTextbox1' ) );
			}
		} );
	} );
}

/* =====================================================
	Function: wp_sk.warning(input)

	Dodaje ostrze�enie i likwiduje je
	po wci�ni�ciu odpowiedniego przycisku
   ===================================================== */
wp_sk.warning = function() {
	var $summary = jQuery( '#wpSummary' );
	if ( this.nochanges ) {
		// kolorowanka, gdy bez zmian
		$summary.css( 'border', '2px solid #696' );
	} else if ( mw.config.get( 'wgArticleId' ) > 0 ) {
		$summary.css( 'border', '' );

		var text = $summary.val();

		var summary1 = 'po czyszczeniu kodu przejrzyj wykonane zmiany!';
		var summary2 = mw.config.get( 'wp-sk-summary', '[[WP:SK]]' );

		if ( text.indexOf( summary1 ) > -1 || text.indexOf( summary2 ) > -1 ) {
			// opis ju� jest, nie potrzeba nast�pnego
			return;
		}

		if ( text != '' ) {
			text += ', ';
		}
		text += summary1;
		$summary.val( text );
		$summary.addClass( 'summaryWarning' );

		var $diff = jQuery( '#wpDiff' );
		$diff.addClass( 'summaryWarning' );
		$diff.click( function() {
			$summary.val( $summary.val().replace( summary1, summary2 ) );
		} );
	}
}


/* =====================================================
	Function: wp_sk.cleanup(input)

	G��wna funkcja inicjuj�ca i wywo�uj�ca funkcj�
	czyszcz�c�
   ===================================================== */
wp_sk.cleanup = function (input)
{
	// default input
	if (!input)
	{
		input = document.getElementById('wpTextbox1')
	}
	//
	// Pobierz zaznaczony fragment (ca�o�� je�li nic nie zaznaczone)
	//
	var str = sel_t.getSelStr(input, true);
	// OMG - IE & Opera fix
	str = str.replace(/\r\n/g, '\n');

	//
	// Wywo�anie czyszciciela
	//
	str = str.replace(/\n+$/,''); // bez ko�cowych enter�w
	var str_pre = str;
	str = wp_sk.cleaner(str);
	wp_sk.nochanges = (str==str_pre);

	//
	// zapisanie zmian
	//
	if (!wp_sk.nochanges)
	{
		sel_t.qsetSelStr(input, str, true);
	}

	input.focus();

	wp_sk.warning();
}

/* =====================================================
	Function: wp_sk.cleaner(str)

	Funkcja czyszcz�ca podany na wej�ciu ci�g znak�w str.
	Zwraca przetworzony ci�g znak�w.
   ===================================================== */
wp_sk.cleaner = function (str)
{
	//
	// ukrywanie obszar�w w tagach: nowiki, pre, source i math
	str = wp_sk.nowiki.hide(str);

	//
	// sprz�tanie podstawowe
	str = wp_sk.cleanerLinks(str);		// wikilinki
	str = wp_sk.cleanerTpls(str);		// szablony
	str = wp_sk.cleanerWikiVaria(str);	// pozosta�e wikisk�adniowe

	str = wp_sk.cleanerTXT(str);		// poza sk�adniowe

	if (wp_sk.projectSpecificCleanup) {
		str = wp_sk.projectSpecificCleanup(str);
	}

	//
	// ko�cowe porz�dkowanie mi�dzywiki itp
	str = wp_sk.cleanerMagicLinks(str);

	//
	// przywr�cenie ukrytych tag�w
	str = wp_sk.nowiki.show(str);

	return str;
}

/* =====================================================
	Function: wp_sk.cleanerLinks(str)

	Sprz�tanie wikilink�w
   ===================================================== */
wp_sk.cleanerLinks = function (str)
{
	// [[http://]].[http://...]
	str = str.replace(/\[\[([a-z]+:\/\/[^\|\]]+)\]\]/g, '[$1]');
	// [[Kto%C5%9B_jaki%C5%9B#co.C5.9B|...]].[[Kto� jaki�#co�|...]]
	str = str.replace(/\[\[([^|#\]]*)([^|\]]*)(\||\]\])/g, wp_sk.rLinkdecode);

	// poprawa nazw przestrzeni i drobne okoliczne
	str = str.replace(/\[\[(:?) *(image|grafika|file) *: *([^ ])/gi, function (a,dw,co,l1) {return '[['+dw+'Plik:'+l1.toUpperCase();} );
	str = str.replace(/\[\[(:?) *(category|kategoria) *: *([^ ])/gi, function (a,dw,co,l1) {return '[['+dw+'Kategoria:'+l1.toUpperCase();} );
	str = str.replace(/\[\[ *(:?) *(template|szablon) *: *([^ ])/gi, function (a,dw,co,l1) {return '[[Szablon:'+l1.toUpperCase();} );
	str = str.replace(/\[\[ *(:?) *(special|specjalna) *: *([^ ])/gi, function (a,dw,co,l1) {return '[[Specjalna:'+l1.toUpperCase();} );

	str = str.replace(/\[\[ *:? *[Dd]yskusja( [a-z]*) *: */g, '[[Dyskusja$1:');

	// usuni�cie klucza sortowania kat. je�li w ca�o�ci jest prefiksem nazwy artyku�u lub nazw� artyku�u
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

	// zb�dne w obrazkach
	str = str.replace(/(\[\[Plik:[^\n\|\]]+?\|thumb)\|right/g, '$1');		// niepotrzebne
	str = str.replace(/(\[\[Plik:[^\n\|\]]+?)\|right(\|thumb)/g, '$1$2');		// niepotrzebne
	str = str.replace(/(\[\[Plik:[^\|\]]+?\|)frame(\|[0-9x]+px)/, '$1thumb$2');	// prawie na pewno b��d
	str = str.replace(/(\[\[Plik:[^\|\]]+\|[^\|\]]+)\.\]\]/, '$1]]');	// kropka
	// -mid spacje
	/* // zawiesza FF w niekt�rych warunkach, psuje niekt�re opisy
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
	// (ro)zwijanie wikilink�w
	// [[Link|link]] > [[link]] i [[Link|linka]] > [[link]]a
	//str = str.replace(/\[\[([^|\]])([^|\]]*)\|([^\]])\2([a-zA-Z���궱��ӣ�ʦ���]*)\]\]/g, function (a, w1_1, w_rest, w2_1, poza)
	str = str.replace(/\[\[([^|\]])([^|\]]*)\|([^\]])\2([a-z���궱��]*)\]\]/g, function (a, w1_1, w_rest, w2_1, poza)
	{
		return (w1_1.toUpperCase()==w2_1.toUpperCase()) ? '[['+w2_1+w_rest+']]'+poza : a;
	});
	// [[Link|link]]er > [[Link|linker]]
	//str = str.replace(/\[\[([^|\]]+)\|([^|\]]+)\]\]([a-zA-Z���궱��ӣ�ʦ���]+)/g, '[[$1|$2$3]]');
	str = str.replace(/\[\[([^|\]]+)\|([^|\[\]]+)\]\]([a-z���궱��]+)/g, '[[$1|$2$3]]');

	// usuwanie spacji w wikilinkach
	str = str.replace(/\[\[ *([^\]\|:]*[^\]\| ]) *\|/g, '[[$1|');
	str = str.replace(/([^ \t\n])\[\[ +/g, '$1 [[');
	str = str.replace(/\[\[ +/g, '[[');
	str = str.replace(/([^ \t\n])\[\[([^\]\|:]+)\| +/g, '$1 [[$2|');
	str = str.replace(/\[\[([^\]\|:]+)\| +/g, '[[$1|');
	str = str.replace(/([^ \|]) +\]\]([^ \t\na-zA-Z���궱��ӣ�ʦ���])/g, '$1]] $2');
	str = str.replace(/([^ \|]) +\]\]([^a-zA-Z���궱��ӣ�ʦ���])/g, '$1]]$2');

	// sklejanie skr�t�w linkowych
	str = str.replace(/m\.? ?\[\[n\.? ?p\.? ?m\.?\]\]/g, 'm [[n.p.m.]]');

	// korekty dat - niepotrzebny przecinek
	str = str.replace(/(\[\[[0-9]+ (stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|wrze�nia|pa�dziernika|listopada|grudnia)\]\]), (\[\[[0-9]{4}\]\])/g, '$1 $3');

	// linkowanie do wiek�w
	str = str.replace(/\[\[([XVI]{1,5}) [wW]\.?\]\]/g, '[[$1 wiek|$1 w.]]');
	str = str.replace(/\[\[([XVI]{1,5}) [wW]\.?\|/g, '[[$1 wiek|');
	str = str.replace(/\[\[(III|II|IV|VIII|VII|VI|IX|XIII|XII|XI|XIV|XV|XVIII|XVII|XVI|XIX|XXI|XX)\]\]/g, '[[$1 wiek|$1]]');
	str = str.replace(/\[\[(III|II|IV|VIII|VII|VI|IX|XIII|XII|XI|XIV|XV|XVIII|XVII|XVI|XIX|XXI|XX)\|/g, '[[$1 wiek|');

	// rozwijanie typowych link�w
	str = str.replace(/\[\[ang\.\]\]/g, '[[j�zyk angielski|ang.]]');
	str = str.replace(/\[\[cz\.\]\]/g, '[[j�zyk czeski|cz.]]');
	str = str.replace(/\[\[fr\.\]\]/g, '[[j�zyk francuski|fr.]]');
	str = str.replace(/\[\[�ac\.\]\]/g, '[[�acina|�ac.]]');
	str = str.replace(/\[\[niem\.\]\]/g, '[[j�zyk niemiecki|niem.]]');
	str = str.replace(/\[\[pol\.\]\]/g, '[[j�zyk polski|pol.]]');
	str = str.replace(/\[\[pl\.\]\]/g, '[[j�zyk polski|pol.]]');
	str = str.replace(/\[\[ros\.\]\]/g, '[[j�zyk rosyjski|ros.]]');
	str = str.replace(/\[\[(((G|g)iga|(M|m)ega|(K|k)ilo)herc|[GMk]Hz)\|/g, '[[herc|');

	return str;
}
/* =====================================================
	Function: wp_sk.cleanerTpls(str)

	Sprz�tanie szablon�w
   ===================================================== */
wp_sk.cleanerTpls = function (str)
{
	// niepotrzebna przestrze�
	str = str.replace(/\{\{ *([Tt]emplate|[Ss]zablon|msg) *: */g, '{{');

	// zb�dne spacje w szablonach jedno wierszowych
	str = str.replace(/\{\{[ \t]+([^\n\{\} ]+)[ \t]*\}\}/g, '{{$1}}').replace(/\{\{([^\n\{\}]+)[ \t]+\}\}/g, '{{$1}}');

	// poprawki lang i nowy multilang
	str = str.replace(/\{\{[lL]ang\|cz\}\}/g, '{{lang|cs}}');
	str = str.replace(/\{\{[lL]ang\|dk\}\}/g, '{{lang|da}}');
	str = str.replace(/\{\{[lL]ang\|nb\}\}/g, '{{lang|no}}');
	str = str.replace(/(\{\{lang\|[a-z-]+\}\}[\t ]*){2,10}/g, function(a) {
		return '{{lang'+a.replace(/\{\{lang\|([a-z-]+)\}\}\s*/g, '|$1')+'}}';
	});

	// wci�ganie {{lang}} do szablon�w cytowania
	str = str.replace(/{{(cytuj [^{}]+?)}} {{lang\|([a-z-]+)}}/gi, '{{$1 | j�zyk = $2}}');

	// ujednolicanie nazw szablon�w (tabela poni�ej)
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

	// poprawka, bo FF wywala si� na czo�gach np. http://pl.wikipedia.org/w/index.php?title=T-72&diff=14511491&oldid=14437344
	str = str.replace(/<!--[\s\S]+?-->/g, function(a) {
		a
			.replace(/\{/g,'###comment_klamra_l###')
			.replace(/\}/g,'###comment_klamra_r###')
		;
		return a;
	});
	// ucz�owieczanie szablon�w
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

	Sprz�tanie pozosta�ych element�w wikisk�adni
   ===================================================== */
wp_sk.cleanerWikiVaria = function (str)
{
	if ( mw.config.get( 'wp-sk-fix-wikipedia-sections', true ) ) {
		// unifikacja nag��wkowa
		str = str.replace(/[ \n\t]*\n'''? *(Zobacz|Patrz) (te�|tak�e|r�wnie�):* *'''?[ \t]*\n[ \t\n]*/gi, '\n\n== Zobacz te� ==\n');
		str = str.replace(/[ \n\t]*\n'''? *(Zobacz|Patrz) (te�|tak�e|r�wnie�):* *'''?[ \t]*(.+)/gi, function(a, w1, w2, linki)
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
			return '\n\n== Zobacz te� ==\n'+linki;
		});
		str = str.replace(/[ \n\t]*\n(=+) *(Zobacz|Patrz) (te�|tak�e|r�wnie�):* *=+[ \n\t]*/gi, '\n\n$1 Zobacz te� $1\n');
		str = str.replace(/[ \n\t]*\n'''? *((Zewn�trzn[ey] )?(Linki?|��cza|Stron[ay]|Zobacz w (internecie|sieci))( zewn[e�]trzn[aey])?):* *'''?[ \n\t]*/gi, '\n\n== Linki zewn�trzne ==\n');
		str = str.replace(/[ \n\t]*\n(=+) *((Zewn�trzn[ey] )?(Linki?|��cza|Stron[ay]|Zobacz w (internecie|sieci))( zewn[e�]trzn[aey])?):* *=+[ \n\t]*/gi, '\n\n$1 Linki zewn�trzne $1\n');
		str = str.replace(/[ \n\t]*\n(=+) *([��Z]r[�o]d[�l]a):* *=+[ \n\t]*/gi, '\n\n$1 �r�d�a $1\n');
	}

	// nag��wki
	str = str.replace(/(^|\n)(=+) *([^=\n].*?)[ :]*\2(?=\s)/g, '$1$2 $3 $2'); // =a= > = a =, =a:= > = a =
	str = str.replace(/(^|\n)(=+[^=\n]+=+)[\n]{2,}/g, '$1$2\n');	// jeden \n

	if ( mw.config.get( 'wp-sk-fix-wikipedia-sections', true ) ) {
		// przypisy - szablon
		str = str.replace(/\n== Przypisy ==[ \t\n]+<references ?\/>/g, '\n{{Przypisy}}');
		str = str.replace(/\n(={3,}) Przypisy \1[ \t\n]+<references ?\/>/g, '\n{{Przypisy|stopie�= $1}}');
		str = str.replace(/\{\{Przypisy\|stopie�==/g, '{{Przypisy|stopie�= =');
	}

	// przypisy - przyprz�tni�cia
	/*
	// rozwijamy {{r}}, bo kod ni�ej pracuje na <ref/>-ach
	str = str.replace(/{{r((?:\|[^|}]+)*)}}/g, function(a, inside) {
		return inside.replace(/\|([^|}]+)/g, function(b, name) {
			// escape'ujemy " w nazwach
			return '<ref name="' + name.replace(/"/g, "\\\"") + '" />';
		});
	});
	*/
	
	str = str.replace(/<(ref[^<>\/]*?)[ ]*><\/ref>/g, "<$1 />");	// puste na pojedynczy
	str = str.replace(/[ \t]+(<ref[ >]|\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, '$1');		// bez bia�ych przed
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
	str = str.replace(/((?:\s|^)[^& ]*);((?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$1$2;");	// �rednik
	str = str.replace(/([a-zA-Z����󶼿��ʣ�Ӧ��]{5}|[()\[\]{}".'>])[.]((?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$1$2.");	// d�ugi wyraz lub znak specjalny
	str = str.replace(/([a-zA-Z����󶼿��ʣ�Ӧ��][aeiouy��])[.]([']*(?:(?:<ref[\s\S]+?(?:<\/ref|\/)>)|(\{\{[Rr]\|[^}]+\}\}))+)/g, "$1$2.");	// kr�tki z samog�osk�
	str = str.replace(/(<\/ref>|\{\{[Rr]\|[^}]+\}\})\.\.(?=\s)/g, '$1.');  // dwukropek poziomy
	
	/*
	// zwijamy z powrotem <ref/> do {{r}}
	str = str.replace(/< *ref *name *= *(?:"([^">\n]+)"|'([^'>\n]+)'|([^\s'"\/]+)) *\/ *>/g, function(a, name1, name2, name3) {
		return "{{r|" + (name1||name2||name3) + "}}";
	});
	// ��czymy kolejne wywo�ania postaci {{r}}{{r}}
	// nie dzia�a dla wywo�a� z parametrami grupaN=
	str = str.replace(/(\{\{r(\|([^|}]+))+\}\}\s*)+/g, function(refs) {
		return refs.replace(/\}\}\s*\{\{r\|/g, '|');
	});
	*/

	// fakty i interpunkcja
	str = str.replace(/([,])(\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$2$1");	// przecinek
	str = str.replace(/((?:\s|^)[^& ]*);(\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$1$2;");	// �rednik
	str = str.replace(/([a-zA-Z����󶼿��ʣ�Ӧ��]{5}|[()\[\]{}".'>])[.](\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$1$2.");	// d�ugi wyraz lub znak specjalny
	str = str.replace(/([a-zA-Z����󶼿��ʣ�Ӧ��][aeiouy��])[.](\{\{[Ff]akt(?:\|data=[0-9\-]+)?\}\})/g, "$1$2.");	// kr�tki z samog�osk�

	// listy ze spacjami
	str = str.replace(/(\n[#*:;]+)(?![ \t\n#*:;{]|if[a-z]* ?:|switch ?:|time ?:|rel2abs ?:|titleparts ?:)/g, '$1 ');

	// rozwijanie link�w w listach
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

	Sprz�tanie nie zwi�zane bezpo�rednio z wikisk�adni�
   ===================================================== */
wp_sk.cleanerTXT = function (str)
{
	// usuwanie unikodowych znak�w steruj�cych
	str = str.replace(/[\u200B\uFEFF\u200E]/g, '');

	// korekty dat
	// wyst�puje w interwiki (hr)
	//str = str.replace(/([0-9])\. *(stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|wrze�nia|pa�dziernika|listopada|grudnia)/g, '$1 $2')	// niepotrzebna kropka
	str = str.replace(/([^0-9])0([0-9]) *(stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|wrze�nia|pa�dziernika|listopada|grudnia)/g, '$1$2 $3')	// niepotrzebne 0

	// poprawkowate r�ne (kolejno�� jest istotna!)
	str = str.replace(/&deg;/g, '�');
	str = str.replace(/&sum;/g, '.');
	str = str.replace(/&larr;/g, '.');
	str = str.replace(/&rarr;/g, '.');
	str = str.replace(/&uarr;/g, '.');
	str = str.replace(/&darr;/g, '.');
	str = str.replace(/&dagger;/g, '.');
	str = str.replace(/<sup>o<\/sup>/g, '�');

	str = str.replace(/([0-9]) (%|.|�)(?!C)/g, '$1$2'); // bez x �C
	str = str.replace(/([0-9]) (%|.|�)(?!F)/g, '$1$2'); // bez x �F
	str = str.replace(/([0-9])(�[CF])/g, '$1 $2'); // spacja

	str = str.replace(/<\/?br ?\/?>/gi, '<br />');

	// dopisanie kropki itp
	str = str.replace(/ (tzw|tzn) /g, ' $1. ');
	str = str.replace(/([ \n])ok\.([0-9])/g, '$1ok. $2');
	//str = str.replace(/([ \n])ok ([^ ])/g, '$1ok. $2');
	str = str.replace(/ d\/s /g, ' ds. ');
	str = str.replace(/ wg\. /g, ' wg ');

	// sklejanie skr�t�w
	str = str.replace(/m\.? ?(npm|n[. ]{1,3}p[. ]{1,3}m\.?)/g, 'm n.p.m.');
	str = str.replace(/ m\. in\./g, ' m.in.');
	str = str.replace(/ o\. o\./g, ' o.o.');

	// Sprawy wagi Pa�stwowej ;-)
	str = str.replace(/(gmina wiejska w powiecie [a-zA-Z����󶼿��ʣ�Ӧ��\-]+ wojew�dztwa [a-zA-Z����󶼿��ʣ�Ӧ��\-]+) II Rzeczpospolitej/g, '\1 II Rzeczypospolitej');

	return str;
}
/* =====================================================
	Function: wp_sk.cleanerMagicLinks(str)

	Sprz�tanie ko�cowe magicznych link�w i element�w
	powi�zanych - mi�dzywiki, medale dla nich i kategorie.
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
	Funkcje wspomagaj�ce porz�dkowanie           {START}
   ----------------------------------------------------- */
//
// Sprz�tanie infoboks�w
//
wp_sk.rFriendlyIbox = function (a,nazwa,zaw)
{
	if (zaw.indexOf('<!--')!=-1 || zaw.indexOf('=')==-1 || zaw.indexOf('\n')==-1)
	{
		return a;
	}
	nazwa = nazwa.replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");	// trim

	//
	// escapowanie parametr�w
	//
	// wewn�trzne szablony
	zaw = zaw.replace(/<<<(#+)>>>/g,'<<<#$1>>>');
	zaw = zaw.replace(/\{\{(([^\{\}]+)?(\{\{[^\{\}]+\}\})?)*\}\}/g,function(a){ return a.replace(/\|/g,'<<<#>>>') });
	// wewn�trzne linki
	zaw = zaw.replace(/\[\[[^\]]+\]\]/g,function(a){ return a.replace(/\|/g,'<<<#>>>') });

	//
	// sprz�tanie
	//
	// del pustych
	zaw = zaw.replace(/\|\s*(?=\|)/g, function(a) {return (a.indexOf('\n')==-1)?'':'\n'}).replace(/\|\s*$/g, "");
	zaw = zaw.replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");	// trim
	// przeniesienie | na pocz�tek wiersza
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
	// Zako�czenie
	//
	return '{{'+nazwa.substring(0,1).toUpperCase()+nazwa.substring(1)+zaw+'}}';
}
//
// Dekodowanie link�w
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
	Funkcje wspomagaj�ce porz�dkowanie          {KONIEC}
   ===================================================== */

/* =====================================================
	Klasy wspomagaj�ce porz�dkowanie             {START}
   ----------------------------------------------------- */
/* =====================================================
	Class: wp_sk.nowiki

	Ukrywanie obszar�w w tagach: nowiki, pre, source i math

	.hide(str)
		ukrywanie tag�w specjalnych wraz z ich wn�trzami
	.show(str)
		przywr�cenie ukrytych tag�w
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
	// w�a�ciwe ukrywanie
	var re = /<(nowiki|pre|source|math|includeonly|noinclude)(|[ \t\n][^>]*)>/g;
	var m;
	wp_sk.nowiki.tags = new Array();
	// p�ki znaleziono tag otwieraj�cy
	for (var t_i = 0; (m=re.exec(str))!=null; t_i++)
	{
		var start, end, re_end;

		start = m.index;

		// odszukanie ko�ca: </tag([ \t\n]*)>
		re_end = new RegExp("</"+m[1]+"([ \t\n]*)>", "g")
		m = re_end.exec(str.substring(re.lastIndex));
		end = (m==null) ? str.length : re.lastIndex+re_end.lastIndex;

		// dopisanie do tablicy zawarto�ci
		wp_sk.nowiki.tags[t_i] = str.substring(start,end);

		// zamiana ca�o�ci znalezionego obszaru na: <<<indeks>>>
		str = str.substring(0,start)+"<<<"+t_i+">>>"+str.substring(end);

		// szukanie od startu, bo cz�� znak�w ju� usuni�to
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

	Zbieranie, porz�dkowanie i wstawianie kategorii

	.gather(str)
		zbieranie kategorii ze str ze zwrotem nowego str
	.output(a)
		porz�dkuje i zwraca wikitekst z kategoriami;
		parametr a jest nieistotny
	.getDefSort()
		zwraca wyra�enie regularne dla defaultsort
	.newDefSort()
		szukanie nowego (najpopularniejszego) defaultsort

	.art_def_sort
		znaleziony w artykule defaultsort
	.def_sort
		wybrany dla artyku�u defsort
	.arr
		tablica z kategoriami ('nazwa|sorotwanie')
	.arr_i
		indeks pomocniczy, a tak�e liczba element�w w arr
   ===================================================== */
// object init
wp_sk.cat = new Object();
//
// .gather(str)
//
wp_sk.cat.gather = function(str)
{
	//
	// zbi�rka i kasowanie
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
	var orderArray = ['a�', '�', '.', '�', 'b', 'c', '�', 'd', 'e', '�', 'f', 'g', 'h', 'i', 'j', 'k', 'l', '�', 'm', 'n', 'o�', '�', 'p', 'q', 'r', 's', '�', 't', 'u�', 'v', 'w', 'x', 'y', 'z', '�', '�'];
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
	// sortowanie (je�li dost�pna odpowiednia funkcja)
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
	// zb�dne spacje
	for (var i=0; i<wp_sk.cat.arr_i; i++)
	{
		if (/^.+\| $/.test(wp_sk.cat.arr[i]) == false)
		{
			wp_sk.cat.arr[i] = wp_sk.cat.arr[i].replace(/^\s*(\S*(\s+\S+)*)\s*$/, "$1");	// trim
		}
	}

	//
	// "wy�wietlanie" kategorii
	if (reDefSort!="") // je�li jest jaki� defaultsort
	{
		str += '\n{{DEFAULTSORT:'+wp_sk.cat.def_sort+'}}';
		for (var i=0; i<wp_sk.cat.arr_i; i++)
		{
			// je�li nie by�o defaultsort i puste, to dodajemy domy�lne, �eby nie psu�
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
	// szukanie nowego je�li liczba kategorii jest wi�ksza od 1
	else if (wp_sk.cat.arr_i>1)
	{
		wp_sk.cat.def_sort = wp_sk.cat.newDefSort();
	}

	var reDefSort="";
	if (wp_sk.cat.def_sort!="")
	{
		// zamiana na regexp (�eby unikn�� cz�ciowych dopasowa�)
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
	// sprawdzenie, czy wybrano jaki� klucz sortowania w kategoriach
	var sort_i;
	for (sort_i=0; sort_i<wp_sk.cat.arr_i && wp_sk.cat.arr[sort_i].indexOf('|')<0; sort_i++);

	//
	// liczenie kategorii z kluczami
	var total_sort_num = 0;	// ca�kowita liczba kluczy sortowania
	for (var i = sort_i; i<wp_sk.cat.arr_i; i++)	// zaczynamy od ju� znalezionego
	{
		if (wp_sk.cat.arr[i].indexOf('|')>0)
			total_sort_num++;
	}
	//
	// je�li ma�o kluczy (by�oby du�o {{PAGENAME}}), to bez domy�lnego klucza
	if (total_sort_num*2<wp_sk.cat.arr_i) //<50%
	{
		return '';
	}

	//
	// je�li wybrano jakie� sorotwanie, to szukamy nowego klucza (wg popularno�ci)
	if (sort_i!=wp_sk.cat.arr_i)
	{
		//
		//
		var def_sort_num = 0;
		var def_sort_forbiden = ['!', ' ', '*', '+'];
		for (var i = sort_i; i<wp_sk.cat.arr_i; i++)	// zaczynamy od ju� znalezionego
		{
			var j, tmp_def_sort, tmp_def_sort_re, tmp_def_sort_num;

			// dochodzimy do klucza kandyduj�cego
			for (j = i; j<wp_sk.cat.arr_i && wp_sk.cat.arr[j].indexOf('|')<0; j++);
			if (j==wp_sk.cat.arr_i)
				break;
			i = j;

			// klucz
			tmp_def_sort = wp_sk.cat.arr[j].substr(wp_sk.cat.arr[j].indexOf('|')+1);
			if (def_sort == tmp_def_sort)	// ju� by�
			{
				continue;
			}
			// zamiana na regexp (�eby unikn�� cz�ciowych dopasowa�)
			tmp_def_sort_re = tmp_def_sort.replace(/([(){}\[\]\\|.*?$^])/g, '\\$1');	// escapowanie znak�w regexpowych
			tmp_def_sort_re = new RegExp('\\|'+tmp_def_sort_re+'$');

			// liczenie wyst�pie�
			var tmp_def_sort_num=1;
			for (j++; j<wp_sk.cat.arr_i; j++)
			{
				if (tmp_def_sort_re.test(wp_sk.cat.arr[j]))
				{
					tmp_def_sort_num++;
				}
			}

			// kandydyj�cy = nowy?
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

	Zbieranie, porz�dkowanie i wstawianie interwiki

	.gather(str)
		zbieranie interwiki ze str ze zwrotem nowego str
	.output(a)
		porz�dkuje i zwraca wikitekst z interwiki;
		parametr a jest nieistotny
	.comp(a, b)
		por�wnuje a z b i zwraca warto�� odpowiedni�
		dla funkcji sort()

	.order
		tablica z j�zykami ustawionymi wg kolejno�ci
		wg kt�rej maj� by� sortowane interwiki
	.arr
		tablica z interwiki ([j�zyk, artyku�])
	.arr_i
		indeks pomocniczy, a tak�e liczba element�w w arr
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

	Zbieranie, porz�dkowanie i wstawianie interwikowych
	szablon�w Featured Articles

	.gather(str)
		zbieranie szablon�w FA ze str ze zwrotem nowego str
	.output(a)
		porz�dkuje i zwraca wikitekst z szablonami FA;
		parametr a jest nieistotny

	.arr
		tablica z szablonami FA ([j�zyk, artyku�])
	.arr_i
		indeks pomocniczy, a tak�e liczba element�w w arr
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

	this.arr.sort(wp_sk.iWiki.comp); // alfabetycznie wg kodu literowego // funkcja wsp�lna wp_sk.iWiki
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

/* =====================================================
	Class: wp_sk.redir

	Poprawianie redrict�w. Przynajmniej na razie bazuje
	na podgl�dzie artyku�u, w kt�rym redirecty s� oznaczone
	specjaln� klas� (mw-redirect).

	.init()
		inicjowanie poprawek przez wstawienie ikonki przetwarzania
		wyszukanie redirect�w i wys�anie wst�pnego ��dania
		do serwera o rozwini�cie redirect�w
	.resp(res)
		funkcja przyjmuj�ca odpowiedzie� (res) z serwera
		i przetwarzaj�ca j� na tabelk� rozwini�� redirect�w

	.arr	- tabela rozwini�� redirect�w wykorzystywana wewn�trznie
	.arr_i	- indeks u�ywany przy tworzeniu tabeli
	.url	- url wst�pnego zapytania, potrzebny w razie
			konieczno�ci kontynuowania ��da� (wym�g API)
   ===================================================== */
//
// object init
//
wp_sk.redir = new Object();

wp_sk.redir.linkPrefix = document.location.protocol + "//" + document.location.hostname + mw.config.get( 'wgArticlePath' ).replace( '$1', '' );

wp_sk.redir.extractTitle = function( link ) {
	if ( link.substring( 0, this.linkPrefix.length ) != this.linkPrefix ) {
		return null;
	}

	return decodeURIComponent( link.substring( this.linkPrefix.length ).replace( /_/g, ' ' ) ).replace( /#.*$/, '' );
}

//
// .init()
//
wp_sk.redir.init = function()
{
	wp_sk.redir.base_url = mw.util.wikiScript('api') + '?action=query&redirects&format=json&titles=';

	// ograniczenie czasowe, ale tylko w podgl�dzie (�eby nie zam�czy� serwer�w)
	if (wgAction=='submit')
	{
		if (document.cookie.indexOf('wpsk_redir_time_disable=1')!=-1)
		{
			return;
		}
		else
		{
			var d = new Date();
			d = new Date(d.getTime()+300000); //+5min (il. sekund * 1000)
			document.cookie = "wpsk_redir_time_disable=1; path=/; expires=" + d.toGMTString();
		}
	}

	var elWikiBody = document.getElementById('wikiPreview');
	if (elWikiBody)
	{
		//
		// szukanie przekierowa�
		wp_sk.redir.urls = new Array();
		wp_sk.redir.urls[0] = new Array();
		var url_i = url_j = 0;
		var as = jQuery("a.mw-redirect");
		for (var i=0; i<as.length; i++)
		{
			var tmp = this.extractTitle( as[i].href );
			if ( tmp == null ) {
				continue;
			}
			// new url?
			var isnew=true;
			for (var ui=0; ui<=url_i; ui++)
			{
				for (var uj=0; uj<url_j; uj++)
				{
					if (wp_sk.redir.urls[ui][uj]==tmp)
					{
						isnew=false;
						break;
					}
				}
				if (!isnew)
					break;
			}
			// add to array
			if (isnew)
			{
				wp_sk.redir.urls[url_i][url_j++] = tmp;
				if (url_j>=50)	// ograniczenie API
				{
					if (url_i>=4)	// max (4+1)x50 link�w
					{
						break;
					}
					url_j = 0;
					wp_sk.redir.urls[++url_i] = new Array();
				}
			}
		}
		//
		// ostateczne przygotowanie i wysy�anie ��dania
		if (wp_sk.redir.urls[0].length>0)
		{
			var $notice = jQuery('<div id="wp-sk-redir-notice">Sprawdzanie link�w do przekierowa�...</div>');
			jQuery('#wpTextbox1').before($notice);

			// na znalezione redirecty
			wp_sk.redir.arr = new Array();
			wp_sk.redir.arr_i = 0;

			// przygotowanie pierwszej porcji
			wp_sk.redir.urls_i = 0;
			var url = wp_sk.redir.urls[wp_sk.redir.urls_i].join('|');
			wp_sk.redir.url = wp_sk.redir.base_url+url;
			wp_sk.redir.full_prev_url = wp_sk.redir.url;
			//wp_sk.debug('<h2>['+wp_sk.redir.urls_i+']['+wp_sk.redir.urls[wp_sk.redir.urls_i].length+']</h2>');
			// run
			var that = this;
			jQuery.getJSON( wp_sk.redir.url, null, function( result ) {
				that.resp( result );
			} );
		}
	}
}

//
// .resp(res)
//
wp_sk.redir.resp = function (jres)
{
	var that = this;

	// zbi�rka t�umaczenia redirect�w
	var txtescape = /([\\^\$\*\+\?\.\(\)\[\]\{\}\:\=\!\|\,\-])/g;
	for (var r in jres.query.redirects)
	{
		r = jres.query.redirects[r];
		wp_sk.redir.arr[wp_sk.redir.arr_i++] = {
			'rdir' : r.from,
			'art' : r.to
		}
		//wp_sk.debug('['+(wp_sk.redir.arr_i-1)+']rdir:'+r.from+'<br />art:'+r.to);
	}
	// kontynuacja?
	if (jres['query-continue']!=null)
	{
		var continue_url = wp_sk.redir.url + '&plcontinue='+encodeURIComponent(jres['query-continue'].links.plcontinue);
		if (wp_sk.redir.full_prev_url != continue_url)	// <s>api</s> potential bug workaround
		{
			wp_sk.redir.full_prev_url = continue_url;
			jQuery.getJSON( continue_url, null, function( result ) {
				that.resp( result );
			} );
			return;
		}
		else
		{
			//wp_sk.debug('<p style="font-weight:bold;font-size:200%">Warning! Query continue loop.</p>');
		}
	}
	// kolejna porcja link�w
	else if (wp_sk.redir.urls_i < wp_sk.redir.urls.length-1)
	{
		var url = wp_sk.redir.urls[++wp_sk.redir.urls_i].join('|');
		wp_sk.redir.url = wp_sk.redir.base_url+url;
		wp_sk.redir.full_prev_url = wp_sk.redir.url;
		//wp_sk.debug('<h2>['+wp_sk.redir.urls_i+']['+wp_sk.redir.urls[wp_sk.redir.urls_i].length+']</h2>');
		jQuery.getJSON( wp_sk.redir.url, null, function( result ) {
			that.resp( result );
		} );
		return;
	}

	/*
	// debug - start
	var str;
	// szukane
	str = ''
	for (var i=0;i<wp_sk.redir.urls.length;i++)
		for (var j=0;j<wp_sk.redir.urls[i].length;j++)
			str += '\nwp.urls['+i+']['+j+']='+ wp_sk.redir.urls[i][j]
	;
	wp_sk.debug('<textarea>'+str+'</textarea>');

	// znalezione
	str = ''
	for (var i=0;i<wp_sk.redir.arr.length;i++)
		str += '\nwp.rdirs['+i+']='+ wp_sk.redir.arr[i].rdir
	;
	wp_sk.debug('<textarea>'+str+'</textarea>');
	// debug - end
	*/

	// przygotowanie funkcji podmiany redirect�w
	wp_sk.cleanerLinks_orig = wp_sk.cleanerLinks;
	wp_sk.cleanerLinks = function (str)
	{
		var reTxtEscape = /([\\^\$\*\+\?\.\(\)\[\]\{\}\:\=\!\|\,\-])/g;
		for (var page in wp_sk.redir.arr)
		{
			page = wp_sk.redir.arr[page];
			var re = page.rdir.replace(reTxtEscape,'\\$1');
			if (re.search(/^[a-z���궱��]/i)==0)
			{
				re = '['+ re[0].toLowerCase() + re[0].toUpperCase() +']'
					+ re.substr(1);
			}
			var re = new RegExp('\\[\\[('+re+')(\\||\\]\\])', 'g');
			str = str.replace(re, function (a, art, end)
			{
				return '[['+ page.art + (end=='|' ? '|' : '|'+art+']]');
			});
		}

		return wp_sk.cleanerLinks_orig(str);	// dopiero teraz, �eby poprawia� tak�e zmienione linki
	}

	jQuery( "#wp-sk-redir-notice" ).remove();

	var el = document.getElementById( 'wp_sk_img_btn' );
	if ( toolbarGadget.wikieditor ) {
		el.src = '//commons.wikimedia.org/w/thumb.php?f=Broom%20icon%20R.svg&w=22';
	} else {
		el.src = '//upload.wikimedia.org/wikipedia/commons/3/31/Button_broom_R.png';
	}
}
/* -----------------------------------------------------
	Klasy wspomagaj�ce porz�dkowanie            {KONIEC}
   ===================================================== */

/* =====================================================
	Function: Array.prototype.indexOf(elt)

	Dost�pna normalnie: Gecko>1.8b2
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

wp_sk.sz_redirs_tab = {};

/* =====================================================
	OnLoad
   ===================================================== */


jQuery( document ).ready( function() {
	if ( mw.config.get( 'wgAction' ) != 'submit' && mw.config.get( 'wgAction' ) != 'edit' ) {
		return;
	}

	if ( wp_sk_show_as_button ) {
		wp_sk.button();
	}

	// kto� mo�e mie� ustawiony podgl�d od razu przy edycji - w�wczas dzia�a od razu
	if ( wp_sk_redir_enabled ) {
		wp_sk.redir.init();
	}
} );

// </nowiki>

