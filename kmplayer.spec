
%bcond_with koffice	# Build koffice plugin

%define		_ver		0.8.4
%define		_snap		%{nil}
%define		_rc		rc5

Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl):	Frontend dla programów MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kmplayer
Version:	%{_ver}
Release:	0.%{_rc}.0.1
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
# From kdeextragear-2 kde cvs module
#Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
Source0:        http://www.xs4all.nl/~jjvrieze/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	c15d792dc40c81a015262bad6323b053
Patch0:		%{name}-mimetypes.patch
URL:		http://www.xs4all.nl/~jjvrieze/kmplayer.html
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 9:3.1.92
%{?with_koffice:BuildRequires:	koffice-devel}
BuildRequires:	rpmbuild(macros) >= 1.129	
BuildRequires:	sed >= 4.0
BuildRequires:	xine-lib-devel >= 1:1.0	
BuildRequires:	unsermake
Requires:	kdebase-core >= 9:3.1.90
Requires:	kdelibs >= 9:3.3.0-2
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend dla programów
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
%setup -q -n %{name}-%{version}-%{_rc}

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
        src/kmplayer.desktop \

#%patch0 -p1

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs 

%configure \
	--disable-rpath \
	--enable-final \
	%{?with_koffice:--enable-koffice-plugin} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# remove bogus translation
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/xx

#%find_lang	%{name}		--with-kde	

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
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
%{_datadir}/mimelnk/video/x-ms-wmp.desktop
%{_datadir}/services/kmplayer_part.desktop
%{_datadir}/mimelnk/application/x-mplayer2.desktop
# Already in kdelibs
#%{_datadir}/mimelnk/audio/x-ms-wma.desktop
#%{_datadir}/mimelnk/video/x-ms-wmv.desktop
#%{_datadir}/services/mms.protocol
#%{_datadir}/services/pnm.protocol
#%{_datadir}/services/rtsp.protocol
%{_desktopdir}/kde/kmplayer.desktop
%{_iconsdir}/[!l]*/*/apps/kmplayer.png

%if %{with koffice}
%files koffice
%defattr(644,root,root,755)
%{_libdir}/kde3/libkmplayerkofficepart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplayerkofficepart.so
%{_datadir}/services/kmplayer_koffice.desktop
%endif
