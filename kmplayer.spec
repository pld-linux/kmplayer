
%define		_ver	0.8.1
%define		_snap	031116

Summary:	A KDE mplayer frontend
Summary(pl):	Frontend do mplayera pod KDE
Name:		kmplayer
Version:	0.8.1.%{_snap}
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
# From kdeextragear-2 kde cvs module
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	8da645769c01f725d41e6403f0873258
Patch0:		%{name}-mimetypes.patch
URL:		http://www.xs4all.nl/~jjvrieze/kmplayer.html
BuildRequires:	kdelibs-devel >= 9:3.1.92
BuildRequires:	rpmbuild(macros) >= 1.129	
BuildRequires:	xine-lib-devel >= 1:1.0	
Requires:	kdebase-core >= 9:3.1.90
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE mplayer GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do mplayera.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build

%{__make} -f admin/Makefile.common cvs 

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} 	

#%%find_lang	%{name}		--with-kde	

%clean
rm -rf $RPM_BUILD_ROOT

%files
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
# Messing one
#%{_datadir}/mimelnk/application/x-mplayer2.desktop
%{_datadir}/mimelnk/audio/x-ms-wma.desktop
%{_datadir}/mimelnk/video/x-ms-wmp.desktop
# Conflicts with kdelibs
#%{_datadir}/mimelnk/video/x-ms-wmv.desktop
%{_datadir}/services/kmplayer_component.desktop
#%{_datadir}/services/kmplayer_koffice.desktop
%{_desktopdir}/kde/kmplayer.desktop
%{_iconsdir}/[!l]*/*/apps/kmplayer.png
