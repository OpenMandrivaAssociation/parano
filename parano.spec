%define name	parano
%define rel	1
%define version	0.3.5

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	Compute, create and edit MD5, SHA-1 and SFV files
License:	GPLv2+
Group:		File tools
URL:		http://parano.berlios.de/
Source0:	http://prdownload.berlios.de/parano/%{name}-%{version}.tar.gz
Patch0:		parano-desktop_file_fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	pygtk2.0
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
%if %mdkversion < 200900
Requires(post):	desktop-common-data
Requires(postun):	desktop-common-data
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
%endif

%description
Parano is a GNOME program to create, edit and verify hashfiles.
For now MD5, SHA-1 and SFV formats are supported.

%prep
%setup -q 
%patch0 -p0

%build
%configure2_5x --disable-update-mime-database
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -scale 48 src/parano-icon.png %{buildroot}%{_liconsdir}/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -scale 32 src/parano-icon.png %{buildroot}%{_iconsdir}/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -scale 16 src/parano-icon.png %{buildroot}%{_miconsdir}/%name.png

#remove unneeded
%{__rm} -rf %{buildroot}%{_datadir}/pixmaps/%{name}-icon.png

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_desktop_database}
%{update_menus}

%postun
%{clean_desktop_database}
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc TODO AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

