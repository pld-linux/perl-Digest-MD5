%include 	/usr/lib/rpm/macros.perl
Summary:	Perl Digest-MD5 module
Summary(pl):	Modu³ Perla Digest-MD5
Name:		perl-Digest-MD5
Version:	2.16
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Digest/Digest-MD5-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
Obsoletes:	perl-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(Digest::Perl::MD5)"

%description
Provides access to the md5 algorithm from RSA.

%description -l pl
Modu³ perla wspomagaj±cy algorytm md5.

%prep
%setup -q -n Digest-MD5-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/Digest
%dir %{perl_sitearch}/auto/Digest
%dir %{perl_sitearch}/auto/Digest/*
%{perl_sitearch}/auto/Digest/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/*/*.so

%{_mandir}/man3/*
