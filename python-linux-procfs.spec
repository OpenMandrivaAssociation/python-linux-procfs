Name:		python-linux-procfs
Version:	0.6
Release:	1
License:	GPLv2
Summary:	Linux /proc abstraction classes
Group:		Development/Python
Source0:	http://pypi.python.org/packages/source/p/python-linux-procfs/%{name}-%{version}.tar.gz
URL:		https://rt.wiki.kernel.org/index.php/Tuna
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
Requires:	python3egg(six)

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/pflags
%{py3_puresitedir}/procfs/
%{py3_puresitedir}/python_linux_procfs*.egg-info
