Summary:	GNOME program for creating CDs and DVDs
Summary(pl):	Program dla GNOME do tworzenia p�yt CD i DVD
Name:		graveman
Version:	0.3.8
Release:	2
License:	GPL v.2
Group:		X11/Applications/Multimedia
Source0:	http://savannah.nongnu.org/download/graveman/%{name}-%{version}.tar.bz2
# Source0-md5:	7d40e0559f0f2c9d733196c22dd9a2d4
Patch0:		%{name}-desktop.patch
URL:		http://www.nongnu.org/graveman/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmad-devel >= 0.15
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
Requires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRAVEMAN is a frontend for cdrtools (cdrecord, readcd, mkisofs),
dvd+rw-tools and sox.

%description -l pl
GRAVEMAN jest nak�adk� na cdrtools (cdrecord, readcd, mkisofs),
dvd+rw-tools i sox.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%banner %{name} -e << EOF
Suggested packages for use with graveman:
- cdrtools
- cdrtools-mkisofs
- cdrtools-readcd
and for DVD recording
- dvd+rw-tools
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%lang(fr) %doc README.fr 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
