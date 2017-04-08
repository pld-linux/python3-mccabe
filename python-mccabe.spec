#
# Conditional build:
%bcond_without	tests	# test target
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	mccabe
Summary:	McCabe checker, plugin for flake8
Summary(pl.UTF-8):	Wtyczka flake8 do sprawdzania złożoności McCabe'a
Name:		python-%{module}
Version:	0.6.1
Release:	1
License:	Expat/MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/mccabe/
Source0:	https://files.pythonhosted.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz
# Source0-md5:	723df2f7b1737b8887475bac4c763e1e
URL:		https://github.com/pycqa/mccabe
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-pytest-runner
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-runner
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ned's script to check McCabe complexity.

%description -l pl.UTF-8
Skrypt Neda do sprawdzania złożoności McCabe'a (cyklomatycznej).

%package -n python3-%{module}
Summary:	McCabe checker, plugin for flake8
Summary(pl.UTF-8):	Wtyczka flake8 do sprawdzania złożoności McCabe'a
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
Ned's script to check McCabe complexity.

%description -n python3-%{module} -l pl.UTF-8
Skrypt Neda do sprawdzania złożoności McCabe'a (cyklomatycznej).

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/mccabe.py[co]
%{py_sitescriptdir}/mccabe-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/mccabe.py
%{py3_sitescriptdir}/__pycache__/mccabe.cpython-*.py[co]
%{py3_sitescriptdir}/mccabe-%{version}-py*.egg-info
%endif
