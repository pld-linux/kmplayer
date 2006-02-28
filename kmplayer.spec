
%bcond_without	gstreamer	# Do not build kgstplayer
%bcond_with	koffice		# Build koffice plugin
%bcond_without	xine		# Do not build kxineplayer

Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl):	Frontend dla program�w MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kmplayer
Version:	0.9.1b
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kmplayer.kde.org/pkgs/%{name}-%{version}.tar.bz2
# Source0-md5:	dd9930c64757b553ff32705b5218ba05
#Patch0:		%{name}-mimetypes.patch
URL:		http://kmplayer.kde.org/
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-devel >= 0.8.6}
BuildRequires:	kdelibs-devel >= 9:3.1.92
%{?with_koffice:BuildRequires:	koffice-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake
%{?with_xine:BuildRequires:	xine-lib-devel >= 1:1.0}
Requires:	kdebase-core >= 9:3.1.90
Requires:	kdelibs >= 9:3.4.0-4
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l pl
W pe�ni zintegrowany z KDE frontend dla program�w
MPlayer/Xine/ffmpeg/ffserver/VDR.

%package koffice
Summary:	Kmplayer integration with Koffice
Summary(pl):	Integracja kmplayera z koffice
Group:		X11/Applications/Multimedia
Requires:	koffice-common

%description koffice
Kmplayer integration with Koffice.

%description koffice -l pl
Integracja kmplayera z koffice.

%prep
%setup -q

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
        src/kmplayer.desktop \

#%patch0 -p1

%build
cp /usr/share/automake/config.sub admin

#%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	%{?with_koffice:--enable-koffice-plugin} \
	%{!?with_gstreamer:--without-gstreamer} \
	%{!?with_xine:--without-xine} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# remove bogus translation
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx

# already in kdelibs
rm $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-mplayer2.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{?with_gstreamer:%attr(755,root,root) %{_bindir}/kgstplayer}
%attr(755,root,root) %{_bindir}/kmplayer
%{?with_xine:%attr(755,root,root) %{_bindir}/kxineplayer}
%attr(755,root,root) %{_bindir}/kxvplayer
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
%{_datadir}/mimelnk/video/x-ms-wmp.desktop
%{_datadir}/services/kmplayer_part.desktop
%{_desktopdir}/kde/kmplayer.desktop
%{_iconsdir}/[!l]*/*/apps/kmplayer.*

%if %{with koffice}
%files koffice
%defattr(644,root,root,755)
%{_libdir}/kde3/libkmplayerkofficepart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplayerkofficepart.so
%{_datadir}/services/kmplayer_koffice.desktop
%endif
