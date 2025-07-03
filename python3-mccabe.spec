# TODO: prepare hypothesmith, reenable tests
#
# Conditional build:
%bcond_with	tests	# unit tests

%define		module	mccabe
Summary:	McCabe checker, plugin for flake8
Summary(pl.UTF-8):	Wtyczka flake8 do sprawdzania złożoności McCabe'a
Name:		python3-%{module}
Version:	0.7.0
Release:	2
License:	Expat/MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mccabe/
Source0:	https://files.pythonhosted.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz
# Source0-md5:	374ee2b9407546bb41d195e7436e5f62
URL:		https://github.com/pycqa/mccabe
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis
BuildRequires:	python3-hypothesmith
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ned's script to check McCabe complexity.

%description -l pl.UTF-8
Skrypt Neda do sprawdzania złożoności McCabe'a (cyklomatycznej).

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test_mccabe.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/mccabe.py
%{py3_sitescriptdir}/__pycache__/mccabe.cpython-*.py[co]
%{py3_sitescriptdir}/mccabe-%{version}-py*.egg-info
