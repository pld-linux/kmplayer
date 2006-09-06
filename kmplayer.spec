
%bcond_without	gstreamer	# Do not build kgstplayer
%bcond_with	koffice		# Build koffice plugin
%bcond_without	xine		# Do not build kxineplayer

%define		_pre	rc1
Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl):	Frontend dla programów MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kmplayer
Version:	0.9.3
Release:	0.%{_pre}.1
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
# http://kmplayer.kde.org/pkgs/kmplayer-0.9.3-pre1.tar.bz2
Source0:	http://kmplayer.kde.org/pkgs/%{name}-%{version}-%{_pre}.tar.bz2
# Source0-md5:	2a2d2cebe1bcbde8dd25d0c0476d8bc2
#Patch0:		%{name}-mimetypes.patch
Patch0:		%{name}-video-size.patch
URL:		http://kmplayer.kde.org/
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0}
BuildRequires:	kdelibs-devel >= 9:3.5.3
%{?with_koffice:BuildRequires:	koffice-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake
%{?with_xine:BuildRequires:	xine-lib-devel >= 1:1.0}
Requires:	kdebase-core >= 9:3.5.3
Requires:	kdelibs >= 9:3.5.3
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend dla programów
MPlayer/Xine/ffmpeg/ffserver/VDR.

%package gstreamer
Summary:	Gstreamer wrapper
Summary(pl):	Wrapper gstreamera
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gstreamer
Gstreamer wrapper.

%description gstreamer -l pl
Wrapper gstreamera.

%package koffice
Summary:	Kmplayer integration with Koffice
Summary(pl):	Integracja kmplayera z koffice
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	koffice-common

%description koffice
Kmplayer integration with Koffice.

%description koffice -l pl
Integracja kmplayera z koffice.

%package xine
Summary:	Xine wrapper
Summary(pl):	Wrapper xine
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description xine
Xine wrapper.

%description xine -l pl
Wrapper xine.

%prep
%setup -q -n %{name}-%{version}-%{_pre}
#%%patch0 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
        src/kmplayer.desktop \


%build
cp /usr/share/automake/config.sub admin
%{__autoconf}

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
%attr(755,root,root) %{_bindir}/kmplayer
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

%if %{with gstreamer}
%files gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgstplayer
%endif

%if %{with koffice}
%files koffice
%defattr(644,root,root,755)
%{_libdir}/kde3/libkmplayerkofficepart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplayerkofficepart.so
%{_datadir}/services/kmplayer_koffice.desktop
%endif

%if %{with xine}
%files xine
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxineplayer
%endif
