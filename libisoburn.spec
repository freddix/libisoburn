Summary:	Multi-session filesystem extension to libisofs, libburn
Name:		libisoburn
Version:	1.3.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	7ebee7c1d4e09565daddca15467035af
Patch0:		%{name}-link.patch
URL:		http://libburnia.pykix.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libburn-devel >= 1.3.2
BuildRequires:	libisofs-devel >= 1.3.2
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libisoburn is a frontend for libraries libburn and libisofs which
enables creation and expansion of ISO-9660 filesystems on all CD/DVD
media supported by libburn. This includes media like DVD+RW, which do
not support multi-session management on media level and even plain
disk files or block devices.

The price for that is thorough specialization on data files in
ISO-9660 filesystem images. So libisoburn is not suitable for audio
(CD-DA) or any other CD layout which does not entirely consist of
ISO-9660 sessions.

%package devel
Summary:	Header files for libisoburn library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libisoburn library.

%package progs
Summary:	libisoburn programs
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description progs
Utilities creating, loading, manipulating and writing ISO 9660
filesystem images with Rock Ridge extensions.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT README TODO
%attr(755,root,root) %{_libdir}/libisoburn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libisoburn.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libisoburn.so
%{_libdir}/libisoburn.la
%{_includedir}/libisoburn
%{_pkgconfigdir}/libisoburn-1.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/osirrox
%attr(755,root,root) %{_bindir}/xorrecord
%attr(755,root,root) %{_bindir}/xorriso
%attr(755,root,root) %{_bindir}/xorrisofs
%{_mandir}/man1/xorrecord.1*
%{_mandir}/man1/xorriso*.1*

