#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyroute2.ethtool
Version  : 0.6.11
Release  : 17
URL      : https://files.pythonhosted.org/packages/4e/6c/702dbfb51cfc0e49dbf5985686dcb091a5d9e2575ed2b3cfb9e40628fc02/pyroute2.ethtool-0.6.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/6c/702dbfb51cfc0e49dbf5985686dcb091a5d9e2575ed2b3cfb9e40628fc02/pyroute2.ethtool-0.6.11.tar.gz
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
%setup -q -n pyroute2.ethtool-0.6.11
cd %{_builddir}/pyroute2.ethtool-0.6.11
pushd ..
cp -a pyroute2.ethtool-0.6.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654547574
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ethtool
cp %{_builddir}/pyroute2.ethtool-0.6.11/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ethtool/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.ethtool-0.6.11/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pypi-pyroute2.ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
