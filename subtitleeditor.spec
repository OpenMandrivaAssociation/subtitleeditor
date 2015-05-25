%define url_ver %(echo %{version} | cut -c 1-4)
%define Werror_cflags %{nil}

Summary:	Subtitle editor
Name:		subtitleeditor
Version:	0.51.0
Release:	1
Group:		Video
License:	GPLv3+
URL:		http://home.gna.org/subtitleeditor/
Source0:	http://download.gna.org/subtitleeditor/%{url_ver}/%{name}-%{version}.tar.gz
Source1:	subtitleeditor.rpmlintrc
%if %mdvver < 201500
Patch1:		subtitleeditor-0.51.0-gtkmm-3.8.patch
%endif
Patch2:		subtitleeditor-0.51.0-memory.patch
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	cppunit-devel
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	enchant-devel
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	gstreamer1.0-plugins-good
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	pkgconfig(gstreamermm-1.0)
Requires:	iso-codes
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-libav
Requires:	mplayer

%description
Subtitle Editor is a GTK+2 tool to edit subtitles.

It can be used for new subtitles or as a tool to transform, edit, correct and
refine existing subtitle. This program also shows sound waves, which makes it 
easier to synchronise subtitles to voices.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static CFLAGS="-Wno-error"
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
%{_datadir}/appdata/subtitleeditor.appdata.xml
