Summary:	A KDE mplayer frontend
Summary(pl):	Frontend do mplayera pod KDE
Name:		kmplayer
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
#Icon:		-
Source0:	http://www.xs4all.nl/~jjvrieze/%{name}-%{version}.tar.bz2
URL:		http://www.xs4all.nl/~jjvrieze/kmplayer.html
BuildRequires:	kdelibs-devel >= 3.1	
BuildRequires:	arts >= 1.0
BuildRequires:	mplayer
Requires:	mplayer
Requires:	kdelibs >= 3.1
Requires:	arts >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		%{_usr}/X11R6

%description
A powerful, fully integrated with KDE mplayer GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do mplayera.

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/en/index.docbook
%attr(755,root,root) %{_bindir}/kmplayer
%{_libdir}/kde3/kparts_kmplayer.la
%attr(755,root,root) %{_libdir}/kde3/kparts_kmplayer.so
%{_libdir}/kdeinit_kmplayer.la
%attr(755,root,root) %{_libdir}/kdeinit_kmplayer.so
%{_applnkdir}/Multimedia/kmplayer.desktop
%{_datadir}/apps/kmplayer
%{_datadir}/mimelnk/application/x-applix.desktop
%{_datadir}/mimelnk/application/x-mplayer2.desktop
%{_datadir}/mimelnk/video/x-ms-wmv.desktop
%{_datadir}/services/kmplayer_component.desktop
