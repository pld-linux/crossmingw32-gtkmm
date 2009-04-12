Summary:	A C++ interface for the GTK+ (a GUI library for X) - cross Mingw32 version
Summary(pl.UTF-8):	Wrapper C++ dla GTK+ - skrośna wersja Mingw32
%define		realname   gtkmm
Name:		crossmingw32-%{realname}
Version:	2.16.0
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.16/%{realname}-%{version}.tar.bz2
# Source0-md5:	a82e3b5b93008421ff67df16d1e51ec2
URL:		http://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	crossmingw32-atk >= 1.24.0
BuildRequires:	crossmingw32-cairomm >= 1.6.3
BuildRequires:	crossmingw32-gcc-c++ >= 3.3.1
BuildRequires:	crossmingw32-glibmm >= 2.18.0
BuildRequires:	crossmingw32-gtk+2 >= 2.16.0
BuildRequires:	crossmingw32-pangomm >= 2.14.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig >= 1:0.15
Requires:	%{name}-atk = %{version}-%{release}
Requires:	crossmingw32-cairomm >= 1.6.3
Requires:	crossmingw32-gtk+2 >= 2.16.0
Requires:	crossmingw32-pangomm >= 2.14.0
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

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker
%define		filterout_ld	-Wl,-z,.*

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
Summary:	Static gtkmm libraries (cross mingw32 version)
Summary(pl.UTF-8):	Statyczne biblioteki gtkmm (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static gtkmm libraries (cross mingw32 version).

%description static -l pl.UTF-8
Statyczne biblioteki gtkmm (wersja skrośna mingw32).

%package dll
Summary:	DLL gtkmm libraries for Windows
Summary(pl.UTF-8):	Biblioteki DLL gtkmm dla Windows
Group:		Applications/Emulators
Requires:	%{name}-atk-dll = %{version}-%{release}
Requires:	crossmingw32-cairomm-dll >= 1.6.3
Requires:	crossmingw32-gtk+2-dll >= 2.16.0
Requires:	crossmingw32-pangomm-dll >= 2.14.0
Requires:	wine

%description dll
DLL gtkmm libraries for Windows.

%description dll -l pl.UTF-8
Biblioteki DLL gtkmm dla Windows.

%package atk
Summary:	A C++ interface for atk library (cross mingw32 version)
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	crossmingw32-atk >= 1.24.0
Requires:	crossmingw32-glibmm >= 2.18.0

%description atk
A C++ interface for atk library (cross mingw32 version).

%description atk -l pl.UTF-8
Interfejs C++ dla biblioteki atk (wersja skrośna mingw32).

%package atk-static
Summary:	Static atkmm library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka atkmm (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name}-atk = %{version}-%{release}

%description atk-static
Static atkmm library (cross mingw32 version).

%description atk-static -l pl.UTF-8
Statyczna biblioteka atkmm (wersja skrośna mingw32).

%package atk-dll
Summary:	DLL atkmm library for Windows
Summary(pl.UTF-8):	Biblioteka DLL atkmm dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-atk-dll >= 1.24.0
Requires:	crossmingw32-glibmm-dll >= 2.18.0
Requires:	wine

%description atk-dll
DLL atkmm library for Windows.

%description atk-dll -l pl.UTF-8
Biblioteka DLL atkmm dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%build
export PKG_CONFIG_LIBDIR=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtkmm-2.4/proc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CHANGES NEWS PORTING README
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

%files atk
%defattr(644,root,root,755)
%{_libdir}/libatkmm-1.6.dll.a
%{_libdir}/libatkmm-1.6.la
%{_includedir}/atkmm-1.6
%{_pkgconfigdir}/atkmm-1.6.pc

%files atk-static
%defattr(644,root,root,755)
%{_libdir}/libatkmm-1.6.a

%files atk-dll
%defattr(644,root,root,755)
%{_dlldir}/libatkmm-1.6-*.dll
