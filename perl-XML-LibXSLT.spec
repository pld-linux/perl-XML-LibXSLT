#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	LibXSLT
Summary:	XML::LibXSLT - interface to the GNOME libxslt library
Summary(pl):	XML::LibXSLT - interfejs do biblioteki libxslt z GNOME
Name:		perl-XML-LibXSLT
Version:	1.57
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b831bc5a97444103f345105f0f6fced
BuildRequires:	libxslt-devel >= 1.0.6
BuildRequires:	perl-XML-LibXML >= 1.57
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libxslt >= 1.0.6
Requires:	perl-XML-LibXML >= 1.57
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an interface to the GNOME project's libxslt. This is an
extremely good XSLT engine, highly compliant and also very fast. I
have tests showing this to be more than twice as fast as Sablotron.

%description -l pl
Ten modu³ jest interfejsem do libxslt z projektu GNOME. Jest to bardzo
dobry silnik XSLT, o du¿ej zgodno¶ci ze standardem, a tak¿e bardzo
szybki. Wed³ug testów jest ponad dwa razy szybszy od Sablotrona.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/XML/LibXSLT.pm
%{perl_vendorarch}/XML/benchmark.pl
%dir %{perl_vendorarch}/auto/XML/LibXSLT
%{perl_vendorarch}/auto/XML/LibXSLT/LibXSLT.bs
%attr(755,root,root) %{perl_vendorarch}/auto/XML/LibXSLT/LibXSLT.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
