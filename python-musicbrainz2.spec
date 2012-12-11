%define name python-musicbrainz2
%define version 0.7.4
%define release %mkrel 1

Summary: An interface to the MusicBrainz XML web service
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://musicbrainz.org/products/python-musicbrainz2/
Source0: http://ftp.musicbrainz.org/pub/musicbrainz/python-musicbrainz2/%{name}-%{version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%{py_requires -d}
BuildRequires: python-setuptools
BuildRequires: python-ctypes
BuildArch: noarch
Requires: python-ctypes libdiscid
Obsoletes: python-musicbrainz < 2.1.5-5
Provides: python-musicbrainz

%description
python-musicbrainz2 provides simple, object oriented access to the
MusicBrainz XML web service. It is useful for applications like CD rippers,
taggers, media players, and other tools that need music metadata.

The MusicBrainz Project collects music metadata and is maintained by its large
and constantly growing user
community.


%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt
%_bindir/mb-submit-disc
%py_puresitedir/*




%changelog
* Mon Nov 21 2011 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdv2012.0
+ Revision: 732165
- new version

* Sat Jun 11 2011 Götz Waschk <waschk@mandriva.org> 0.7.3-1
+ Revision: 684216
- new version
- new source URL

* Fri Jan 08 2010 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 487429
- update to new version 0.7.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0-6mdv2010.0
+ Revision: 442318
- rebuild

* Fri Jan 02 2009 Adam Williamson <awilliamson@mandriva.org> 0.6.0-5mdv2009.1
+ Revision: 323251
- clean up python deps
- obsolete / provide python-musicbrainz (since it's now unsupported and nothing
  uses it)

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-4mdv2009.1
+ Revision: 320636
- rebuild for new python

* Thu Oct 16 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-3mdv2009.1
+ Revision: 294387
- rebuild for new libdiscid

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 269035
- rebuild early 2009.0 package (before pixel changes)

* Mon May 26 2008 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 211296
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 14 2007 Thierry Vignaud <tv@mandriva.org> 0.5.0-2mdv2008.0
+ Revision: 63109
- fix description

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 63051
- new version


* Tue Dec 19 2006 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2007.0
+ Revision: 100303
- new version

* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.0-3mdv2007.1
+ Revision: 96110
- Rebuild against new python

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-2mdv2007.1
+ Revision: 88223
- update file list

* Sat Nov 25 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2007.1
+ Revision: 87242
- Import python-musicbrainz2

* Sat Nov 25 2006 G�tz Waschk <waschk@mandriva.org> 0.4.0-1mdv2007.1
- initial package

