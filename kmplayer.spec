#
# Conditional build:
%bcond_with	koffice		# Build koffice plugin
#
Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl.UTF-8):	Frontend dla programów MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kmplayer
Version:	0.11.3c
Release:	0.1
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kmplayer.kde.org/pkgs/%{name}-%{version}.tar.bz2
# Source0-md5:	3e9ef221ca15d264e553706c6e611eb9
URL:		http://kmplayer.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	dbus-glib-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+2-devel
BuildRequires:	kde4-kdelibs-devel
%{?with_koffice:BuildRequires:	koffice-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	xulrunner-devel
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l pl.UTF-8
W pełni zintegrowany z KDE frontend dla programów
MPlayer/Xine/ffmpeg/ffserver/VDR.

%package koffice
Summary:	Kmplayer integration with Koffice
Summary(pl.UTF-8):	Integracja kmplayera z koffice
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	koffice-common

%description koffice
Kmplayer integration with Koffice.

%description koffice -l pl.UTF-8
Integracja kmplayera z koffice.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
		.. \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/kmplayer
%attr(755,root,root) %{_bindir}/knpplayer
%attr(755,root,root) %{_bindir}/kphononplayer
%attr(755,root,root) %{_libdir}/kde4/libkmplayerpart.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kmplayer.so
%attr(755,root,root) %{_libdir}/libkmplayercommon.so
%{_desktopdir}/kde4/kmplayer.desktop
%{_docdir}/kde/HTML/en/kmplayer/common
%{_docdir}/kde/HTML/en/kmplayer/index.cache.bz2
%{_docdir}/kde/HTML/en/kmplayer/index.docbook
%{_datadir}/kde4/services/kmplayer_part.desktop
%{_datadir}/apps/kmplayer
%{_datadir}/config/kmplayerrc
%{_iconsdir}/[!l]*/*/apps/kmplayer.*

%if %{with koffice}
%files koffice
%defattr(644,root,root,755)
%{_libdir}/kde3/libkmplayerkofficepart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplayerkofficepart.so
%{_datadir}/services/kmplayer_koffice.desktop
%endif
