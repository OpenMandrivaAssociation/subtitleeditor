%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Subtitle editor
Name:		subtitleeditor
Version:	0.35.1
Release:	%mkrel 1
Group:		Video
License:	GPLv3+
URL:		http://home.gna.org/subtitleeditor/
Source:		http://download.gna.org/subtitleeditor/%{url_ver}/%{name}-%{version}.tar.gz
Patch0:		subtitleeditor-0.30.0-fix-linkage.patch
BuildRequires:	libglademm-devel
BuildRequires:	cppunit-devel
BuildRequires:	libxml++-devel
BuildRequires:	enchant-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	gstreamer0.10-plugins-good
BuildRequires:	pcre-devel
BuildRequires:	libxml2-devel
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libgstreamermm-devel
Requires:	iso-codes
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-ffmpeg
Requires:	mplayer
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Subtitle Editor is a GTK+2 tool to edit subtitles.

It can be used for new subtitles or as a tool to transform, edit, correct and
refine existing subtitle. This program also shows sound waves, which makes it 
easier to synchronise subtitles to voices.

%prep
%setup -q
#patch0 -p0

%build
#autoreconf -fi
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

# we don't ship devel files for now
rm -f %buildroot%_libdir/{*.a,*.la,*.so}
rm -f %buildroot%_libdir/%name/plugins/*/*.la

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/subtitleeditor
%{_libdir}/*.so.*
%{_libdir}/%name
%{_datadir}/applications/subtitleeditor.desktop
%{_datadir}/subtitleeditor
%{_mandir}/man1/*.1.*
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/pixmaps/subtitleeditor.svg
