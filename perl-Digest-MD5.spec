#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	MD5
Summary:	A perl interface to the MD5 digest algorithm
Summary(cs):	Rozhraní s podporou algoritmu MD5 v Perlu
Summary(da):	En perlmodul som implementerer MD5-algoritmen
Summary(de):	Ein Perl-Interface zum MD5 Digest-Algorithmus
Summary(es):	Interfaz perl para el algoritmo MD5 digest
Summary(fr):	Interface perl pour l'algorithme digest MD5
Summary(id):	Antarmuka Perl ke MD5 Digest Algorithm RSA
Summary(is):	Perl skil á RSA Message Digest Algorithm
Summary(it):	Interfaccia perl per l'algoritmo digest MD5
Summary(ja):	MD5 ¥À¥¤¥¸¥§¥¹¥È¥¢¥ë¥´¥ê¥º¥à¤ËÂĞ¤¹¤ë Perl ¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹
Summary(ko):	MD5 digest ¾Ë°í¸®Áò¿¡ ´ëÇÑ ÆŞ ÀÎÅÍÆäÀÌ½º
Summary(no):	En perlmodul som implementerer MD5-algoritmen
Summary(pl):	Modu³ Perla Digest::MD5
Summary(pt):	Uma interface de Perl para o algoritmo de 'digest' MD5
Summary(pt_BR):	Módulo Perl Digest::MD5
Summary(ru):	áÌÇÏÒÉÔÍ ÇÅÎÅÒÁÃÉÉ "ÃÉÆÒÏ×ÏÊ ĞÏÄĞÉÓÉ": MD5
Summary(sk):	Perl rozhranie k RSA MD5 Digest Algorithm
Summary(sv):	Ett Perl-gränssnitt till kontrollsummealgoritmen MD5
Summary(uk):	áÌÇÏÒÉÔÍ ÇÅÎÅÒÁÃ¦§ "ÃÉÆÒÏ×ÏÇÏ Ğ¦ÄĞÉÓÕ": MD5
Summary(zh_CN):	Ò»¸öµ½ MD5 Ïû»¯Ëã·¨µÄ perl ½çÃæ¡£
Name:		perl-Digest-MD5
Version:	2.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b53c5c1a199932122f52f14b01252399
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Digest::Perl::MD5)'

%description
Provides access to the MD5 algorithm from RSA.

%description -l cs
Balíèek perl-Digest-MD5 obsahuje modul pro Perl, kterı implementuje
algoritmus pro vıpoèet vıtahu MD5 (RFC 1321, 128 bitová hodnota, známá
jako digest nebo fingerprint).

%description -l da
Kontrollsummealgoritmen MD5, specificeret i RFC 1321, er en metod for
at beregna et relativt unikt 128-bitars værdi (kallas kontrollsumma
eller fingeravtryck) som en funktion af data af godtycklig størrelse.

%description -l de
Der MD5 Message Digest Algorithmus, der in RFC 1321 angegeben ist,
stellt eine Rechenmethode für relativ eindeutige 128-bit Werte
(bekannt als digest oder fingerprint) als Funktion von Daten einer
arbiträren Größe dar.

%description -l es
El algoritmo MD5 message digest, especificado en el RFC 1321, es un
método para obtener un valor de 128-bits relativamente único (conocido
como digest, o huella) como una función de datos de tamaño arbotrario.

%description -l fr
L'algorithme digest de message MD5, spécifié sous RFC 1321, est une
méthode de traitement d'une valeur 128 bits relativement unique
(connue sous le nom de digest ou d'empreinte digitale) en tant que
fonction de données d'une taille arbitraire.

%description -l it
L'algoritmo MD5 per il calcolo del message digest, specificato in RFC
1321, è un metodo per calcolare un valore lungo 128-bit relativamente
unico (conosciuto come digest o fingerprint) come una funzione di dati
di dimensioni arbitrarie.

%description -l ja
RFC 1321 ¤Ç»ØÄê¤µ¤ì¤Æ¤¤¤ë MD5 ¥á¥Ã¥»¡¼¥¸¥À¥¤¥¸¥§¥¹¥È¥¢¥ë¥´¥ê¥º¥à¤Ï¡¢
Èæ³ÓÅª°ì°Õ¤Ê 128 ¥Ó¥Ã¥ÈÃÍ (¥À¥¤¥¸¥§¥¹¥È¤Ş¤¿¤Ï¥Õ¥£¥ó¥¬¡¼¥×¥ê¥ó¥È¤È¸À¤¤
¤Ş¤¹) ¤òÇ¤°Õ¥µ¥¤¥º¤Î¥Ç¡¼¥¿¤Î´Ø¿ô¤È¤·¤Æ·×»»¤¹¤ëÊıË¡¤Ç¤¹¡£

%description -l pl
Modu³ perla wspomagaj±cy algorytm MD5.

%description -l pt
O algoritmo de análise de mensagens de MD5, especificado no RFC 1321,
é um método para calcular um valor de 128 bits relativamente único
(conhecido por 'digest' ou impressão digital) em função de um conjunto
de dados de tamanho arbitrário.

%description -l pt_BR
Módulo Perl Digest::MD5 - Extensão para os algoritmos MD5.

%description -l ru
óÏÄÅÒÖÉÔ ÍÏÄÕÌØ ÄÌÑ ĞÏÄÓŞÅÔÁ ÃÉÆÒÏ×OJ PODPISI MD5.

%description -l sv
Kontrollsummealgoritmen MD5, specificerad i RFC 1321, är en metod för
att beräkna ett relativt unikt 128-bitars värde (kallas kontrollsumma
eller fingeravtryck) som en funktion av data av godtycklig storlek.

%description -l uk
í¦ÓÔÉÔØ ÍÏÄÕÌØ ÄÌÑ Ğ¦ÄÒÁÈÕÎËÕ ÃÉÆÒÏ×OGO P&DPISU MD5.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Digest/*
%dir %{perl_vendorarch}/auto/Digest/*
%{perl_vendorarch}/auto/Digest/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/*/*.so
%{_mandir}/man3/*
