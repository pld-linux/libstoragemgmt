#
# Conditional build:
%bcond_without	python2	# CPython 2.x support
%bcond_without	python3	# CPython 3.x support
%bcond_with	tests	# tests

Summary:	Storage array management library
Summary(pl.UTF-8):	Biblioteka do zarządzania macierzami dyskowymi
Name:		libstoragemgmt
Version:	1.9.8
Release:	3
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/libstorage/libstoragemgmt/releases
Source0:	https://github.com/libstorage/libstoragemgmt/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0608b44ce238221ae1dff75bf3e6ff2c
Patch0:		%{name}-types.patch
URL:		https://github.com/libstorage/libstoragemgmt
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.22.5
BuildRequires:	libconfig-devel >= 1.3.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	perl-base
BuildRequires:	openssl-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	systemd-devel
BuildRequires:	systemd-units
BuildRequires:	pkgconfig
BuildRequires:	procps
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-six
BuildRequires:	python-pywbem
%endif
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pywbem
BuildRequires:	python3-six
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.043
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	systemd-devel
BuildRequires:	udev-devel
%if %{with tests}
BuildRequires:	check-devel >= 0.9.8
BuildRequires:	chrpath
BuildRequires:	valgrind
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libStorageMgmt library will provide a vendor agnostic open source
storage application programming interface (API) that will allow
management of storage arrays. The library includes a command line
interface for interactive use and scripting (command lsmcli). The
library also has a daemon that is used for executing plug-ins in a
separate process (lsmd).

%description -l pl.UTF-8
Biblioteka libStorageMgmt ma na celu udostępnienie niezależnego od
producenta, mającego otwarte źródła API, pozwalającego na operowanie
na macierzach dyskowych. Biblioteka zawiera interfejs linii poleceń
do użycia interaktywnego i w skryptach (polecenie lsmcli). Ma także
demona, używanego przy uruchamianiu wtyczek w osobnym procesie (lsmd).

%package -n bash-completion-libstoragemgmt
Summary:	Bash completion for lsmcli command
Summary(pl.UTF-8):	Bashowe uzupełnianie składni polecenia lsmcli
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-libstoragemgmt
Bash completion for lsmcli command.

%description -n bash-completion-libstoragemgmt -l pl.UTF-8
Bashowe uzupełnianie składni polecenia lsmcli.

%package daemon
Summary:	libStorageMgmt daemon
Summary(pl.UTF-8):	Demon libStorageMgmt
Group:		Daemons
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires:	%{name} = %{version}-%{release}
Requires:	python3-%{name} = %{version}-%{release}
Requires:	systemd-units
Provides:	group(libstoragemgmt)
Provides:	user(libstoragemgmt)
Obsoletes:	libstoragemgmt-netapp-plugin < 1.9.4
Obsoletes:	libstoragemgmt-nstor-plugin < 1.9.4
Obsoletes:	libstoragemgmt-udev < 1.9.4

%description daemon
libStorageMgmt daemon.

%description daemon -l pl.UTF-8
Demon libStorageMgmt.

%package devel
Summary:	Development files for libStorageMgmt
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libStorageMgmt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for developing applications that
use libStorageMgmt.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących libStorageMgmt.

%package -n python-%{name}
Summary:	Python 2 client libraries and plug-in support for libStorageMgmt
Summary(pl.UTF-8):	Biblioteki klienckie Pythona 2 oraz obsługa wtyczek libStorageMgmt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-libstoragemgmt-clibs < 1.9.4
Obsoletes:	libstoragemgmt-python-clibs < 1.9

%description -n python-%{name}
This package contains Python client libraries as well as Python
framework support and open source plug-ins written in Python.

%description -n python-%{name} -l pl.UTF-8
Ten pakiet zawiera biblioteki klienckie Pythona oraz obsługę
szkieletu wraz z wtyczkami napisanymi w Pythonie.

%package -n python3-%{name}
Summary:	Python 3 client libraries and plug-in support for libStorageMgmt
Summary(pl.UTF-8):	Biblioteki klienckie Pythona 3 oraz obsługa wtyczek libStorageMgmt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python3-libstoragemgmt-clibs < 1.9.4

%description -n python3-%{name}
This package contains Python client libraries as well as Python
framework support and open source plug-ins written in Python.

%description -n python3-%{name} -l pl.UTF-8
Ten pakiet zawiera biblioteki klienckie Pythona oraz obsługę
szkieletu wraz z wtyczkami napisanymi w Pythonie.

%package plugin-arcconf
Summary:	Files for Microsemi Adaptec and Smart Family support for libStorageMgmt
Summary(pl.UTF-8):	Pliki obsługi macierzy rodziny Microsemi Adaptec i Smart dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Obsoletes:	libstoragemgmt-arcconf-plugin < 1.9.4
BuildArch:	noarch

%description plugin-arcconf
This package contains the plugin for Microsemi Adaptec RAID and Smart
Family Controller storage management.

%description plugin-arcconf -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zarządzania macierzami rodziny Microsemi
Adaptec RAID i Smart.

