%include 	/usr/lib/rpm/macros.perl
Summary:	Perl Digest-MD5 module
Summary(pl):	Modu³ Perla Digest-MD5
Name:		perl-Digest-MD5
Version:	2.09
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Digest-MD5-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides access to the md5 algorithm from RSA.

%description -l pl
Modu³ perla wspomagaj±cy algorytm md5.

%prep
%setup -q -n Digest-MD5-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT 

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Digest/MD5/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

strip --strip-unneeded $RPM_BUILD_ROOT%{perl_sitearch}/auto/Digest/*/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/*.pm
%{perl_sitearch}/Digest

%dir %{perl_sitearch}/auto/Digest
%dir %{perl_sitearch}/auto/Digest/*

%{perl_sitearch}/auto/Digest/*/*.bs
%{perl_sitearch}/auto/Digest/MD5/.packlist
%attr(755,root,root) %{perl_sitearch}/auto/Digest/*/*.so

%{_mandir}/man3/*
