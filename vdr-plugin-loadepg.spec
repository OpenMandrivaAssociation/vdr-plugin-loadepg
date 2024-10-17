
%define plugin	loadepg
%define name	vdr-plugin-%plugin
%define version	0.1.12
%define rel	6

Summary:	VDR plugin: Load EPG Data sent to Mediahighway receivers
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		https://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tgz
Patch0:		loadepg-02_vdr-1.5.14-with-api-wrapper.dpatch
Patch1:		loadepg-02_vdr-1.5.15.dpatch
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
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
install -m644 *.equiv *.conf %{buildroot}%{vdr_plugin_cfgdir}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{vdr_plugin_cfgdir}/%plugin.conf
%config(noreplace) %{vdr_plugin_cfgdir}/%plugin.equiv


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.12-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.12-3mdv2009.1
+ Revision: 359333
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.12-2mdv2009.0
+ Revision: 197945
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.12-1mdv2009.0
+ Revision: 197688
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt for api changes of VDR 1.5.15 (P1 from e-tobi)
- add support for DVB API wrapper (P0 from e-tobi)
- apply new license policy

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.11-3mdv2008.1
+ Revision: 145116
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.11-2mdv2008.1
+ Revision: 103149
- rebuild for new vdr

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.1.11-1mdv2008.0
+ Revision: 81785
- 0.1.11

* Wed Jul 25 2007 Anssi Hannula <anssi@mandriva.org> 0.1.10-2mdv2008.0
+ Revision: 55246
- rebuild due to missing x86_64 binary

* Thu Jul 19 2007 Anssi Hannula <anssi@mandriva.org> 0.1.10-1mdv2008.0
+ Revision: 53417
- 0.1.10

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.9-10mdv2008.0
+ Revision: 50014
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.9-9mdv2008.0
+ Revision: 42100
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.9-8mdv2008.0
+ Revision: 22747
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-7mdv2007.0
+ Revision: 90938
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-6mdv2007.1
+ Revision: 74044
- rebuild for new vdr
- Import vdr-plugin-loadepg

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-2mdv2007.0
- rebuild for new vdr

* Fri Jul 14 2006 Anssi Hannula <anssi@mandriva.org> 0.1.9-1mdv2007.0
- initial Mandriva release