%package plugin-hpsa
Summary:	Files for HP SmartArray array support for libStorageMgmt
Summary(pl.UTF-8):	Pliki obsługi macierzy HP SmartArray dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Obsoletes:	libstoragemgmt-hpsa-plugin < 1.9.4
BuildArch:	noarch

%description plugin-hpsa
This package contains the plugin for HP SmartArray storage management
via hpssacli.

%description plugin-hpsa -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zarządzania macierzami HP SmartArray
poprzez hpssacli.

%package plugin-local
Summary:	Files for local pseudo plugin of libStorageMgmt
Summary(pl.UTF-8):	Pliki lokalnej pseudo wtyczki dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Obsoletes:	libstoragemgmt-local-plugin < 1.9.4
BuildArch:	noarch

%description plugin-local
This is a plugin that provides auto plugin selection for locally
managed storage.

%description plugin-local -l pl.UTF-8
Ten pakiet zawiera wtyczkę zapewniającą automatyczny wybór wtyczki dla
lokalnie zarządzanej przestrzeni dyskowej.

%package plugin-megaraid
Summary:	Files for LSI MegaRAID array support for libStorageMgmt
Summary(pl.UTF-8):	Pliki obsługi macierzy LSI MegaRAID dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Obsoletes:	libstoragemgmt-megaraid-plugin < 1.9.4
BuildArch:	noarch

%description plugin-megaraid
This package contains the plugin for LSI MegaRAID storage management
via storcli.

%description plugin-megaraid -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zarządzania macierzami LSI MegaRAID
poprzez storcli.

%package plugin-nfs
Summary:	Files for NFS local filesystem support for libStorageMgmt
Summary(pl.UTF-8):	Pliki do lokalnej obsługi systemu plików NFS dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Requires:	nfs-utils
Obsoletes:	libstoragemgmt-nfs-plugin < 1.9.4
Obsoletes:	libstoragemgmt-nfs-plugin-clibs < 1.9.4

%description plugin-nfs
This package contains plug-in for local NFS exports support.

%description plugin-nfs -l pl.UTF-8
Ten pakiet zawiera wtyczkę do obsługi lokalnego eksportowania NFS-a.

%package plugin-smis
Summary:	Files for SMI-S generic array support for libStorageMgmt
Summary(pl.UTF-8):	Pliki ogólnej obsługi macierzy SMI-S dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Requires:	python3-pywbem
Obsoletes:	libstoragemgmt-smis-plugin < 1.9.4
BuildArch:	noarch

%description plugin-smis
This package contains plug-in for generic SMI-S array support.

%description plugin-smis -l pl.UTF-8
Ten pakiet zawiera wtyczkę do ogólnej obsługi macierzy SMI-S.

%package plugin-targetd
Summary:	Files for targetd array support for libStorageMgmt
Summary(pl.UTF-8):	Pliki obsługi macierzy targetd dla libStorageMgmt
Group:		Libraries
Requires:	%{name}-daemon = %{version}-%{release}
Obsoletes:	libstoragemgmt-targetd-plugin < 1.9.4
BuildArch:	noarch

%description plugin-targetd
This package contains plug-in for targetd array support.

%description plugin-targetd -l pl.UTF-8
Ten pakiet zawiera wtyczkę do obsługi macierzy targetd.

%prep
%setup -q
%patch -P 0 -p1

