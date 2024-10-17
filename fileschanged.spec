Summary:	Reports when files have been altered
Name:		fileschanged
Version:	0.6.5
Release:	6
License:	GPLv2+
Group:		File tools
Url:		https://fileschanged.sourceforge.net
Source0:	http://mesh.dl.sourceforge.net/sourceforge/fileschanged/%{name}-%{version}.tar.bz2
BuildRequires:	help2man
BuildRequires:	pkgconfig(gamin)
Requires:	gamin

%description
This software is a client to the FAM (File Alteration Monitor) server.
Here's how the fileschanged FAM client works: 
you give it some filenames on the command line, it monitors those for changes.
When it discovers that a file has changed (or has been altered),
it displays the filename on the standard-output.

%files -f %{name}.lang
%doc README
%{_bindir}/fileschanged
%{_datadir}/fileschanged
%{_mandir}/man1/*
%{_datadir}/info/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
sed -i 's/-Werror//' src/Makefile.*
%configure2_5x
make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/%{name}/NEWS

%find_lang %{name}
