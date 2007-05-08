Summary:	A C++ interface for the GTK+ (a GUI library for X) - cross Mingw32 version
Summary(pl.UTF-8):	Wrapper C++ dla GTK+ - skrośna wersja Mingw32
%define		_realname   gtkmm
Name:		crossmingw32-%{_realname}
Version:	2.10.10
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.10/%{_realname}-%{version}.tar.bz2
# Source0-md5:	c86ccbed9735be84689baac2f38015bf
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	crossmingw32-atk >= 1.18.0
BuildRequires:	crossmingw32-cairomm >= 1.2.4
BuildRequires:	crossmingw32-gcc-c++ >= 3.3.1
BuildRequires:	crossmingw32-glibmm >= 2.12.9
BuildRequires:	crossmingw32-gtk+2 >= 2.10.11
BuildRequires:	crossmingw32-pango >= 1.16.2
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
Requires:	%{name}-atk = %{version}-%{release}
Requires:	%{name}-pango = %{version}-%{release}
Requires:	crossmingw32-gtk+2 >= 2.10.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
This package provides a C++ interface for GTK+ (the Gimp ToolKit) GUI
library. The interface provides a convenient interface for C++
programmers to create GUIs with GTK+'s flexible object-oriented
framework. Features include type safe callbacks, widgets that are
extensible using inheritance and over 110 classes that can be freely
combined to quickly create complex user interfaces.

This package contains the cross version for Win32.

%description -l pl.UTF-8
GTK-- jest wrapperem C++ dla Gimp ToolKit (GTK). GTK+ jest biblioteką
służącą do tworzenia graficznych interfejsów. W pakiecie znajduje się
także biblioteka GDK-- - wrapper C++ dla GDK (General Drawing Kit).

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
Requires:	%{name}-pango-dll = %{version}-%{release}
Requires:	crossmingw32-gtk+2-dll >= 2.10.11
Requires:	wine

%description dll
DLL gtkmm libraries for Windows.

%description dll -l pl.UTF-8
Biblioteki DLL gtkmm dla Windows.

%package atk
Summary:	A C++ interface for atk library (cross mingw32 version)
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	crossmingw32-atk >= 1.18.0
Requires:	crossmingw32-glibmm >= 2.12.9

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
Requires:	crossmingw32-atk-dll >= 1.18.0
Requires:	crossmingw32-glibmm-dll >= 2.12.9
Requires:	wine

%description atk-dll
DLL atkmm library for Windows.

%description atk-dll -l pl.UTF-8
Biblioteka DLL atkmm dla Windows.

%package pango
Summary:	A C++ interface for pango library (cross mingw32 version)
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki pango (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	crossmingw32-cairomm >= 1.2.4
Requires:	crossmingw32-glibmm >= 2.12.9
Requires:	crossmingw32-pango >= 1.16.2

%description pango
A C++ interface for pango library (cross mingw32 version).

%description pango -l pl.UTF-8
Interfejs C++ dla biblioteki pango (wersja skrośna mingw32).

%package pango-static
Summary:	Static pangomm library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka pangomm (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name}-pango = %{version}-%{release}

%description pango-static
Static pangomm library (cross mingw32 version).

%description pango-static -l pl.UTF-8
Statyczna biblioteka pangomm (wersja skrośna mingw32).

%package pango-dll
Summary:	DLL pangomm library for Windows
Summary(pl.UTF-8):	Biblioteka DLL pangomm dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-cairomm-dll >= 1.2.4
Requires:	crossmingw32-glibmm-dll >= 2.12.9
Requires:	crossmingw32-pango-dll >= 1.16.2
Requires:	wine

%description pango-dll
DLL pangomm library for Windows.

%description pango-dll -l pl.UTF-8
Biblioteka DLL pangomm dla Windows.

%prep
%setup -q -n %{_realname}-%{version}

%build
export PKG_CONFIG_PATH=%{_prefix}/lib/pkgconfig
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
%{_libdir}/libg[dt]kmm-2.4.dll.a
%{_libdir}/libg[dt]kmm-2.4.la
%{_libdir}/g[dt]kmm-2.4
%{_includedir}/g[dt]kmm-2.4
%{_pkgconfigdir}/g[dt]kmm-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libg[dt]kmm-2.4.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libg[dt]kmm-2.4-*.dll

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

%files pango
%defattr(644,root,root,755)
%{_libdir}/libpangomm-1.4.dll.a
%{_libdir}/libpangomm-1.4.la
%{_includedir}/pangomm-1.4
%{_pkgconfigdir}/pangomm-1.4.pc

%files pango-static
%defattr(644,root,root,755)
%{_libdir}/libpangomm-1.4.a

%files pango-dll
%defattr(644,root,root,755)
%{_dlldir}/libpangomm-1.4-*.dll
