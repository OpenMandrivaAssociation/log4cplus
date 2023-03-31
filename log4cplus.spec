%define major 3
%define libname %mklibname log4cplus
%define devname %mklibname log4cplus -d

Name: log4cplus
Version: 2.0.8
Release: 2
Source0: https://github.com/log4cplus/log4cplus/releases/download/REL_%(echo %{version}|sed -e 's,\.,_,g')/log4cplus-%{version}.tar.xz
Summary: C++17 logging library
URL: https://github.com/log4cplus/log4cplus
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja

%description
log4cplus is a simple to use C++17 logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.

It is modeled after the Java log4j API.

%package -n %{libname}
Summary: C++17 logging library
Group: System/Libraries

%description -n %{libname}
log4cplus is a simple to use C++17 logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.

It is modeled after the Java log4j API.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

log4cplus is a simple to use C++17 logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.

It is modeled after the Java log4j API.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
