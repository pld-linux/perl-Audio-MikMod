#
# Conditional build:
%bcond_with	tests	# perform "make test" - needs working audio device

%define		pdir	Audio
%define		pnam	MikMod
Summary:	Audio::MikMod Perl module - extension for libmikmod
Summary(pl.UTF-8):	Moduł Perla Audio::MikMod - rozszezenie do libmikmod
Name:		perl-Audio-MikMod
Version:	0.5
Release:	25
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31c8f3dfe79feebcef803a7683596ae4
URL:		http://search.cpan.org/dist/Audio-MikMod/
BuildRequires:	libmikmod-devel >= 3.1.7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to the libmikmod library for playing
MOD, IT, XM, S3M, MTM, 669, STM, ULT, FAR, MED, AMF, DSM, IMF, GDM,
and STX tracker files. In addition, manipulation of WAV samples is
supported.

%description -l pl.UTF-8
Ten moduł udostępnia interfejs do biblioteki libmikmod w celu
odtwarzania plików MOD, IT, XM, S3M, MTM, 669, STM, ULT, FAR, MED,
AMF, DSM, IMF, GDM i STX. Dodatkowo umożliwia obsługę sampli WAV.

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p demo/{*pm,player*} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Audio/MikMod.pm
%dir %{perl_vendorarch}/auto/Audio/MikMod
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/MikMod/*.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/player*
