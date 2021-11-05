Summary:	Implementation of the varlink protocol in golang
Name:		golang-varlink
Version:	0.3.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/varlink/go/releases
Source0:	https://github.com/varlink/go/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ef568f337755816a952b58199027d446
URL:		https://github.com/varlink/go
Requires:	golang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages 0

%description
Implementation of the varlink protocol in golang.

%prep
%setup -q -n go-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/golang/src/github.com/varlink/go

cp -rp varlink $RPM_BUILD_ROOT%{_libdir}/golang/src/github.com/varlink/go

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{_libdir}/golang/src/github.com/varlink
%{_libdir}/golang/src/github.com/varlink/go
