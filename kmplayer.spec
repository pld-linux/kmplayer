
Summary:	A KDE mplayer frontend
Summary(pl):	Frontend do mplayera pod KDE
Name:		kmplayer
Version:	0.8a
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.xs4all.nl/~jjvrieze/%{name}-%{version}.tar.bz2
# Source0-md5:	c385b3bcb4b0c9be82be525cd6e9413a
Patch0:		%{name}-desktop.patch
URL:		http://www.xs4all.nl/~jjvrieze/kmplayer.html
BuildRequires:	kdelibs-devel >= 3.1	
BuildRequires:	mplayer
Requires:	mplayer
Requires:	kdebase-core >= 9:3.1.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML
%define         _icondir        %{_datadir}/icons

%description
A powerful, fully integrated with KDE mplayer GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do mplayera.

%prep
%setup -q -n %{name}
%patch0 -p1

%build

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
        kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir} 	

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/kmplayer.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

%find_lang	%{name}		--with-kde	

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
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
%{_datadir}/mimelnk/application/x-mplayer2.desktop
# Conflict with kdelibs
#%{_datadir}/mimelnk/video/x-ms-asf.desktop
#%{_datadir}/mimelnk/video/x-ms-wmp.desktop
#%{_datadir}/mimelnk/video/x-ms-wmv.desktop
#
%{_datadir}/services/kmplayer_component.desktop
#%{_datadir}/services/kmplayer_koffice.desktop
%{_desktopdir}/kmplayer.desktop
%{_icondir}/[!l]*/*/apps/kmplayer.png
