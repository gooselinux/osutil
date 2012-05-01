Name:             osutil
Version:          2.0.1
Release:          1%{?dist}
Summary:          Operating System Utilities JNI Package
URL:              http://pki.fedoraproject.org/
License:          GPLv2
Group:            System Environment/Libraries

BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:    cmake
BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    nspr-devel
BuildRequires:    nss-devel
BuildRequires:    pkgconfig

Requires:         java >= 1:1.6.0
Requires:         jpackage-utils
Requires:         nss

Source0:          http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.tar.gz

%if 0%{?rhel}
#rhel has no java on ppc
ExcludeArch:    ppc ppc64 s390 s390x
%endif


%description
The Operating System Utilities Java Native Interface (JNI) package
supplies various native operating system operations to Java programs.


%prep


%setup -q


%clean
%{__rm} -rf %{buildroot}


%build
%{__mkdir_p} build
cd build
%cmake -DBUILD_OSUTIL:BOOL=ON ..
%{__make} VERBOSE=1 %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
cd build
%{__make} install DESTDIR=%{buildroot}

cd %{buildroot}%{_libdir}/osutil
%{__rm} osutil.jar
%{__ln_s} osutil-%{version}.jar osutil.jar

cd %{buildroot}%{_jnidir}
%{__rm} osutil.jar
%{__ln_s} %{_libdir}/osutil/osutil.jar osutil.jar


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_jnidir}/osutil.jar
%{_libdir}/osutil/


%changelog
* Fri Jan 21 2011 Matthew Harmsen <mharmsen@redhat.com> 2.0.1-1
- Removed version information from NSPR and NSS build/runtime requires
- Bugzilla Bug #638377 - Generate PKI UI components which exclude
  a GUI interface
- Bugzilla Bug #643206 - New CMake based build system for Dogtag
- Bugzilla Bug #644056 - CS build contains warnings
- Bugzilla Bug #667556 - Consolidate 'osutil' SVN source code with
  'osutil' GIT source code

* Thu Jan 6 2011 Kevin Wright <kwright@redhat.com> 2.0.0-3
- added s390 and s390x to the exclude arches due to missing java-devel >= 1:1.6.0

* Thu Jan 6 2011 Kevin Wright <kwright@redhat.com> 2.0.0-2
- Cleaned up the spec file.
- Re-added the changelog history.

* Wed Dec 1 2010 Matthew Harmsen <mharmsen@redhat.com> 2.0.0-1
- Initial 2.0 revision. (kwright@redhat.com & mharmsen@redhat.com)

* Mon Feb 01 2010 Kevin Wright <kwright@redhat.com> 1.3.1-3
- no java on rhel ppc

* Fri Jan 29 2010 Matthew Harmsen <mharmsen@redhat.com> 1.3.1-2
- Applied %%{?_smp_mflags} option to 'make'

* Mon Dec 14 2009 Kevin Wright <kwright@redhat.com> 1.3.1-1
- Removed BuildRequires bash
- Removed 'with exceptions' from License

* Fri Oct 30 2009 Matthew Harmsen <mharmsen@redhat.com> 1.3.0-3
- Bugzilla Bug #521983 -  New package for Dogtag PKI: osutil
- Removed LICENSE logic from installation section
- Take ownership of library directory

* Tue Oct 27 2009 Matthew Harmsen <mharmsen@redhat.com> 1.3.0-2
- Bugzilla Bug #521983 -  New package for Dogtag PKI: osutil
- Complied with Fedora JNI packaging logic

* Thu Oct 8 2009 Matthew Harmsen <mharmsen@redhat.com> 1.3.0-1
- Bugzilla Bug #521983 -  New package for Dogtag PKI: osutil

