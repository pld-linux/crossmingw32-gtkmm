# TODO
# - think of eliminating cpp runtime dep, as cpp pulls gcc
#
%include	/usr/lib/rpm/macros.perl
Summary:	A C++ interface for the GTK+ (a GUI library for X) - cross Mingw32 version
Summary(pl):	Wrapper C++ dla GTK+ - skro¶na wersja Mingw32
%define		_realname   gtkmm
Name:		crossmingw32-%{_realname}
Version:	2.10.7
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.10/%{_realname}-%{version}.tar.bz2
# Source0-md5:	d8885c0c5350deb201417cc4032c4e09
Patch0:		%{name}-noexamples.patch
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	crossmingw32-atk >= 1.12.3
BuildRequires:	crossmingw32-cairomm >= 1.2.2
BuildRequires:	crossmingw32-glibmm >= 2.12.5
BuildRequires:	crossmingw32-gtk+2 >= 2.10.6
#BuildRequires:	crossmingw32-libstdc++>= 3.3.1
BuildRequires:	crossmingw32-pango >= 1.14.7
BuildRequires:	crossmingw32-pkgconfig
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	%{name}-atk = %{version}-%{release}
Requires:	%{name}-pango = %{version}-%{release}
Requires:	cpp
Requires:	crossmingw32-cairomm >= 1.2.2
Requires:	crossmingw32-gtk+2 >= 2.10.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

%description -l pl
GTK-- jest wrapperem C++ dla Gimp ToolKit (GTK). GTK+ jest bibliotek±
s³u¿±c± do tworzenia graficznych interfejsów. W pakiecie znajduje siê
tak¿e biblioteka GDK-- - wrapper C++ dla GDK (General Drawing Kit).

%package atk
Summary:	A C++ interface for atk library
Summary(pl):	Interfejs C++ dla biblioteki atk
Group:		X11/Development/Libraries
Requires:	atk >= 1:1.12.3
Requires:	glibmm >= 2.12.5

%description atk
A C++ interface for atk library.

%description atk -l pl
Interfejs C++ dla biblioteki atk.

%package pango
Summary:	A C++ interface for pango library
Summary(pl):	Interfejs C++ dla biblioteki pango
Group:		X11/Development/Libraries
Requires:	cairomm >= 1.2.2
Requires:	glibmm >= 2.12.5
Requires:	pango >= 1:1.14.7

%description pango
A C++ interface for pango library.

%description pango -l pl
Interfejs C++ dla biblioteki pango.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p1

%build
export PKG_CONFIG_PATH=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
# exceptions and rtti are used in this package --misiek
%configure \
	--targe=%{target} \
	--host=%{target} \
	--disable-demos \
	--disable-docs \
	--disable-examples \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CHANGES NEWS PORTING README
%{_libdir}/libg[dt]kmm*.la
%{_libdir}/libg[dt]kmm*.a
%{_libdir}/g[dt]kmm-2.4
%{_bindir}/libg[dt]kmm*.dll
%{_includedir}/g[dt]kmm-2.4
%{_pkgconfigdir}/g[dt]kmm*.pc

%files atk
%defattr(644,root,root,755)
%{_libdir}/libatkmm*.la
%{_libdir}/libatkmm*.a
%{_bindir}/libatkmm*.dll
%{_pkgconfigdir}/atkmm*.pc
%{_includedir}/atkmm-1.6

%files pango
%defattr(644,root,root,755)
%{_libdir}/libpangomm*.la
%{_libdir}/libpangomm*.a
%{_bindir}/libpangomm*.dll
%{_pkgconfigdir}/pangomm*.pc
%{_includedir}/pangomm-1.4
