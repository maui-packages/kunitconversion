# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kunitconversion

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 addon for unit conversions
Version:    5.2.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kunitconversion.yaml
Source101:  kunitconversion-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  ki18n-devel
BuildRequires:  kconfig-devel

%description
KDE Frameworks 5 Tier 3 addon for unit conversions


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kconfig-devel
Requires:   ki18n-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5UnitConversion.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kunitconversion_version.h
%{_kf5_includedir}/KUnitConversion
%{_kf5_libdir}/libKF5UnitConversion.so
%{_kf5_cmakedir}/KF5UnitConversion
%{_kf5_mkspecsdir}/qt_KUnitConversion.pri
# >> files devel
# << files devel
