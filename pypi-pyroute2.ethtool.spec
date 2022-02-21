#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyroute2.ethtool
Version  : 0.6.7
Release  : 13
URL      : https://files.pythonhosted.org/packages/bf/6b/3f2f2625507fdc207eb7ccce9b63f1d9273927ff8f4d2eac3aa12f6cc37d/pyroute2.ethtool-0.6.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/6b/3f2f2625507fdc207eb7ccce9b63f1d9273927ff8f4d2eac3aa12f6cc37d/pyroute2.ethtool-0.6.7.tar.gz
Summary  : Python Netlink library: ethtool
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pypi-pyroute2.ethtool-license = %{version}-%{release}
Requires: pypi-pyroute2.ethtool-python = %{version}-%{release}
Requires: pypi-pyroute2.ethtool-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyroute2.core)

%description
pyroute2.ethtool
================
PyRoute2 is a pure Python **netlink** library.

%package license
Summary: license components for the pypi-pyroute2.ethtool package.
Group: Default

%description license
license components for the pypi-pyroute2.ethtool package.


%package python
Summary: python components for the pypi-pyroute2.ethtool package.
Group: Default
Requires: pypi-pyroute2.ethtool-python3 = %{version}-%{release}

%description python
python components for the pypi-pyroute2.ethtool package.


%package python3
Summary: python3 components for the pypi-pyroute2.ethtool package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2.ethtool)
Requires: pypi(pyroute2.core)

%description python3
python3 components for the pypi-pyroute2.ethtool package.


%prep
%setup -q -n pyroute2.ethtool-0.6.7
cd %{_builddir}/pyroute2.ethtool-0.6.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645464482
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ethtool
cp %{_builddir}/pyroute2.ethtool-0.6.7/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ethtool/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.ethtool-0.6.7/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyroute2.ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pypi-pyroute2.ethtool/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*