%{__sed} -i -e '1s,/usr/bin/env python@PY_VERSION@,%{__python3},' \
	tools/basic_check/local_check.py.in \
	tools/lsmcli/lsmcli.in \
	tools/use_cases/find_unused_lun.py.in \
	plugin/*_plugin/*_lsmplugin.in

# daemon/lsb_daemon.c still specifies /var/run/lsm, adjust tmpfiles back
%{__sed} -i -e 's, /run/lsm,/var/run/lsm,' packaging/daemon/libstoragemgmt.conf

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

install -d build
cd build
%define	configuredir	..
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-bash-completion-dir=%{bash_compdir} \
	--with-python3 \
	%{!?with_tests:--without-test}

%{__make}
cd ..

%if %{with python2}
install -d build-py2
cd build-py2
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-bash-completion-dir=%{bash_compdir} \
	--with-python2 \
	%{!?with_tests:--without-test}

%{__make}
cd ..
%endif

%if %{with tests}
if ! make -C build check
then
	cat test-suite.log || true
	exit 1
fi

%if %{with python2}
if ! make -C build-py2 check
then
	cat test-suite.log || true
	exit 1
fi
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__make} -C build-py2 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/{lsm,nfs_plugin}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/*_plugin
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/*_plugin
%py_postclean

%{__rm} $RPM_BUILD_ROOT%{_bindir}/lsmcli
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libstoragemgmt.la
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/{lsm,nfs_plugin}/*.la

# Files for udev handling
install -d $RPM_BUILD_ROOT/lib/udev/rules.d
cp -p tools/udev/90-scsi-ua.rules $RPM_BUILD_ROOT/lib/udev/rules.d/90-scsi-ua.rules
install build/tools/udev/scan-scsi-target $RPM_BUILD_ROOT/lib/udev/scan-scsi-target

install -d $RPM_BUILD_ROOT/var/run/lsm/ipc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%pre daemon
%groupadd -g 345 libstoragemgmt
%useradd -u 345 -d /var/run/lsm -s /bin/false -c "libstoragemgmt daemon" -g libstoragemgmt libstoragemgmt

%post daemon
%systemd_post %{name}.service

%preun daemon
%systemd_preun %{name}.service

%postun daemon
%systemd_postun %{name}.service
if [ "$1" = "0" ]; then
	%userremove libstoragemgmt
	%groupremove libstoragemgmt
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-arcconf
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-arcconf
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-hpsa
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-hpsa
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-local
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-local
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-megaraid
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-megaraid
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-nfs
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-nfs
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-smis
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-smis
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

# Need to restart lsmd if plugin is new installed or removed.
%post plugin-targetd
if [ $1 -eq 1 ]; then
	%systemd_service_restart %{name}.service
fi

%postun plugin-targetd
if [ $1 -eq 0 ]; then
	%systemd_service_restart %{name}.service
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/lsmcli
%attr(755,root,root) %{_libdir}/libstoragemgmt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstoragemgmt.so.1
%{_mandir}/man1/lsmcli.1*

%files -n bash-completion-libstoragemgmt
%defattr(644,root,root,755)
%{bash_compdir}/lsmcli

%files daemon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lsmd
%attr(755,root,root) %{_bindir}/simc_lsmplugin
%attr(755,root,root) /lib/udev/scan-scsi-target
/lib/udev/rules.d/90-scsi-ua.rules
%dir %{_sysconfdir}/lsm
%dir %{_sysconfdir}/lsm/pluginconf.d
%config(noreplace) %{_sysconfdir}/lsm/lsmd.conf
%{_mandir}/man1/lsmd.1*
%{_mandir}/man1/simc_lsmplugin.1*
%{_mandir}/man5/lsmd.conf.5*
%{systemdunitdir}/%{name}.service
%{systemdtmpfilesdir}/%{name}.conf
%attr(775,root,libstoragemgmt) %dir /var/run/lsm
%attr(775,root,libstoragemgmt) %dir /var/run/lsm/ipc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstoragemgmt.so
%{_includedir}/libstoragemgmt
%{_pkgconfigdir}/libstoragemgmt.pc
%{_mandir}/man3/lsm_*.3*
%{_mandir}/man3/libstoragemgmt.h.3*

%if %{with python2}
%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{py_sitedir}/lsm
%attr(755,root,root) %{py_sitedir}/lsm/_clib.so
%{py_sitedir}/lsm/*.py[co]
%{py_sitedir}/lsm/lsmcli
%endif

%files -n python3-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sim_lsmplugin
%dir %{py3_sitedir}/lsm
%attr(755,root,root) %{py3_sitedir}/lsm/_clib.so
%{py3_sitedir}/lsm/*.py
%{py3_sitedir}/lsm/__pycache__
%{py3_sitedir}/lsm/lsmcli
%{py3_sitedir}/sim_plugin
%dir %{_libexecdir}/lsm.d
%{_libexecdir}/lsm.d/find_unused_lun.py*
%{_libexecdir}/lsm.d/local_check.py*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lsm/pluginconf.d/sim.conf
%{_mandir}/man1/sim_lsmplugin.1*

%files plugin-arcconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arcconf_lsmplugin
%{py3_sitescriptdir}/arcconf_plugin
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lsm/pluginconf.d/arcconf.conf
%{_mandir}/man1/arcconf_lsmplugin.1*

%files plugin-hpsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hpsa_lsmplugin
%{py3_sitescriptdir}/hpsa_plugin
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lsm/pluginconf.d/hpsa.conf
%{_mandir}/man1/hpsa_lsmplugin.1*

%files plugin-local
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/local_lsmplugin
%{py3_sitescriptdir}/local_plugin
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lsm/pluginconf.d/local.conf
%{_mandir}/man1/local_lsmplugin.1*

%files plugin-megaraid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/megaraid_lsmplugin
%{py3_sitescriptdir}/megaraid_plugin
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lsm/pluginconf.d/megaraid.conf
%{_mandir}/man1/megaraid_lsmplugin.1*

%files plugin-nfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nfs_lsmplugin
%dir %{py3_sitedir}/nfs_plugin
%attr(755,root,root) %{py3_sitedir}/nfs_plugin/nfs_clib.so
%{py3_sitedir}/nfs_plugin/*.py
%{py3_sitedir}/nfs_plugin/__pycache__
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lsm/pluginconf.d/nfs.conf
%{_mandir}/man1/nfs_lsmplugin.1*

%files plugin-smis
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smispy_lsmplugin
%{py3_sitescriptdir}/smispy_plugin
%{_mandir}/man1/smispy_lsmplugin.1*

%files plugin-targetd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/targetd_lsmplugin
%{py3_sitescriptdir}/targetd_plugin
%{_mandir}/man1/targetd_lsmplugin.1*
