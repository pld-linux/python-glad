#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs
Summary(pl.UTF-8):	Wielojęzykowy generator loaderów GL/GLES/EGL/GLX/WGL oparty na oficjalnych specyfikacjach
Name:		python-glad
Version:	0.1.36
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/glad/
Source0:	https://files.pythonhosted.org/packages/source/g/glad/glad-%{version}.tar.gz
# Source0-md5:	e691bde76a8434b375681c6fab65b49c
URL:		https://pypi.org/project/glad/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glad uses the official Khronos-XML specs to generate a
GL/GLES/EGL/GLX/WGL Loader made for your needs.

%description -l pl.UTF-8
Glad wykorzystuje oficjalne specyfikacje Khronos-XML do generowania
loaderów GL/GLES/EGL/GLX/WGL zgodnych z potrzebami.

%package -n python3-glad
Summary:	Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs
Summary(pl.UTF-8):	Wielojęzykowy generator loaderów GL/GLES/EGL/GLX/WGL oparty na oficjalnych specyfikacjach
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-glad
Glad uses the official Khronos-XML specs to generate a
GL/GLES/EGL/GLX/WGL Loader made for your needs.

%description -n python3-glad -l pl.UTF-8
Glad wykorzystuje oficjalne specyfikacje Khronos-XML do generowania
loaderów GL/GLES/EGL/GLX/WGL zgodnych z potrzebami.

%prep
%setup -q -n glad-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__mv} $RPM_BUILD_ROOT%{_bindir}/glad{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/glad{,-3}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/glad-2
%{py_sitescriptdir}/glad
%{py_sitescriptdir}/glad-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-glad
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/glad-3
%{py3_sitescriptdir}/glad
%{py3_sitescriptdir}/glad-%{version}-py*.egg-info
%endif
