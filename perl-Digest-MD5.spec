%include 	/usr/lib/rpm/macros.perl
Summary:	Perl Digest-MD5 module
Summary(pl):	Modu³ Perla Digest-MD5
Name:		perl-Digest-MD5
Version:	2.13
Release:	1
License:	Distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Digest/Digest-MD5-%{version}.tar.gz
Patch0:		%{name}-rpmperl-automation-workaround.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl
Obsoletes:	perl-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides access to the md5 algorithm from RSA.

%description -l pl
Modu³ perla wspomagaj±cy algorytm md5.

%prep
%setup -q -n Digest-MD5-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
