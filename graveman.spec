Summary:	GTK+2 program for creating CDs and DVDs
Summary(pl):	Oparty o GTK+2 program do tworzenia p³yt CD i DVD
Name:		graveman
Version:	0.3.11
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://graveman.tuxfamily.org/%{name}-%{version}.tar.bz2
# Source0-md5:	06dfb5c9599fe90ed6e5c8c8c1c35dca
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
URL:		http://graveman.tuxfamily.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmad-devel >= 0.15
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GRAVEMAN is a frontend for cdrtools (cdrecord, readcd, mkisofs),
dvd+rw-tools and sox.

%description -l pl
GRAVEMAN jest nak³adk± na cdrtools (cdrecord, readcd, mkisofs),
dvd+rw-tools i sox.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

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
for CD recording
- cdrdao
- cdrtools
- cdrtools-mkisofs
- cdrtools-readcd
for DVD recording
- dvd+rw-tools
for operations on audio files
- sox
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
%{_mandir}/
%{_pixmapsdir}/*
