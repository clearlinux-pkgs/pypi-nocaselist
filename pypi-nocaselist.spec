#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nocaselist
Version  : 1.1.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/e2/dc/d218cf3cd95a267334ad5e8e8c77138bae480fe9545a5208b782e28f3e35/nocaselist-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/dc/d218cf3cd95a267334ad5e8e8c77138bae480fe9545a5208b782e28f3e35/nocaselist-1.1.1.tar.gz
Summary  : A case-insensitive list for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-nocaselist-license = %{version}-%{release}
Requires: pypi-nocaselist-python = %{version}-%{release}
Requires: pypi-nocaselist-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
nocaselist - A case-insensitive list for Python
===============================================

%package license
Summary: license components for the pypi-nocaselist package.
Group: Default

%description license
license components for the pypi-nocaselist package.


%package python
Summary: python components for the pypi-nocaselist package.
Group: Default
Requires: pypi-nocaselist-python3 = %{version}-%{release}

%description python
python components for the pypi-nocaselist package.


%package python3
Summary: python3 components for the pypi-nocaselist package.
Group: Default
Requires: python3-core
Provides: pypi(nocaselist)
Requires: pypi(six)

%description python3
python3 components for the pypi-nocaselist package.


%prep
%setup -q -n nocaselist-1.1.1
cd %{_builddir}/nocaselist-1.1.1
pushd ..
cp -a nocaselist-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677516004
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nocaselist
cp %{_builddir}/nocaselist-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nocaselist/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nocaselist/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
