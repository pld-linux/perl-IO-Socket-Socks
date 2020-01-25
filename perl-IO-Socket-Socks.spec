#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Socket-Socks
Summary:	IO::Socket::Socks - provides a way to create socks client or server both 4 and 5 version
Summary(pl.UTF-8):	IO::Socket::Socks - tworzenie klienta i serwera SOCKS w wersji 4 i 5
Name:		perl-IO-Socket-Socks
Version:	0.74
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b19fba551ae14aa2382bfe318245de2
URL:		http://search.cpan.org/dist/IO-Socket-Socks/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Socket::Socks connects to a SOCKS proxy, tells it to open a
connection to a remote host/port when the object is created. The
object you receive can be used directly as a socket (with IO::Socket
interface) for sending and receiving data from the remote host. In
addition to create socks client this module could be used to create
socks server.

%description -l pl.UTF-8
IO::Socket::Socks łączy się do proxy SOCKS i mówi mu, żeby połączył
się ze zdalnym hostem. Obiekt tego typu można użyć wprost jako socket
(z interfejsem IO::Socket) do wysyłania i pobierania danych ze
zdalnego hosta. Dodatkowo, poza możliwością tworzenia klienta SOCKS,
można również utworzyć serwer SOCKS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Socket/Socks.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
