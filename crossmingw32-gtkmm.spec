Summary:	A C++ interface for the GTK+ (a GUI library for X) - cross MinGW32 version
Summary(pl.UTF-8):	Wrapper C++ dla GTK+ - skrośna wersja MinGW32
%define		realname   gtkmm
Name:		crossmingw32-%{realname}
Version:	2.24.4
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.24/%{realname}-%{version}.tar.xz
# Source0-md5:	b9ac60c90959a71095f07f84dd39961d
URL:		http://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	crossmingw32-atkmm >= 2.22.2
BuildRequires:	crossmingw32-cairomm >= 1.6.3
BuildRequires:	crossmingw32-gcc-c++ >= 3.3.1
BuildRequires:	crossmingw32-glibmm >= 2.28.0
BuildRequires:	crossmingw32-gtk+2 >= 2.20.0
BuildRequires:	crossmingw32-pangomm >= 2.28.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig >= 1:0.15
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	crossmingw32-atkmm >= 2.22.2
Requires:	crossmingw32-cairomm >= 1.6.3
Requires:	crossmingw32-gtk+2 >= 2.20.0
Requires:	crossmingw32-pangomm >= 2.28.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++
%define		__pkgconfig_provides	%{nil}
%define		__pkgconfig_requires	%{nil}

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker, most of -f options are Linux-specific
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*
%define		filterout_cxx	-f[-a-z0-9=]*

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

This package contains the cross version for Win32.

%description -l pl.UTF-8
gtkmm jest wrapperem C++ dla Gimp ToolKit (GTK). GTK+ jest biblioteką
służącą do tworzenia graficznych interfejsów. W pakiecie znajduje się
także biblioteka gdkmm - wrapper C++ dla GDK (General Drawing Kit).

Ten pakiet zawiera wersję skrośną dla Win32.

%package static
Summary:	Static gtkmm libraries (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczne biblioteki gtkmm (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static gtkmm libraries (cross MinGW32 version).

%description static -l pl.UTF-8
Statyczne biblioteki gtkmm (wersja skrośna MinGW32).

%package dll
Summary:	DLL gtkmm libraries for Windows
Summary(pl.UTF-8):	Biblioteki DLL gtkmm dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-atkmm-dll >= 2.22.2
Requires:	crossmingw32-cairomm-dll >= 1.6.3
Requires:	crossmingw32-glibmm-dll >= 2.28.0
Requires:	crossmingw32-gtk+2-dll >= 2.20.0
Requires:	crossmingw32-pangomm-dll >= 2.28.0
Requires:	wine

%description dll
DLL gtkmm libraries for Windows.

%description dll -l pl.UTF-8
Biblioteki DLL gtkmm dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%build
export PKG_CONFIG_LIBDIR=%{_prefix}/lib/pkgconfig:%{_npkgconfigdir}
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--targe=%{target} \
	--host=%{target} \
	--disable-documentation \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING README
%{_libdir}/libgdkmm-2.4.dll.a
%{_libdir}/libgtkmm-2.4.dll.a
%{_libdir}/libgdkmm-2.4.la
%{_libdir}/libgtkmm-2.4.la
%{_libdir}/gdkmm-2.4
%{_libdir}/gtkmm-2.4
%{_includedir}/gdkmm-2.4
%{_includedir}/gtkmm-2.4
%{_pkgconfigdir}/gdkmm-2.4.pc
%{_pkgconfigdir}/gtkmm-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkmm-2.4.a
%{_libdir}/libgtkmm-2.4.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libgdkmm-2.4-*.dll
%{_dlldir}/libgtkmm-2.4-*.dll
