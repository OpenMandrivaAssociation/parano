%define name	parano
%define rel	3
%define version	0.3.5

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	Compute, create and edit MD5, SHA-1 and SFV files
License:	GPLv2+
Group:		File tools
URL:		https://parano.berlios.de/
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


%changelog
* Tue Jan 18 2011 Jani Välimaa <wally@mandriva.org> 0.3.5-3mdv2011.0
+ Revision: 631614
- drop support for old mdv releases

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sat Jun 06 2009 Jani Välimaa <wally@mandriva.org> 0.3.5-1mdv2010.0
+ Revision: 383392
- imported package parano


