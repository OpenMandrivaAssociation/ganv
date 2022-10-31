%define _empty_manifest_terminate_build 0

%define major 1

%define libname %mklibname ganv %{major}
%define develname %mklibname ganv -d

Name:           ganv
Version:        1.8.2
Release:        1
Summary:        Interactive Gtk canvas widget for graph-based interfaces
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            http://drobilla.net/software/ganv
Source0:        http://download.drobilla.net/ganv-%{version}.tar.bz2

BuildRequires:  python
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(libgvc)

Requires:	      %{libname} =  %{EVRD}

%description
Ganv is an interactive Gtk canvas widget for graph-based interfaces (patchers, modular synthesizers, finite state automata, interactive graphs, etc).


%package -n %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
%{name} shared library.


%package -n     %{develname}
Summary:        Development packages for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} =  %{EVRD}
Requires:	      %{libname} =  %{EVRD}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
./waf --libdir=%{_libdir} --prefix=%{_prefix} configure
./waf

%install
./waf --destdir=%{buildroot} install
install -d %{buildroot}%{_libdir}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc NEWS
%license COPYING
%{_bindir}/ganv_bench

%files -n %{libname}
%{_libdir}/lib%{name}-%{major}.so.*

%files -n %{develname}
%doc README.md
%license COPYING
%{_includedir}/%{name}-%{major}
%{_libdir}/lib%{name}-%{major}.so
%{_libdir}/pkgconfig/*.pc
