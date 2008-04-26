
%define plugin	loadepg
%define name	vdr-plugin-%plugin
%define version	0.1.12
%define rel	1

Summary:	VDR plugin: Load EPG Data sent to Mediahighway receivers
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tgz
Patch0:		loadepg-02_vdr-1.5.14-with-api-wrapper.dpatch
Patch1:		loadepg-02_vdr-1.5.15.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Loads EPG Data sent to Mediahighway receivers (Canal+ group).

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# alternative configuration directory
var=CONFIG_DIR
param="-c CONFIG_DIR"
%vdr_plugin_params_end

perl -pi -e "s,^SCRIPT,# SCRIPT," loadepg.conf
perl -pi -e "s,^FILE,# FILE," loadepg.conf

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
