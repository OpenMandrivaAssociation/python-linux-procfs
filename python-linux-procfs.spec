Name:		python-linux-procfs
Version:	0.5.1
Release:	4
License:	GPLv2
Summary:	Linux /proc abstraction classes
Group:		Development/Python
Source0:	https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
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
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%{_bindir}/pflags
%{python3_sitelib}/procfs/
%{python3_sitelib}/python_linux_procfs*.egg-info
