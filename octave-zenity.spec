%define octpkg zenity

Summary:	Octave functions for creating simple GUIs
Name:		octave-%{octpkg}
Version:	0.5.7
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.9

Requires:	octave(api) = %{octave_api}
Requires:	zenity >= 2.16

Requires(post): octave
Requires(postun): octave

%description
A set of functions for creating simple graphical user interfaces. It is
currently possible to create  calendar windows, text entries, file
selection dialogs, lists, message windows, icons in the notification area,
and windows for large amount of text.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

