%include	/usr/lib/rpm/macros.perl

%define	pdir	XML
%define	pnam	LibXSLT

Summary:	XML-LibXSLT perl module
Summary(pl):	Modu³ perla XML-LibXSLT
Name:		perl-%{pdir}-%{pnam}
Version:	1.31
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-XML-LibXML >= 1.30
BuildRequires:	libxslt-devel >= 1.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	libxslt >= 1.0.6

%description
This module is an interface to the gnome project's libxslt. This is an
extremely good XSLT engine, highly compliant and also very fast. I
have tests showing this to be more than twice as fast as Sablotron.

%description -l pl
Ten modu³ jest interfejsem do libxslt z projektu GNOME. Jest to bardzo
dobry silnik XSLT, o du¿ej zgodno¶ci ze standardem, a tak¿e bardzo
szybki. Wed³ug testów jest ponad dwa razy szybszy od Sablotrona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/XML/LibXSLT.pm
%dir %{perl_sitearch}/auto/XML/LibXSLT
%{perl_sitearch}/auto/XML/LibXSLT/LibXSLT.bs
%attr(755,root,root) %{perl_sitearch}/auto/XML/LibXSLT/LibXSLT.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
