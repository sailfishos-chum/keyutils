# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       keyutils

# >> macros
# << macros
%define keepstatic 1

Summary:    tools to control the key management system of the Linux kernel
Version:    1.6.3
Release:    0
Group:      Development/Libraries
License:    GPLv2
URL:        https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils
Source0:    %{name}-%{version}.tar.gz
Source100:  keyutils.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  make

%description
These tools are used to control the key management system built into the
Linux kernel.

%if "%{?vendor}" == "chum"
PackagerName: nephros
Type: console-application
Categories:
  - System
  - Library
%endif


%package doc
Summary:    Documentation files for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%package devel
Summary:    Developmemt files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# from Gentoo: usr /usr prefix. Otherwise packageconfig files will end up in /lib
sed -i \
-e '/^BUILDFOR/s:=.*:=:' \
-e "/^LIBDIR/s:=.*:= %{_libdir}:" \
-e '/^USRLIBDIR/s:=.*:=$(LIBDIR):' \
Makefile
# << build pre


make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/sbin/*
/bin/*
%{_libdir}/*.so.*
%dir %{_datadir}/%{name}
%{_sysconfdir}/*
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_mandir}/*/*
# >> files doc
# << files doc

%files devel
%defattr(-,root,root,-)
%{_datadir}/%{name}/*-debug.sh
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%attr(0644,root,root) %{_libdir}/pkgconfig/*
# >> files devel
# << files devel
