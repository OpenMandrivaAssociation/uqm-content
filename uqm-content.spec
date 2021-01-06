%define base_name	uqm

Name:		%{base_name}-content
Version:	0.8.0
Release:	1
Summary:	Mandatory content package for Ur-Quan Masters game
License:	GPL
Group:		Games/Strategy
URL:		http://sc2.sourceforge.net
Source:		http://sourceforge.net/projects/sc2/files/UQM/%(echo %{version} |cut -d. -f1-2)/uqm-%{version}-content.uqm
Requires:	%{base_name}
%rename %{base_name}-data
BuildArch:	noarch

%description
The Ur-Quan Masters is a port of the 3DO version of Star Control 2.

%prep
%setup -c -q

%build

%install
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/content
cp -pr * %{buildroot}%{_gamesdatadir}/%{base_name}/content

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}/content/*
