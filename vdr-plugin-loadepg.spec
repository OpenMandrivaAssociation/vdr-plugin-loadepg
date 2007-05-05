
%define plugin	loadepg
%define name	vdr-plugin-%plugin
%define version	0.1.9
%define rel	8

Summary:	VDR plugin: Load EPG Data sent to Mediahighway receivers
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Loads EPG Data sent to Mediahighway receivers (Canal+ group).

%prep
%setup -q -n %plugin-%version

%vdr_plugin_params_begin %plugin
# alternative configuration directory
var=CONFIG_DIR
param="-c CONFIG_DIR"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
install -m644 *.equiv *.conf %{buildroot}%{_vdr_plugin_cfgdir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{_vdr_plugin_cfgdir}/%plugin.conf
%config(noreplace) %{_vdr_plugin_cfgdir}/%plugin.equiv


