Summary:	DevHelp book: automake
Summary(pl):	Ksi±¿ka do DevHelpa o automake'u
Name:		devhelp-book-automake
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/automake.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DevHelp book about automake.

%description -l pl
Ksi±¿ka do DevHelpa o automake'u.

%prep
%setup -q -c -n automake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/automake,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/automake.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/automake

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
