#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x51722B08FE4745A2 (simon@josefsson.org)
#
Name     : libtasn1
Version  : 4.19.0
Release  : 41
URL      : https://mirrors.kernel.org/gnu/libtasn1/libtasn1-4.19.0.tar.gz
Source0  : https://mirrors.kernel.org/gnu/libtasn1/libtasn1-4.19.0.tar.gz
Source1  : https://mirrors.kernel.org/gnu/libtasn1/libtasn1-4.19.0.tar.gz.sig
Summary  : Library for ASN.1 and DER manipulation
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 LGPL-2.1 LGPL-2.1+
Requires: libtasn1-bin = %{version}-%{release}
Requires: libtasn1-info = %{version}-%{release}
Requires: libtasn1-lib = %{version}-%{release}
Requires: libtasn1-license = %{version}-%{release}
Requires: libtasn1-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : valgrind

%description
This is GNU Libtasn1, a small ASN.1 library.
The C library (libtasn1.*) is licensed under the GNU Lesser General
Public License version 2.1 or later.  See the file COPYING.LIB.

%package bin
Summary: bin components for the libtasn1 package.
Group: Binaries
Requires: libtasn1-license = %{version}-%{release}

%description bin
bin components for the libtasn1 package.


%package dev
Summary: dev components for the libtasn1 package.
Group: Development
Requires: libtasn1-lib = %{version}-%{release}
Requires: libtasn1-bin = %{version}-%{release}
Provides: libtasn1-devel = %{version}-%{release}
Requires: libtasn1 = %{version}-%{release}

%description dev
dev components for the libtasn1 package.


%package dev32
Summary: dev32 components for the libtasn1 package.
Group: Default
Requires: libtasn1-lib32 = %{version}-%{release}
Requires: libtasn1-bin = %{version}-%{release}
Requires: libtasn1-dev = %{version}-%{release}

%description dev32
dev32 components for the libtasn1 package.


%package info
Summary: info components for the libtasn1 package.
Group: Default

%description info
info components for the libtasn1 package.


%package lib
Summary: lib components for the libtasn1 package.
Group: Libraries
Requires: libtasn1-license = %{version}-%{release}

%description lib
lib components for the libtasn1 package.


%package lib32
Summary: lib32 components for the libtasn1 package.
Group: Default
Requires: libtasn1-license = %{version}-%{release}

%description lib32
lib32 components for the libtasn1 package.


%package license
Summary: license components for the libtasn1 package.
Group: Default

%description license
license components for the libtasn1 package.


%package man
Summary: man components for the libtasn1 package.
Group: Default

%description man
man components for the libtasn1 package.


%prep
%setup -q -n libtasn1-4.19.0
cd %{_builddir}/libtasn1-4.19.0
pushd ..
cp -a libtasn1-4.19.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664932091
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1664932091
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libtasn1
cp %{_builddir}/libtasn1-%{version}/doc/COPYING %{buildroot}/usr/share/package-licenses/libtasn1/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/libtasn1-%{version}/doc/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libtasn1/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asn1Coding
/usr/bin/asn1Decoding
/usr/bin/asn1Parser

%files dev
%defattr(-,root,root,-)
/usr/include/libtasn1.h
/usr/lib64/libtasn1.so
/usr/lib64/pkgconfig/libtasn1.pc
/usr/share/man/man3/asn1_array2tree.3
/usr/share/man/man3/asn1_bit_der.3
/usr/share/man/man3/asn1_check_version.3
/usr/share/man/man3/asn1_copy_node.3
/usr/share/man/man3/asn1_create_element.3
/usr/share/man/man3/asn1_decode_simple_ber.3
/usr/share/man/man3/asn1_decode_simple_der.3
/usr/share/man/man3/asn1_delete_element.3
/usr/share/man/man3/asn1_delete_structure.3
/usr/share/man/man3/asn1_delete_structure2.3
/usr/share/man/man3/asn1_der_coding.3
/usr/share/man/man3/asn1_der_decoding.3
/usr/share/man/man3/asn1_der_decoding2.3
/usr/share/man/man3/asn1_der_decoding_element.3
/usr/share/man/man3/asn1_der_decoding_startEnd.3
/usr/share/man/man3/asn1_dup_node.3
/usr/share/man/man3/asn1_encode_simple_der.3
/usr/share/man/man3/asn1_expand_any_defined_by.3
/usr/share/man/man3/asn1_expand_octet_string.3
/usr/share/man/man3/asn1_find_node.3
/usr/share/man/man3/asn1_find_structure_from_oid.3
/usr/share/man/man3/asn1_get_bit_der.3
/usr/share/man/man3/asn1_get_length_ber.3
/usr/share/man/man3/asn1_get_length_der.3
/usr/share/man/man3/asn1_get_object_id_der.3
/usr/share/man/man3/asn1_get_octet_der.3
/usr/share/man/man3/asn1_get_tag_der.3
/usr/share/man/man3/asn1_length_der.3
/usr/share/man/man3/asn1_number_of_elements.3
/usr/share/man/man3/asn1_object_id_der.3
/usr/share/man/man3/asn1_octet_der.3
/usr/share/man/man3/asn1_parser2array.3
/usr/share/man/man3/asn1_parser2tree.3
/usr/share/man/man3/asn1_perror.3
/usr/share/man/man3/asn1_print_structure.3
/usr/share/man/man3/asn1_read_node_value.3
/usr/share/man/man3/asn1_read_tag.3
/usr/share/man/man3/asn1_read_value.3
/usr/share/man/man3/asn1_read_value_type.3
/usr/share/man/man3/asn1_strerror.3
/usr/share/man/man3/asn1_write_value.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.so
/usr/lib32/pkgconfig/32libtasn1.pc
/usr/lib32/pkgconfig/libtasn1.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libtasn1.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtasn1.so.6
/usr/lib64/libtasn1.so.6.6.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtasn1.so.6
/usr/lib32/libtasn1.so.6.6.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libtasn1/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libtasn1/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/asn1Coding.1
/usr/share/man/man1/asn1Decoding.1
/usr/share/man/man1/asn1Parser.1
