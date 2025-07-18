#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	XML
%define		pnam	LibXSLT
Summary:	XML::LibXSLT - interface to the GNOME libxslt library
Summary(pl.UTF-8):	XML::LibXSLT - interfejs do biblioteki libxslt z GNOME
Name:		perl-XML-LibXSLT
Version:	2.003000
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	632dce587b3c405edd4e622364750191
URL:		https://metacpan.org/dist/XML-LibXSLT
BuildRequires:	libxslt-devel >= 1.1.28
BuildRequires:	perl-XML-LibXML >= 1.75
BuildRequires:	perl-devel >= 1:5.14
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%if "%(perl -MXML::LibXML -e 'print XML::LibXML::LIBXML_VERSION == XML::LibXML::LIBXML_RUNTIME_VERSION || 0' 2>/dev/null)" == "0"
BuildRequires:	REBUILD-perl-XML-LibXML
%endif
%endif
Requires:	libxslt >= 1.1.28
Requires:	perl-XML-LibXML >= 1.70
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an interface to the GNOME project's libxslt. This is an
extremely good XSLT engine, highly compliant and also very fast. I
have tests showing this to be more than twice as fast as Sablotron.

%description -l pl.UTF-8
Ten moduł jest interfejsem do libxslt z projektu GNOME. Jest to bardzo
dobry silnik XSLT, o dużej zgodności ze standardem, a także bardzo
szybki. Według testów jest ponad dwa razy szybszy od Sablotrona.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%{perl_vendorarch}/XML/LibXSLT.pm
%{perl_vendorarch}/XML/LibXSLT
%dir %{perl_vendorarch}/auto/XML/LibXSLT
%attr(755,root,root) %{perl_vendorarch}/auto/XML/LibXSLT/LibXSLT.so
%{_mandir}/man3/XML::LibXSLT.3pm*
%{_mandir}/man3/XML::LibXSLT::Quick.3pm*
%{_examplesdir}/%{name}-%{version}
