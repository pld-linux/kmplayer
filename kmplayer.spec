
Summary:	A KDE mplayer frontend
Summary(pl):	Frontend do mplayera pod KDE
Name:		kmplayer
Version:	0.7.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.xs4all.nl/~jjvrieze/%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
URL:		http://www.xs4all.nl/~jjvrieze/kmplayer.html
BuildRequires:	kdelibs-devel >= 3.1	
BuildRequires:	mplayer
Requires:	mplayer
Requires:	kdelibs >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
A powerful, fully integrated with KDE mplayer GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do mplayera.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/kmplayer.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

%find_lang	%{name}		--with-kde	

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplayer
%{_libdir}/kde3/kparts_kmplayer.la
%attr(755,root,root) %{_libdir}/kde3/kparts_kmplayer.so
%{_libdir}/kdeinit_kmplayer.la
%attr(755,root,root) %{_libdir}/kdeinit_kmplayer.so
%{_datadir}/apps/kmplayer
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/video/x-ms-wmv.desktop
%{_datadir}/services/kmplayer_component.desktop
%{_desktopdir}/kmplayer.desktop
%{_pixmapsdir}/[!l]*/*/apps/kmplayer.png
