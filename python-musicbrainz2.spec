%define name python-musicbrainz2
%define version 0.5.0
%define release %mkrel 2

Summary: An interface to the MusicBrainz XML web service
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://musicbrainz.org/products/python-musicbrainz2/
Source0: http://musicbrainz.org/~matt/%{name}-%{version}.tar.bz2
License: BSD
Group: Development/Python
BuildRequires: python-devel
BuildRequires: python-ctypes
BuildArch: noarch
Requires: python-ctypes libdiscid

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


