%define name fileschanged
%define version 0.6.5
%define release %mkrel 5

Summary: Reports when files have been altered
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: File tools
URL: http://fileschanged.sourceforge.net
Source: http://mesh.dl.sourceforge.net/sourceforge/fileschanged/%{name}-%{version}.tar.bz2
Source1: help2man
Patch0:	 fileschanged-help2man.patch
Requires: gamin 
Buildrequires: libgamin-devel
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRoot: %{_tmppath}/%{name}-buildroot


%description
This software is a client to the FAM (File Alteration Monitor) server.
Here's how the fileschanged FAM client works: 
you give it some filenames on the command line, it monitors those for changes.
When it discovers that a file has changed (or has been altered),
it displays the filename on the standard-output.

%prep
%setup -q
%patch0
install %SOURCE1 $RPM_BUILD_DIR/%{name}-%{version}/man

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc README
%{_bindir}/fileschanged
%{_datadir}/fileschanged
%{_mandir}/man1/*
%{_datadir}/info/*
%{_datadir}/locale/ca/LC_MESSAGES/fileschanged.mo
%{_datadir}/locale/es/LC_MESSAGES/fileschanged.mo


