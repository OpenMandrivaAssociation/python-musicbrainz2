
Summary: An interface to the MusicBrainz XML web service

Name: python-musicbrainz2
Version: 0.7.4
Release: 2
Url: http://musicbrainz.org/products/python-musicbrainz2/
Source0: http://ftp.musicbrainz.org/pub/musicbrainz/python-musicbrainz2/%{name}-%{version}.tar.gz
License: BSD
Group: Development/Python
BuildRequires: python-devel
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
python setup.py install --root=%{buildroot}

%clean

%files
%doc *.txt
%{_bindir}/mb-submit-disc
%{py_puresitedir}/*




