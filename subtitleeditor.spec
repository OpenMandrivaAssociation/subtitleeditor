%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Subtitle editor
Name:		subtitleeditor
Version:	0.40.0
Release:	2
Group:		Video
License:	GPLv3+
URL:		http://home.gna.org/subtitleeditor/
Source0:	http://download.gna.org/subtitleeditor/%{url_ver}/%{name}-%{version}.tar.gz
Patch0:		subtitleeditor-0.40.0-glib-2.31.patch
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	cppunit-devel
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	enchant-devel
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	gstreamer0.10-plugins-good
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libgstreamermm-devel
Requires:	iso-codes
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-ffmpeg
Requires:	mplayer

%description
Subtitle Editor is a GTK+2 tool to edit subtitles.

It can be used for new subtitles or as a tool to transform, edit, correct and
refine existing subtitle. This program also shows sound waves, which makes it 
easier to synchronise subtitles to voices.

%prep
%setup -q
%patch0 -p1

%build
#autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

# we don't ship devel files for now
rm -f %buildroot%_libdir/{*.a,*.la,*.so}
rm -f %buildroot%_libdir/%name/plugins/*/*.la

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/subtitleeditor
%{_libdir}/*.so.*
%{_libdir}/%name
%{_datadir}/applications/subtitleeditor.desktop
%{_datadir}/subtitleeditor
%{_mandir}/man1/*.1.*
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/pixmaps/subtitleeditor.svg
