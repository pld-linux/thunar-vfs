#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		xfce_version	4.8.0
Summary:	Thunar VFS library
Summary(pl.UTF-8):	Biblioteka Thunar VFS
Name:		thunar-vfs
Version:	1.2.0
Release:	1
License:	GPL v2 / LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/thunar-vfs/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	1fbc55af8ed98174f5c3c7f8daec10cc
URL:		http://thunar.xfce.org/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	gamin-devel >= 0.1.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	hal-devel > 0.5.0
BuildRequires:	intltool
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.12
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.8.0
Requires:	exo >= 0.6.0
Requires:	shared-mime-info >= 0.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thunar VFS library.

%description -l pl.UTF-8
Biblioteka Thunar VFS.

%package apidocs
Summary:	Thunar VFS library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Thunar VFS
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Thunar VFS library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Thunar VFS.

%package devel
Summary:	Header files for Thunar VFS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Thunar VFS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exo-devel >= 0.6.0
Requires:	glib2-devel >= 1:2.12.4

%description devel
This is the package containing the header files for Thunar VFS
library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki Thunar VFS.

%package static
Summary:	Static Thunar VFS library
Summary(pl.UTF-8):	Statyczna biblioteka Thunar VFS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Thunar VFS library.

%description static -l pl.UTF-8
Statyczna biblioteka Thunar VFS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--enable-dbus \
	--enable-gnome-thumbnailers \
	--enable-gtk-doc \
	--enable-startup-notification \
	--with-html-dir=%{_gtkdocdir} \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libthunar-vfs-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthunar-vfs-1.so.2
%dir %{_libdir}/thunar-vfs-1
%attr(755,root,root) %{_libdir}/thunar-vfs-1/thunar-vfs-font-thumbnailer-1
%attr(755,root,root) %{_libdir}/thunar-vfs-1/thunar-vfs-mime-cleaner-1
%attr(755,root,root) %{_libdir}/thunar-vfs-1/thunar-vfs-pixbuf-thumbnailer-1
%attr(755,root,root) %{_libdir}/thunar-vfs-1/thunar-vfs-update-thumbnailers-cache-1
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/thunar-vfs-font-thumbnailer-1.desktop
%{_docdir}/thunar-vfs

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/thunar-vfs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libthunar-vfs-1.so
%{_includedir}/thunar-vfs-1
%{_pkgconfigdir}/thunar-vfs-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libthunar-vfs-1.a
%endif
