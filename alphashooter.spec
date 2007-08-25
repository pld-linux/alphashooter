Summary:	3D first-person shooter
Summary(pl.UTF-8):	Trójwymiarowa strzelanina typu FPP
Name:		alphashooter
Version:	0.0.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/alphashooter/%{name}-%{version}.tar.bz2
# Source0-md5:	a0dd9c2fbcb0d4e6a4fd53065c99fa18
Patch0:		%{name}-Makefile.patch
URL:		http://alphashooter.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	freeglut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alpha Shooter is a 3D OpenGL first-person shooter game with a sci-fi
setting.

%description -l pl.UTF-8
Alpha Shooter jest trójwymiarową strzelaniną FPP używającą OpenGL z
oprawą sci-fi.

%prep
%setup -q
%patch0 -p1

%build
%{__make} linux \
	CC="%{__cc}"
	CFLAGS="%{rpmcflags}" \
	LDFALGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
