
%define		_ver		0.9
%define		_snap		040418
%define		_packager	djurban

Summary:	A KDE mplayer frontend
Summary(pl):	Frontend do mplayera pod KDE
Name:		kmplayer
Version:	%{_ver}.%{_snap}
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
# From kdeextragear-2 kde cvs module
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	66fb9824c31a93c1f60ef797e4bb2756
Patch0:		%{name}-mimetypes.patch
URL:		http://www.xs4all.nl/~jjvrieze/kmplayer.html
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 9:3.1.92
BuildRequires:	rpmbuild(macros) >= 1.129	
BuildRequires:	xine-lib-devel >= 1:1.0	
BuildRequires:	unsermake
Requires:	kdebase-core >= 9:3.1.90
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE mplayer GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do mplayera.

%package koffice
Summary:	Kmplayer integration with Koffice
Summary(pl):	Integracja kmplayera z koffice
Group:		X11/Applications/Multimedia
Requires:	koffice-common
BuildRequires:	koffice-devel

%description koffice
Kmplayer integration with Koffice.

%description koffice -l pl
Integracja kmplayera z koffice.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs 

%configure \
	--with-qt-libraries=%{_libdir} \
	--enable-koffice-plugin 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} 	

#%find_lang	%{name}		--with-kde	

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc kmplayer/{AUTHORS,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/kmplayer
%attr(755,root,root) %{_bindir}/kxineplayer
%{_libdir}/libkdeinit_kmplayer.la
%attr(755,root,root) %{_libdir}/libkdeinit_kmplayer.so
%{_libdir}/libkmplayercommon.la
%attr(755,root,root) %{_libdir}/libkmplayercommon.so
%{_libdir}/kde3/kmplayer.la
%attr(755,root,root) %{_libdir}/kde3/kmplayer.so
%{_libdir}/kde3/libkmplayerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplayerpart.so
%{_datadir}/apps/kmplayer
%{_datadir}/config/kmplayerrc
%{_datadir}/mimelnk/application/x-kmplayer.desktop
# Messing one
##%{_datadir}/mimelnk/application/x-mplayer2.desktop
##%{_datadir}/mimelnk/audio/x-ms-wma.desktop
%{_datadir}/mimelnk/video/x-ms-wmp.desktop
# Conflicts with kdelibs
#%{_datadir}/mimelnk/video/x-ms-wmv.desktop
%{_datadir}/services/kmplayer_part.desktop
%{_desktopdir}/kde/kmplayer.desktop
%{_iconsdir}/[!l]*/*/apps/kmplayer.png

%files koffice
%defattr(644,root,root,755)
%{_libdir}/kde3/libkmplayerkofficepart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplayerkofficepart.so
%{_datadir}/services/kmplayer_koffice.desktop
