%global octpkg zenity

Summary:	Octave functions for creating simple GUIs
Name:		octave-%{octpkg}
Version:	0.5.7
Release:	1
Url:		https://octave.sourceforge.io/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.9

Requires:	octave(api) = %{octave_api}
Requires:	zenity

Requires(post): octave
Requires(postun): octave

%description
A set of functions for creating simple graphical user interfaces. It is
currently possible to create  calendar windows, text entries, file
selection dialogs, lists, message windows, icons in the notification area,
and windows for large amount of text.

This package is part of unmantained Octave-Forge collection.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# convert to utf8
for f in DESCRIPTION inst/*m
do
	iconv -f ISO-8859-1 -t UTF-8 -o "${f}".utf8 "${f}"
	mv ${f}.utf8 ${f}
done

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

