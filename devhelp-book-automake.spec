Summary:	DevHelp book: automake
Summary(pl):	Ksi±¿ka do DevHelpa o automake'u
Name:		devhelp-book-automake
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/automake.tar.gz
# Source0-md5:	3dd4ef2d0f1f33778ae808c1327690b4
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about automake.

%description -l pl
Ksi±¿ka do DevHelpa o automake'u.

%prep
%setup -q -c -n automake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/automake

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/automake/automake.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/automake

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
