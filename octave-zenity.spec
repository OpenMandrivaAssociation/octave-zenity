%define	pkgname zenity

Summary:	Octave functions for creating simple GUIs
Name:       octave-%{pkgname}
Version:	0.5.7
Release:	4
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/zenity/
Requires:	zenity >= 2.16
BuildRequires:  octave-devel >= 2.9.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
This package provides a set of Octave functions for creating simple
graphical user interfaces. It is currently possible to create calendar
windows, text entries, file selection dialogs, lists, message windows,
icons in the notification area, and windows for large amount of text.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"
touch %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/packinfo/.autoload
chmod 644 %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/packinfo/.autoload

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
