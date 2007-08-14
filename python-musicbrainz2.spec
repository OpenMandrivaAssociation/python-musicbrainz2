%define name python-musicbrainz2
%define version 0.5.0
%define release %mkrel 1

Summary: An interface to the MusicBrainz XML web service
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://musicbrainz.org/products/python-musicbrainz2/
Source0: http://musicbrainz.org/~matt/%{name}-%{version}.tar.bz2
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: python-ctypes
BuildArch: noarch
Requires: python-ctypes libdiscid

%description
An interface to the MusicBrainz XML web service
===============================================

python-musicbrainz2 provides simple, object oriented access to the
MusicBrainz web service. It is useful for applications like CD rippers,
taggers, media players, and other tools that need music metadata.

The MusicBrainz Project (see http://musicbrainz.org) collects music
metadata and is maintained by its large and constantly growing user
community.

Most of this package works on python-2.3 and later without further
dependencies. If you want to generate DiscIDs from an audio CD in the
drive, you need ctypes (already included in python-2.5) and libdiscid.


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


