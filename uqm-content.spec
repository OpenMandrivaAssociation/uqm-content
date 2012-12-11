%define base_name	uqm
%define name		%{base_name}-content
%define version		0.6.0
%define release		%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Mandatory content package for Ur-Quan Masters game
License:	GPL
Group:		Games/Strategy
URL:		http://sc2.sourceforge.net
Source:		http://prdownloads.sourceforge.net/sc2/%{base_name}-%{version}-content.uqm
Requires:	%{base_name}
Provides:	%{base_name}-data
Obsoletes:	%{base_name}-data
BuildArch:	    noarch
ExcludeArch:    x86_64 amd64
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
The Ur-Quan Masters is a port of the 3DO version of Star Control 2.

%prep
%setup -c -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/content
cp -pr * %{buildroot}%{_gamesdatadir}/%{base_name}/content

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}/content/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-7mdv2010.0
+ Revision: 434584
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-6mdv2009.0
+ Revision: 261792
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-5mdv2009.0
+ Revision: 255229
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6.0-3mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-3mdv2007.0
+ Revision: 121004
- drop versioning on base package dependency

* Thu Jan 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-2mdv2007.1
+ Revision: 113141
- game engine is not x86_64 compatible, so mark content as noarch too

* Wed Jan 24 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1mdv2007.1
+ Revision: 112931
- new version
- Import uqm-content

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-2mdv2007.0
- Rebuild

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdk
- new version
- keep original archive

* Tue May 31 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-1mdk 
- new version
- changed name
- moved 3domusic and voice into distinct packages

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3-2mdk 
- rebuild

