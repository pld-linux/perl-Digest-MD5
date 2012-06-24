%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	MD5
Summary:	Perl Digest::MD5 module
Summary(es):	Modulo Perl Digest
Summary(pl):	Modu� Perla Digest::MD5
Summary(pt_BR):	M�dulo Digest
Summary(ru):	��������� ��������� "�������� �������": MD5, MD2, SHA1 & HMAC
Summary(uk):	��������� ������æ� "��������� Ц�����": MD5, MD2, SHA1 & HMAC
Name:		perl-Digest-MD5
Version:	2.20
Release:	4
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
Obsoletes:	perl-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(Digest::Perl::MD5)"

%description
Provides access to the MD5 algorithm from RSA.

%description -l es
Perl module Digest::MD5 - Extension interface to MD5, MD2, NIST SHA-1.

%description -l pl
Modu� perla wspomagaj�cy algorytm MD5.

%description -l pt_BR
M�dulo Perl Digest::MD5 - Extens�o para os algoritmos MD5, MD2, NIST
SHA-1.

%description -l ru
�������� ������ ��� �������� �������� �������� MD5, MD2, SHA1 � HMAC.

%description -l uk
������ ����̦ ��� Ц�������� �������� Ц���Ӧ� MD5, MD2, SHA1 ��
HMAC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/Digest/*
%dir %{perl_sitearch}/auto/Digest/*
%{perl_sitearch}/auto/Digest/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/*/*.so

%{_mandir}/man3/*
