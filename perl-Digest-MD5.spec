#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Digest
%define		pnam	MD5
Summary:	A perl interface to the MD5 digest algorithm
Summary(cs.UTF-8):	Rozhraní s podporou algoritmu MD5 v Perlu
Summary(da.UTF-8):	En perlmodul som implementerer MD5-algoritmen
Summary(de.UTF-8):	Ein Perl-Interface zum MD5 Digest-Algorithmus
Summary(es.UTF-8):	Interfaz perl para el algoritmo MD5 digest
Summary(fr.UTF-8):	Interface perl pour l'algorithme digest MD5
Summary(id.UTF-8):	Antarmuka Perl ke MD5 Digest Algorithm RSA
Summary(is.UTF-8):	Perl skil á RSA Message Digest Algorithm
Summary(it.UTF-8):	Interfaccia perl per l'algoritmo digest MD5
Summary(ja.UTF-8):	MD5 ダイジェストアルゴリズムに対する Perl インターフェイス
Summary(ko.UTF-8):	MD5 digest 알고리즘에 대한 펄 인터페이스
Summary(nb.UTF-8):	En perlmodul som implementerer MD5-algoritmen
Summary(pl.UTF-8):	Interfejs perlowy do algorytmu skrótu MD5
Summary(pt.UTF-8):	Uma interface de Perl para o algoritmo de 'digest' MD5
Summary(pt_BR.UTF-8):	Módulo Perl Digest::MD5
Summary(ru.UTF-8):	Алгоритм генерации "цифровой подписи": MD5
Summary(sk.UTF-8):	Perl rozhranie k RSA MD5 Digest Algorithm
Summary(sv.UTF-8):	Ett Perl-gränssnitt till kontrollsummealgoritmen MD5
Summary(uk.UTF-8):	Алгоритм генерації "цифрового підпису": MD5
Summary(zh_CN.UTF-8):	一个到 MD5 消化算法的 perl 界面。
Name:		perl-Digest-MD5
Version:	2.58
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39543642b1f4773d77def620df3f592a
URL:		http://search.cpan.org/dist/Digest-MD5/
%{?with_tests:BuildRequires:	perl-Encode}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.663
Obsoletes:	perl-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl		Digest::Perl::MD5

%description
The "Digest::MD5" module allows you to use the RSA Data Security Inc.
MD5 Message Digest algorithm from within Perl programs.  The algorithm
takes as input a message of arbitrary length and produces as output a
128-bit "fingerprint" or "message digest" of the input.

%description -l cs.UTF-8
Balíček perl-Digest-MD5 obsahuje modul pro Perl, který implementuje
algoritmus pro výpočet výtahu MD5 (RFC 1321, 128 bitová hodnota, známá
jako digest nebo fingerprint).

%description -l da.UTF-8
Kontrollsummealgoritmen MD5, specificeret i RFC 1321, er en metod for
at beregna et relativt unikt 128-bitars værdi (kallas kontrollsumma
eller fingeravtryck) som en funktion af data af godtycklig størrelse.

%description -l de.UTF-8
Der MD5 Message Digest Algorithmus, der in RFC 1321 angegeben ist,
stellt eine Rechenmethode für relativ eindeutige 128-bit Werte
(bekannt als digest oder fingerprint) als Funktion von Daten einer
arbiträren Größe dar.

%description -l es.UTF-8
El algoritmo MD5 message digest, especificado en el RFC 1321, es un
método para obtener un valor de 128-bits relativamente único (conocido
como digest, o huella) como una función de datos de tamaño arbotrario.

%description -l fr.UTF-8
L'algorithme digest de message MD5, spécifié sous RFC 1321, est une
méthode de traitement d'une valeur 128 bits relativement unique
(connue sous le nom de digest ou d'empreinte digitale) en tant que
fonction de données d'une taille arbitraire.

%description -l it.UTF-8
L'algoritmo MD5 per il calcolo del message digest, specificato in RFC
1321, è un metodo per calcolare un valore lungo 128-bit relativamente
unico (conosciuto come digest o fingerprint) come una funzione di dati
di dimensioni arbitrarie.

%description -l ja.UTF-8
RFC 1321 で指定されている MD5 メッセージダイジェストアルゴリズムは、
比較的一意な 128 ビット値 (ダイジェストまたはフィンガープリントと言い
ます) を任意サイズのデータの関数として計算する方法です。

%description -l pl.UTF-8
Moduł "Digest::MD5" umożliwia korzystanie z algorytmu skrótu MD5 firmy
RSA Data Security Inc. w programach perlowych. Algorytm ten pobiera
jako dane wejściowe komunikat o dowolnej długości i tworzy na wyjściu
128-bitowy "odcisk palca" lub "skrót" danych wejściowych.

%description -l pt.UTF-8
O algoritmo de análise de mensagens de MD5, especificado no RFC 1321,
é um método para calcular um valor de 128 bits relativamente único
(conhecido por 'digest' ou impressão digital) em função de um conjunto
de dados de tamanho arbitrário.

%description -l pt_BR.UTF-8
Módulo Perl Digest::MD5 - Extensão para os algoritmos MD5.

%description -l ru.UTF-8
Содержит модуль для подсчета цифровOJ PODPISI MD5.

%description -l sv.UTF-8
Kontrollsummealgoritmen MD5, specificerad i RFC 1321, är en metod för
att beräkna ett relativt unikt 128-bitars värde (kallas kontrollsumma
eller fingeravtryck) som en funktion av data av godtycklig storlek.

%description -l uk.UTF-8
Містить модуль для підрахунку цифровOGO P&DPISU MD5.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Digest/MD5.pm
%dir %{perl_vendorarch}/auto/Digest/MD5
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/MD5/MD5.so
%{_mandir}/man3/Digest::MD5.3pm*
