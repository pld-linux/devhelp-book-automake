Summary:	DevHelp book: automake
Summary(pl):	Ksi±¿ka do DevHelp'a o automake
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

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about automake

%description -l pl
Ksi±¿ka do DevHelp o automake

%prep
%setup -q -c automake -n automake

%build
mv -f book automake
mv -f book.devhelp automake.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/automake
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install automake.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install automake/* $RPM_BUILD_ROOT%{_prefix}/books/automake

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
