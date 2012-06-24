#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	MD5
Summary:	A perl interface to the MD5 digest algorithm
Summary(cs):	Rozhran� s podporou algoritmu MD5 v Perlu
Summary(da):	En perlmodul som implementerer MD5-algoritmen
Summary(de):	Ein Perl-Interface zum MD5 Digest-Algorithmus
Summary(es):	Interfaz perl para el algoritmo MD5 digest
Summary(fr):	Interface perl pour l'algorithme digest MD5
Summary(id):	Antarmuka Perl ke MD5 Digest Algorithm RSA
Summary(is):	Perl skil � RSA Message Digest Algorithm
Summary(it):	Interfaccia perl per l'algoritmo digest MD5
Summary(ja):	MD5 �����������ȥ��르�ꥺ����Ф��� Perl ���󥿡��ե�����
Summary(ko):	MD5 digest �˰��� ���� �� �������̽�
Summary(no):	En perlmodul som implementerer MD5-algoritmen
Summary(pl):	Modu� Perla Digest::MD5
Summary(pt):	Uma interface de Perl para o algoritmo de 'digest' MD5
Summary(pt_BR):	M�dulo Perl Digest::MD5
Summary(ru):	�������� ��������� "�������� �������": MD5
Summary(sk):	Perl rozhranie k RSA MD5 Digest Algorithm
Summary(sv):	Ett Perl-gr�nssnitt till kontrollsummealgoritmen MD5
Summary(uk):	�������� ������æ� "��������� Ц�����": MD5
Summary(zh_CN):	һ���� MD5 �����㷨�� perl ���档
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
Bal��ek perl-Digest-MD5 obsahuje modul pro Perl, kter� implementuje
algoritmus pro v�po�et v�tahu MD5 (RFC 1321, 128 bitov� hodnota, zn�m�
jako digest nebo fingerprint).

%description -l da
Kontrollsummealgoritmen MD5, specificeret i RFC 1321, er en metod for
at beregna et relativt unikt 128-bitars v�rdi (kallas kontrollsumma
eller fingeravtryck) som en funktion af data af godtycklig st�rrelse.

%description -l de
Der MD5 Message Digest Algorithmus, der in RFC 1321 angegeben ist,
stellt eine Rechenmethode f�r relativ eindeutige 128-bit Werte
(bekannt als digest oder fingerprint) als Funktion von Daten einer
arbitr�ren Gr��e dar.

%description -l es
El algoritmo MD5 message digest, especificado en el RFC 1321, es un
m�todo para obtener un valor de 128-bits relativamente �nico (conocido
como digest, o huella) como una funci�n de datos de tama�o arbotrario.

%description -l fr
L'algorithme digest de message MD5, sp�cifi� sous RFC 1321, est une
m�thode de traitement d'une valeur 128 bits relativement unique
(connue sous le nom de digest ou d'empreinte digitale) en tant que
fonction de donn�es d'une taille arbitraire.

%description -l it
L'algoritmo MD5 per il calcolo del message digest, specificato in RFC
1321, � un metodo per calcolare un valore lungo 128-bit relativamente
unico (conosciuto come digest o fingerprint) come una funzione di dati
di dimensioni arbitrarie.

%description -l ja
RFC 1321 �ǻ��ꤵ��Ƥ��� MD5 ��å����������������ȥ��르�ꥺ��ϡ�
���Ū��դ� 128 �ӥå��� (�����������Ȥޤ��ϥե��󥬡��ץ��Ȥȸ���
�ޤ�) ��Ǥ�ե������Υǡ����δؿ��Ȥ��Ʒ׻�������ˡ�Ǥ���

%description -l pl
Modu� perla wspomagaj�cy algorytm MD5.

%description -l pt
O algoritmo de an�lise de mensagens de MD5, especificado no RFC 1321,
� um m�todo para calcular um valor de 128 bits relativamente �nico
(conhecido por 'digest' ou impress�o digital) em fun��o de um conjunto
de dados de tamanho arbitr�rio.

%description -l pt_BR
M�dulo Perl Digest::MD5 - Extens�o para os algoritmos MD5.

%description -l ru
�������� ������ ��� �������� ������OJ PODPISI MD5.

%description -l sv
Kontrollsummealgoritmen MD5, specificerad i RFC 1321, �r en metod f�r
att ber�kna ett relativt unikt 128-bitars v�rde (kallas kontrollsumma
eller fingeravtryck) som en funktion av data av godtycklig storlek.

%description -l uk
������ ������ ��� Ц�������� ������OGO P&DPISU MD5.

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
