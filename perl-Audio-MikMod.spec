#
# Conditional build:
# _with_tests - perform "make test" - needs working audio device
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	MikMod
Summary:	Audio::MikMod Perl module - extension for libmikmod
Summary(pl):	Modu³ Perla Audio::MikMod - rozszezenie do libmikmod
Name:		perl-Audio-MikMod
Version:	0.5
Release:	5
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-Time-HiRes >= 1.20
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	libmikmod-devel >= 3.1.7
Requires:	perl-Time-HiRes >= 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to the libmikmod library for playing
MOD, IT, XM, S3M, MTM, 669, STM, ULT, FAR, MED, AMF, DSM, IMF, GDM,
and STX tracker files. In addition, manipulation of WAV samples is
supported.

%description -l pl
Ten modu³ udostêpnia interfejs do biblioteki libmikmod w celu
odtwarzania plików MOD, IT, XM, S3M, MTM, 669, STM, ULT, FAR, MED,
AMF, DSM, IMF, GDM i STX. Dodatkowo umo¿liwia obs³ugê sampli WAV.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install demo/{*pm,player*} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Audio/MikMod.pm
%dir %{perl_vendorarch}/auto/Audio/MikMod
%{perl_vendorarch}/auto/Audio/MikMod/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/MikMod/*.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/player*
