%define compile_apidox 0
%define _mobile 0
%define prerel %nil
%define _disable_ld_no_undefined 1
%define defaultmajor 14

%define service(s) %{_libdir}/kde4/%{1}.so \
%{_datadir}/kde4/services/calligra/%{1}.desktop
%define kservice(s) %{_libdir}/kde4/%{1}.so \
%{_datadir}/kde4/services/%{1}.desktop

Summary:	Set of office applications for KDE
#koffice has epoch 15. We need upper epoch
Epoch:		16
Name:		calligra
URL:		http://www.calligra-suite.org
Version:	2.9.1
%if "%prerel" != ""
Release:	0.%prerel.1
%else
Release:	2
%endif
Source0:	http://master.kde.org/%(if [ `echo %version |cut -d. -f3` -ge 50 ]; then echo -n un; fi)stable/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch2:		calligra-2.6.0-xbase-3.1.2.patch
Patch3:		calligra-optionize-staging.patch
Patch4:		calligra-2.8.0-libpqxx-4.0.patch
Group:		Office
License:	GPLv2+ and LGPLv2+ and GFDL
BuildRequires:	kdepimlibs4-devel
#Source100:		%{name}.rpmlintrc

#For version upper or equal 2012
BuildRequires:	pkgconfig(libkexiv2)
#BuildRequires:	kdegraphics4-devel
BuildRequires:	pkgconfig(libkdcraw)
#For version upper or equal 2012
BuildRequires:	okular-devel
BuildRequires:	gmic-devel
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	xbase-devel
BuildRequires:	pkgconfig(libwpd-0.10)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	jbig-devel
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libpqxx)
BuildRequires:	postgresql-devel
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pstoedit
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	glpk-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:	getfem-devel
BuildRequires:	pkgconfig(libctemplate)
BuildRequires:	freetds-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	marble-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(libodfgen-0.1)
BuildRequires:	pkgconfig(libvisio-0.1)
BuildRequires:	pkgconfig(libwps-0.3)
BuildRequires:	pkgconfig(libetonyek-0.1)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	nepomuk-core-devel
BuildRequires:	nepomuk-widgets-devel
BuildRequires:	tiff-devel
%if %compile_apidox
BuildRequires:	graphviz
BuildRequires:	doxygen
%endif
Suggests:	%{name}-words
Suggests:	%{name}-sheets
Suggests:	%{name}-karbon
Suggests:	%{name}-stage
Suggests:	%{name}-krita
Suggests:	%{name}-plan
Suggests:	%{name}-kchart
Suggests:	%{name}-kformula
Suggests:	%{name}-kexi
Suggests:	%{name}-flow
Suggests:	%{name}-braindump
Obsoletes:	f-office
Obsoletes:	koshell
Obsoletes:	kugar
Obsoletes:	kivio
Obsoletes:	koffice-kivio < 1.6.3-20
Obsoletes:	koffice

%description
Office applications for the K Desktop Environment.

Calligra contains:
   * Words: word processor
   * Table: spreadsheet
   * Stage: presentations
   * Flow: diagram generator
   * Some filters (Excel 97, Winword 97/2000, etc.)
   * karbon: the scalable vector drawing application for KDE.
   * krita: painting and image editing application.
   * plan: a project management.
   * kexi: an integrated data management application.

%files

#--------------------------------------------------------------------
%libpackage koversion 14
%libpackage kritacolor 14
%libpackage kritasketchlib 14
#--------------------------------------------------------------------

%package core
Group:		Office
Summary:	Set of office applications for KDE
Obsoletes:	koffice-core < 15:2.4
Obsoletes:	%{_lib}kopainter5
Obsoletes:	koffice2-core
Obsoletes:	koffice-common
Obsoletes:	koshell
Obsoletes:	kugar
Obsoletes:	kplatowork
Obsoletes:	kivio
Requires:	kdebase4-runtime

%description core
Common files for Calligra.

%files core
%defattr(0755,root,root,0755)
%{_bindir}/calligra
%{_bindir}/calligraconverter
%{_bindir}/cstester
%{_bindir}/cstrunner
%{_bindir}/visualimagecompare
%{service calligra_docker_defaults}
%{service calligra_shape_artistictext}
%{service calligra_textediting_autocorrect}
%{service calligra_textediting_changecase}
%{service calligra_textediting_spellcheck}
%{service calligra_textediting_thesaurus}
%{service calligra_tool_basicflakes}
%{service calligra_tool_defaults}
%{service calligra_shape_music}
%{service calligra_shape_paths}
%{service calligra_shape_picture}
%{service calligra_shape_plugin}
%{service calligra_shape_text}
%{service calligra_shape_threed}
%{service calligra_shape_vector}
%{service calligra_shape_video}
%{service calligra_textinlineobject_variables}
%{_libdir}/kde4/calligradocinfopropspage.so
%{_libdir}/kde4/calligraimagethumbnail.so
%{_libdir}/kde4/calligrathumbnail.so
#%{_libdir}/kde4/calligragoogledocs.so
%{_libdir}/kde4/kolcmsengine.so
%{_libdir}/kde4/kopabackgroundtool.so
%{_libdir}/kde4/koreport_barcodeplugin.so
%{_libdir}/kde4/koreport_chartplugin.so
%optional %{_libdir}/kde4/koreport_mapsplugin.so
%{_libdir}/kde4/koreport_webplugin.so
%{_datadir}/icons/*/*/*/insert-tableofcontents.*
%{_libdir}/calligra/imports/org/calligra/CalligraComponents
%defattr(0644,root,root,0755)
%_kde_applicationsdir/calligra.desktop
%{_kde_appsdir}/calligra
%{_kde_appsdir}/koproperty
%{_kde_appsdir}/musicshape
%{_datadir}/kde4/servicetypes/kopa_tool.desktop
%{_datadir}/kde4/servicetypes/kpr_tool.desktop
%_kde_iconsdir/*/*/actions/black.*
%_kde_iconsdir/*/*/actions/curve-connector.*
%_kde_iconsdir/*/*/actions/highlight.*
%_kde_iconsdir/*/*/actions/insert-endnote.png
%_kde_iconsdir/*/*/actions/insert-footnote.png
%_kde_iconsdir/*/*/actions/lines-connector.png
%_kde_iconsdir/*/*/actions/object-align-horizontal-center-calligra.*
%_kde_iconsdir/*/*/actions/object-align-horizontal-left-calligra.*
%_kde_iconsdir/*/*/actions/object-align-horizontal-right-calligra.*
%_kde_iconsdir/*/*/actions/object-align-vertical-bottom-calligra.*
%_kde_iconsdir/*/*/actions/object-align-vertical-bottom-top-calligra.*
%_kde_iconsdir/*/*/actions/object-align-vertical-center-calligra.*
%_kde_iconsdir/*/*/actions/object-align-vertical-top-calligra.*
%_kde_iconsdir/*/*/actions/object-group-calligra.*
%_kde_iconsdir/*/*/actions/object-order-back-calligra.*
%_kde_iconsdir/*/*/actions/object-order-front-calligra.*
%_kde_iconsdir/*/*/actions/object-order-lower-calligra.*
%_kde_iconsdir/*/*/actions/object-order-raise-calligra.*
%_kde_iconsdir/*/*/actions/object-ungroup-calligra.*
%_kde_iconsdir/*/*/actions/pen.*
%_kde_iconsdir/*/*/actions/shape-choose.* 
%_kde_iconsdir/*/*/actions/standard-connector.*
%_kde_iconsdir/*/*/actions/straight-connector.*
%_kde_iconsdir/*/*/actions/table.*
%_kde_iconsdir/*/*/actions/x-shape-connection.*
%_kde_iconsdir/*/*/actions/x-shape-formula.*
%_kde_iconsdir/*/*/actions/x-shape-image.*
%_kde_iconsdir/*/*/actions/x-shape-text.*
%_kde_services/calligra_odg_thumbnail.desktop
%_kde_services/calligra/kolcmsengine.desktop
%_kde_services/calligra/kopabackgroundtool.desktop
%_kde_services/calligra/koreport_barcodeplugin.desktop
%_kde_services/calligra/koreport_chartplugin.desktop
%optional %_kde_services/calligra/koreport_mapsplugin.desktop
%_kde_services/calligra/koreport_webplugin.desktop
%_kde_servicetypes/calligra_application.desktop
%_kde_servicetypes/flake.desktop
%_kde_servicetypes/flakedevice.desktop
%_kde_servicetypes/flakeshape.desktop
%_kde_servicetypes/flaketool.desktop
%_kde_servicetypes/inlinetextobject.desktop
%_kde_servicetypes/calligradocker.desktop
%_kde_servicetypes/koreport_itemplugin.desktop
%_kde_servicetypes/pigment.desktop
%_kde_servicetypes/pigmentextension.desktop
%_kde_servicetypes/scripteventaction.desktop
%_kde_servicetypes/texteditingplugin.desktop
%_kde_servicetypes/calligra_deferred_plugin.desktop
%{_datadir}/mime/packages/msooxml-all.xml
%{_datadir}/mime/packages/calligra_svm.xml
%_kde_services/calligra/calligradocinfopropspage.desktop
%_kde_servicetypes/calligra_filter.desktop
%_kde_servicetypes/calligra_part.desktop
%doc %_kde_docdir/HTML/en/calligra
# FIXME Should those remain core or move to a separate package?
%_kde_servicetypes/calligra_semanticitem.desktop
%{service calligra_semanticitem_contact}
%{service calligra_semanticitem_event}
%{service calligra_semanticitem_location}
%optional %{_datadir}/kde4/services/calligra/calligra_docker_textdocumentinspection.desktop

#--------------------------------------------------------------------

%package words
Summary:		Word processor for calligra
Group:			Graphical desktop/KDE
URL:			http://www.calligra-suite.org/words/
Requires:		%{name}-core = %{EVRD}
Requires:		wordnet
Provides:		%{name}-apps
Obsoletes:		koffice-kword
Obsoletes:		koffice2-kword
Obsoletes:		kword

%description    words
Words is an intuitive word processor application with desktop publishing
features.
With it, you can create informative and attractive documents with ease.

%files words
%defattr(755,root,root)
%{_bindir}/calligrawords
%{service calligra_filter_odt2ascii}
%{service calligra_filter_doc2odt}
%{service calligra_filter_ascii2words}
%{service calligra_filter_applixword2odt}
%{service calligra_filter_docx2odt}
%{service calligra_filter_odt2epub2}
%{service calligra_filter_odt2html}
%{service calligra_filter_odt2mobi}
%{service calligra_filter_rtf2odt}
%{service calligra_filter_wps2odt}
%{service calligra_filter_wpd2odt}
%{service calligra_filter_odt2docx}
%{kservice calligra_filter_odt2wiki}
%{_datadir}/kde4/services/words_*_thumbnail.desktop
%{_datadir}/applications/kde4/calligrawords_ascii.desktop
%{_datadir}/mime/packages/wiki-format.xml
#%{_libdir}/kde4/krossmodulekword.so
%{_libdir}/kde4/wordspart.so
%{_libdir}/libkdeinit4_calligrawords.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/words.desktop
#%{_kde_appsdir}/kword
%{_kde_appsdir}/words
%_kde_configdir/wordsrc
%_kde_services/ServiceMenus/calligra/words_print.desktop
#%_kde_services/calligra/krossmodulekword.desktop
%_kde_services/calligra/words*.desktop
%{_datadir}/templates/.source/TextDocument.odt
%{_datadir}/templates/TextDocument.desktop
%_kde_iconsdir/hicolor/*/*/calligrawords*
%_kde_iconsdir/hicolor/*/*/calligraauthor*
%_kde_iconsdir/hicolor/*/actions/tool_pagelayout.*
%{_datadir}/appdata/words.appdata.xml

#--------------------------------------------------------------------

%package author
Summary:	Write ebooks and textbooks
Group:		Office
Requires:	%{name}-words = %{EVRD}

%description author
Write ebooks and textbooks.

%files author
%{_bindir}/calligraauthor
%{_libdir}/kde4/authorpart.so
%{_libdir}/libkdeinit4_calligraauthor.so
%{_kde_applicationsdir}/author.desktop
%{_kde_appsdir}/author
%{_kde_configdir}/authorrc
%{_kde_services}/calligra/authorpart.desktop

#--------------------------------------------------------------------

%package plan
Summary:	Project management application for Calligra
Group:		Graphical desktop/KDE
URL:		http://www.calligra-suite.org/plan/
Requires:	%{name}-core = %{EVRD}
Provides:	%{name}-apps
Provides:	kplato2
Obsoletes:	kplatowork
Obsoletes:	kplato
Obsoletes:	%{_lib}kplatoworkprivat5
Obsoletes:	koffice-kplato
Obsoletes:	koffice2-kplato
# For M$ Project import filter
BuildRequires:	java-1.7.0-openjdk-devel
%rename		plan

%description plan
Plan is a project management application.
It is intended for managing moderately large projects with multiple resources.

%files plan
%defattr(0755,root,root,0755)
%{_bindir}/calligraplan
%{_bindir}/calligraplanwork
%{_libdir}/libkdeinit4_calligraplan.so
%{_libdir}/libkdeinit4_calligraplanwork.so
%{_libdir}/kde4/krossmoduleplan.so
%{_libdir}/kde4/planpart.so
%{_libdir}/kde4/planworkpart.so
%{_libdir}/kde4/planicalexport.so
%{_libdir}/kde4/plankplatoimport.so
%{_libdir}/kde4/plantjscheduler.so
# Doesn't fit the regular service naming scheme, can't use %%service
%{_libdir}/kde4/calligra_filter_mpxj2plan.so
%{_libdir}/kde4/planconvert
%defattr(0644,root,root,0755)
%_kde_applicationsdir/plan.desktop
%_kde_applicationsdir/planwork.desktop
%{_kde_appsdir}/plan
%{_kde_appsdir}/planwork
%{_datadir}/config/planrc
%_kde_services/calligra/krossmoduleplan.desktop
%_kde_services/calligra/plan_icalendar_export.desktop
%_kde_services/calligra/planpart.desktop
%_kde_services/calligra/planworkpart.desktop
%_kde_services/calligra/plan_kplato_import.desktop
%_kde_services/calligra/planrcpsscheduler.desktop
%_kde_services/calligra/plantjscheduler.desktop
%_kde_services/calligra/planscripting.desktop
%_kde_services/calligra/calligra_filter_mpp2plan.desktop
%_kde_services/calligra/calligra_filter_mpx2plan.desktop
%_kde_services/calligra/calligra_filter_planner2plan.desktop
%_kde_servicetypes/plan_schedulerplugin.desktop
%_kde_servicetypes/plan_viewplugin.desktop
%_kde_iconsdir/hicolor/*/*/calligraplan*
%_kde_iconsdir/hicolor/*/*/application-x-vnd.kde.plan*
%_kde_iconsdir/hicolor/*/*/*kde.kplato*
%{_datadir}/config.kcfg/plansettings.kcfg
%{_datadir}/config.kcfg/planworksettings.kcfg
%{_datadir}/config/planworkrc
%{_datadir}/mime/packages/calligra_planner_mpp.xml
%{_datadir}/appdata/plan.appdata.xml

#--------------------------------------------------------------------

%package sheets
Summary:	SpreadSheet for calligra
Group:		Graphical desktop/KDE
URL:		http://www.calligra-suite.org/sheets/
Requires:	%{name}-core = %{EVRD}
Provides:	%{name}-apps
Obsoletes:	koffice-kspread
Obsoletes:	koffice2-kspread
Obsoletes:	kspread
# Sheets used to be called tables in early betas
%rename		tables
%rename		sheets
Conflicts:	kword < 11:2.1.91-2

%description sheets
Sheets is a fully-featured calculation and spreadsheet tool.
Use it to quickly create and calculate various business-related spreadsheets,
such as income and expenditure, employee working hours, etc.

%files sheets
%defattr(0755,root,root,0755)
%{_bindir}/calligrasheets
%{_libdir}/kde4/krossmodulesheets.so
%{_libdir}/kde4/calligrasheetspart.so
%{service calligra_filter_gnumeric2sheets}
%{service calligra_filter_html2ods}
%{service calligra_filter_kspread2tex}
%{service calligra_filter_opencalc2sheets}
%{service calligra_filter_qpro2sheets}
%{service calligra_filter_sheets2csv}
%{service calligra_filter_sheets2gnumeric}
%{service calligra_filter_sheets2html}
%{service calligra_filter_sheets2opencalc}
%{service calligra_filter_xls2ods}
%{service calligra_filter_xlsx2ods}
%{service calligra_filter_applixspread2kspread}
%{service calligra_filter_csv2sheets}
%{service calligra_filter_dbase2kspread}
%{service calligra_shape_spreadsheet}
%{service calligra_shape_spreadsheet-deferred}
%{service sheetspivottables}
%{service sheetssolver}
%_datadir/kde4/services/sheets_*_thumbnail.desktop
%_kde_services/calligra/sheetsscripting.desktop
%_kde_servicetypes/sheets_viewplugin.desktop
%{_libdir}/kde4/kplatorcpsscheduler.so
%{_libdir}/kde4/kspread*.so
%{_libdir}/libkdeinit4_calligrasheets.so
%defattr(0644,root,root,0755)
%{_datadir}/applications/kde4/sheets.desktop
%{_datadir}/config.kcfg/sheets.kcfg
%_kde_services/calligra/sheetspart.desktop
%_kde_services/ServiceMenus/calligra/sheets_print.desktop
%{_kde_appsdir}/sheets
%{_datadir}/config/sheetsrc
%{_datadir}/templates/SpreadSheet.desktop
%_kde_services/calligra/kspread*.desktop
%{_datadir}/templates/.source/SpreadSheet.ods
%_kde_services/calligra/krossmodulesheets.desktop
%_kde_servicetypes/sheets_plugin.desktop
%_kde_iconsdir/hicolor/*/*/calligrasheets*
%doc %_docdir/HTML/en/sheets
%{_datadir}/appdata/sheets.appdata.xml
#--------------------------------------------------------------------

%package stage
Summary:	Presentation for calligra-suite
Group:		Graphical desktop/KDE
URL:		http://www.calligra-suite.org/stage/
Requires:	%{name}-core = %{EVRD}
Requires:	xdg-utils
Provides:	%{name}-apps
Obsoletes:	koffice-kpresenter
Obsoletes:	koffice2-kpresenter
Obsoletes:	kpresenter
%rename	stage


%description stage
Stage is an easy to use yet still flexible presentation application. You can
easily create presentations containing a rich variety of elements,
from graphics to text, from charts to images.
Stage is extensible through a plugin system, so it is easy to add new effects,
new content elements or even new ways of managing your presentation. Because of
the integration with Calligra, all the power and flexibility of the Calligra
content elements are available to Stage.

%files stage
%defattr(0755,root,root,0755)
%{_bindir}/calligrastage
%{_libdir}/kde4/calligrastagepart.so
%{_libdir}/kde4/kpr_pageeffect_barwipe.so
%{_libdir}/kde4/kpr_pageeffect_clockwipe.so
%{_libdir}/kde4/kpr_pageeffect_edgewipe.so
%{_libdir}/kde4/kpr_pageeffect_iriswipe.so
%{_libdir}/kde4/kpr_pageeffect_matrixwipe.so
%{_libdir}/kde4/kpr_pageeffect_slidewipe.so
%{_libdir}/kde4/kpr_pageeffect_fade.so
%{_libdir}/kde4/kpr_pageeffect_spacerotation.so
%{_libdir}/kde4/kpr_pageeffect_swapeffect.so
%{_libdir}/kde4/kpr_shapeanimation_example.so
%{_datadir}/mime/packages/x-iwork-keynote-sffkey.xml
%{_datadir}/kde4/services/stage_*_thumbnail.desktop
%{service calligra_filter_ppt2odp}
%{service calligra_filter_pptx2odp}
%{service calligra_filter_kpr2odp}
%{service calligra_filter_key2odp}
%{_libdir}/kde4/calligrastageeventactions.so 
%{_libdir}/kde4/calligrastagetoolanimation.so
%{_libdir}/kde4/kprvariables.so
#%{_libdir}/kde4/threedshape.so
%{_libdir}/libkdeinit4_calligrastage.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/stage.desktop
%_kde_services/ServiceMenus/calligra/stage_print.desktop
%{_kde_appsdir}/stage
%{_datadir}/templates/Presentation.desktop
%{_datadir}/templates/.source/Presentation.odp
%{_datadir}/config/stagerc
%_kde_iconsdir/hicolor/*/apps/calligrastage.*
%_kde_services/calligra/calligrastageeventactions.desktop
%_kde_servicetypes/presentationeventaction.desktop
%_kde_services/calligra/kpr_pageeffect_barwipe.desktop
%_kde_services/calligra/kpr_pageeffect_clockwipe.desktop
%_kde_services/calligra/kpr_pageeffect_edgewipe.desktop
%_kde_services/calligra/kpr_pageeffect_iriswipe.desktop
%_kde_services/calligra/kpr_pageeffect_matrixwipe.desktop
%_kde_services/calligra/kpr_pageeffect_slidewipe.desktop
%_kde_services/calligra/kpr_shapeanimation_example.desktop
%_kde_services/calligra/kpr_pageeffect_fade.desktop
%_kde_services/calligra/kpr_pageeffect_spacerotation.desktop
%_kde_services/calligra/kpr_pageeffect_swapeffect.desktop
%_kde_services/calligra/calligrastagetoolanimation.desktop
%_kde_services/calligra/kprvariables.desktop
#%_kde_services/calligra/threedshape.desktop
%_kde_servicetypes/kpr_pageeffect.desktop
%_kde_servicetypes/kpr_shapeanimation.desktop
%{_datadir}/kde4/services/calligra/stagepart.desktop
%doc %_docdir/HTML/en/stage
%{_datadir}/appdata/stage.appdata.xml

#--------------------------------------------------------------------

%package kchart
Summary:	Chart and diagram drawing
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
URL:		http://www.koffice.org/
Provides:	%{name}-apps
Provides:	kchart2
Obsoletes:	koffice2-kchart
%rename		kchart


%description kchart
Kchart is a chart and diagram drawing program.

%files kchart
%{service calligra_shape_chart}

#--------------------------------------------------------------------

%package krita
%define __noautoreq 'devel.*'
Summary:	Sketching and painting program
Group:		Graphics
URL:		http://www.calligra-suite.org/krita/
Requires:	%{name}-core = %{EVRD}
Requires:	libkdcraw-common
Provides:	%{name}-apps
Obsoletes:	koffice-krita
Obsoletes:	koffice2-krita
Obsoletes:	%{_lib}kritafilterslistdynamicprogram5
Obsoletes:	%{_lib}krita_gray_u165
Obsoletes:	%{_lib}kritargbf32hdr5
Obsoletes:	%{_lib}krossmodulekrita8
%rename		krita
BuildRequires:	pkgconfig(OpenColorIO)
BuildRequires:	vc-devel

%description krita
Krita offers an end–to–end solution for creating digital painting files
from scratch by masters. It supports concept art, creation of comics
and textures for rendering.

%files krita
%defattr(0755,root,root,0755)
%{_bindir}/gmicparser
%{_bindir}/krita
%{_libdir}/kde4/*krita*
%{_libdir}/kde4/plugins/imageformats/kimg_kra.so
%{_libdir}/kde4/plugins/imageformats/kimg_ora.so
%{_datadir}/kde4/services/qimageioplugins/kra.desktop
%{_datadir}/kde4/services/qimageioplugins/ora.desktop
%{_datadir}/applications/kde4/krita_heightmap.desktop
%{_datadir}/applications/kde4/krita_tga.desktop
%{_libdir}/calligra/imports/org/krita
%{_datadir}/appdata/krita.appdata.xml
%{_datadir}/applications/kde4/kritasketch.desktop
%{_datadir}/apps/kritaanimation
%{_datadir}/apps/kritasketch
%{_datadir}/apps/color-schemes/KritaNeutral.colors
%{_datadir}/config/kritasketchpanelsrc
%{_datadir}/config/kritasketchrc
%{_datadir}/kde4/services/krita_*_thumbnail.desktop
%{_datadir}/color/icc/krita/CMakeLists.txt
%defattr(0644,root,root,0755)
%_kde_applicationsdir/krita.desktop
%_kde_applicationsdir/krita_jpeg.desktop
%_kde_applicationsdir/krita_png.desktop
%_kde_applicationsdir/krita_bmp.desktop
%_kde_applicationsdir/krita_odg.desktop
%_kde_applicationsdir/krita_ora.desktop
%_kde_applicationsdir/krita_pdf.desktop
%_kde_applicationsdir/krita_tiff.desktop
%optional %_kde_applicationsdir/krita_raw.desktop
%_kde_applicationsdir/krita_exr.desktop
%_kde_applicationsdir/krita_jp2.desktop
%_kde_applicationsdir/krita_ppm.desktop
%_kde_applicationsdir/krita_xcf.desktop
%_kde_applicationsdir/krita_psd.desktop
%_kde_services/ServiceMenus/calligra/krita_print.desktop
%_kde_services/calligra/*krita*.desktop
%_kde_servicetypes/*krita*.desktop
%_kde_iconsdir/hicolor/*/apps/calligrakrita.*
%{_kde_appsdir}/krita
%{_kde_appsdir}/kritaplugins
%_kde_configdir/kritarc
%_kde_configdir/krita*.knsrc
%dir %{_datadir}/color/icc/krita
%{_datadir}/color/icc/krita/README
%{_datadir}/color/icc/krita/*.icm
%{_datadir}/color/icc/krita/*.icc
%{_kde_appsdir}/color-schemes/KritaBlender.colors
%{_kde_appsdir}/color-schemes/KritaBright.colors
%{_kde_appsdir}/color-schemes/KritaDark.colors
%{_datadir}/mime/packages/krita_ora.xml
%{_datadir}/mime/packages/krita.xml

#--------------------------------------------------------------------
%package gemini
Summary:	Unified interface for Krita and Krita Sketch
Group:		Graphics

%description gemini
Unified interface for Krita and Krita Sketch.

%files gemini
%{_bindir}/calligragemini
%{_bindir}/calligrageminithumbnailhelper
%{_libdir}/calligra/imports/Calligra/Gemini
%{_datadir}/applications/kde4/calligragemini.desktop
%{_datadir}/apps/calligragemini
%{_datadir}/apps/kritagemini
%{_datadir}/icons/hicolor/*/apps/calligragemini.png
%{_datadir}/icons/hicolor/*/apps/kritasketch.png

#--------------------------------------------------------------------

%package karbon
Summary:	Scalable drawing for calligra
Group:		Graphical desktop/KDE
URL:		http://www.calligra-suite.org/karbon/
Requires:	%{name}-core = %{EVRD}
Provides:	%{name}-apps
Obsoletes:	koffice-karbon
Obsoletes:	koffice2-karbon
Conflicts:	oxygen-icon-theme < 1:4.4.2-2
%rename		karbon

%description karbon
Karbon is a vector drawing application with an user interface that is easy to
use, highly customizable and extensible.
That makes Karbon a great application for users starting to explore the world
of vector graphics as well as for artists wanting to create breathtaking vector
art.

%files karbon
%defattr(0755,root,root,0755)
%{_bindir}/karbon
%{service calligra_filter_karbon1x2karbon}
%{service calligra_filter_karbon2svg}
%{service calligra_filter_karbon2wmf}
%{service calligra_filter_pdf2svg}
%{service calligra_filter_svg2karbon}
%_kde_services/calligra/calligra_filter_svgz2karbon.desktop
%{service calligra_filter_wmf2svg}
%{service calligra_filter_wpg2svg}
%{service calligra_filter_wpg2odg}
%{service calligra_filter_xfig2odg}
%optional %{_libdir}/kde4/calligra_filter_eps2svgai.so
%optional %{_datadir}/kde4/services/calligra/calligra_filter_eps2svgai.desktop
%{_libdir}/kde4/calligra_filter_karbon2image.so
%_kde_services/calligra/calligra_filter_karbon2jpg.desktop
%_kde_services/calligra/calligra_filter_karbon2png.desktop
%_kde_servicetypes/karbon_viewplugin.desktop
%_kde_servicetypes/karbon_dock.desktop
%{_libdir}/kde4/karbonfiltereffects.so
%{_libdir}/kde4/karbon_flattenpathplugin.so
%{_libdir}/kde4/karbon_whirlpinchplugin.so
%{_libdir}/kde4/karbontools.so
%{_libdir}/kde4/karbonpart.so
%{_libdir}/kde4/karbon_refinepathplugin.so
%{_libdir}/kde4/karbon_roundcornersplugin.so
%{_libdir}/libkdeinit4_karbon.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/karbon.desktop
%_kde_iconsdir/*/*/apps/calligrakarbon.*
%_kde_configdir/karbonrc
%{_kde_appsdir}/karbon
%{_datadir}/templates/Illustration.desktop
%{_datadir}/templates/.source/Illustration.odg
%{_datadir}/kde4/services/karbon_*_thumbnail.desktop
%_kde_services/ServiceMenus/calligra/karbon_print.desktop
%_kde_services/calligra/karbon*.desktop
%_kde_servicetypes/filtereffect.desktop
%{_datadir}/appdata/karbon.appdata.xml

#--------------------------------------------------------------------

%package kformula
Summary:	Formula Editor for calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
%rename		kformula

%description kformula
Kformula is a formula editor for kde project.

%files kformula
%{_datadir}/apps/formulashape
%{_kde_services}/calligra/kformulapart.desktop
%{service calligra_shape_formular}

#--------------------------------------------------------------------

%package flow
Summary:	Diagramming and flowcharting apps for calligra
Group:		Graphical desktop/KDE
URL:		http://www.calligra-suite.org/flow/
Requires:	%{name}-core = %{EVRD}
%rename		flow

%description flow
Use Flow to make network diagrams, organization charts, flowcharts and much
more. Flow also comes with numerous stencils that can be used to make anything
you want. There are options for Networking, Renewable Energy, Chemistry,
Building sites, and many other options to help you make your diagrams.

%files flow
%defattr(0755,root,root,0755)
%{_bindir}/calligraflow
%{_libdir}/kde4/flowdockersplugin.so
%{_libdir}/kde4/flowpart.so
%{service calligra_filter_vsdx2odg}
%{_libdir}/libkdeinit4_calligraflow.so
%defattr(0644,root,root,0755)
%{_datadir}/applications/kde4/flow.desktop
%{_datadir}/config/flowrc
%{_datadir}/config/flow_stencils.knsrc
%{_datadir}/appdata/flow.appdata.xml
%{_datadir}/kde4/services/flow_*_thumbnail.desktop
%{_kde_appsdir}/flow
%_kde_services/calligra/flowdockersplugin.desktop
%_kde_services/calligra/flowpart.desktop
%_kde_servicetypes/flow_dock.desktop
%_kde_services/ServiceMenus/calligra/flow_print.desktop
%_kde_iconsdir/hicolor/*/*/calligraflow*
#--------------------------------------------------------------------

%package kexi
Summary:	An integrated environment for managing data
Group:		Graphical desktop/KDE
URL:		http://www.calligra-suite.org/kexi/
Requires:	%{name}-core = %{EVRD}
Provides:	%{name}-apps
Obsoletes:	keximdb
%rename		kexi


%description kexi
Kexi is an integrated data management application.
It can be used for creating database schemas, inserting data, performing
queries, and processing data. Forms can be created to provide a custom
interface to your data. All database objects – tables, queries and forms –
are stored in the database, making it easy to share data and design.

%files kexi
%defattr(0755,root,root,0755)
%{_bindir}/kexi
%{_bindir}/kexi_sqlite3_dump
%{_libdir}/kde4/kformdesigner_containers.so
%optional %{_libdir}/kde4/kformdesigner_mapbrowser.so
%{_libdir}/kde4/kformdesigner_kexidbwidgets.so
%{_libdir}/kde4/kformdesigner_stdwidgets.so
%{_libdir}/kde4/kformdesigner_webbrowser.so
%{_libdir}/kde4/kexidb_pqxxsqldriver.so
%{_libdir}/kde4/kexidb_mysqldriver.so
%{_libdir}/kde4/kexidb_sqlite3driver.so
%{_libdir}/kde4/kexidb_sqlite3_icu.so
%{_libdir}/kde4/kexidb_sybasedriver.so
%{_libdir}/kde4/kexidb_xbasedriver.so
%{_libdir}/kde4/kexihandler_csv_importexport.so
%{_libdir}/kde4/kexihandler_form.so
%{_libdir}/kde4/kexihandler_migration.so
%{_libdir}/kde4/kexihandler_query.so
%{_libdir}/kde4/kexihandler_script.so
%{_libdir}/kde4/kexihandler_table.so
#%{_libdir}/kde4/keximigrate_kspread.so
%{_libdir}/kde4/keximigrate_mdb.so
%{_libdir}/kde4/keximigrate_mysql.so
%{_libdir}/kde4/keximigrate_pqxx.so
%{_libdir}/kde4/keximigrate_sybase.so
%{_libdir}/kde4/keximigrate_txt.so
%{_libdir}/kde4/keximigrate_spreadsheet.so
%{_libdir}/kde4/keximigrate_xbase.so
%{_libdir}/kde4/kexirelationdesignshape.so
%{_libdir}/kde4/krossmodulekexidb.so
%{_libdir}/kde4/kexihandler_report.so
%defattr(0644,root,root,0755)
%{_kde_appsdir}/kexi
%{_datadir}/config/kexirc
%{_kde_services}/calligra/kexi*.desktop
%{_kde_services}/calligra/kformdesigner_*.desktop
%{_kde_servicetypes}/widgetfactory.desktop
%{_kde_servicetypes}/calligradb_driver.desktop
%{_kde_servicetypes}/kexihandler.desktop
%{_kde_servicetypes}/keximigration_driver.desktop
%{_kde_applicationsdir}/kexi.desktop
%_kde_iconsdir/hicolor/*/*/calligrakexi*
%doc %_docdir/HTML/en/kexi
%{_datadir}/appdata/kexi.appdata.xml

#--------------------------------------------------------------------

%package okular-odp
Summary:	ODP file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular
%rename		okular-odp

%description okular-odp
ODP file renderer for Okular.

%files okular-odp
%defattr(0755,root,root,0755)
%{_libdir}/kde4/okularGenerator_odp.so
%defattr(0644,root,root,0755)
%_datadir/applications/kde4/okularApplication_odp.desktop
%_kde_services/libokularGenerator_odp.desktop
%_kde_services/okularOdp.desktop

#--------------------------------------------------------------------

%package okular-odt
Summary:	ODT file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-odt
ODT file renderer for Okular.

%files okular-odt
%defattr(0755,root,root,0755)
%{_libdir}/kde4/okularGenerator_odt.so
%defattr(0644,root,root,0755)
%_datadir/applications/kde4/okularApplication_odt.desktop
%_kde_services/libokularGenerator_odt.desktop
%_kde_services/okularOdt.desktop
%_datadir/kde4/services/calligra/okularDoc_calligra.desktop
%_datadir/kde4/services/calligra/okularDocx_calligra.desktop
%_datadir/kde4/services/calligra/okularWpd_calligra.desktop
%_kde_applicationsdir/okularApplication_doc_calligra.desktop
%_kde_applicationsdir/okularApplication_docx_calligra.desktop
%_kde_applicationsdir/okularApplication_wpd_calligra.desktop
%_datadir/kde4/services/calligra/libokularGenerator_doc_calligra.desktop
%_datadir/kde4/services/calligra/libokularGenerator_docx_calligra.desktop
%_datadir/kde4/services/calligra/libokularGenerator_wpd_calligra.desktop

#--------------------------------------------------------------------

%package stateshape
Summary:	State Shape
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
%rename		stateshape

%description stateshape
Calligra State Shape.

%files stateshape
%{_kde_appsdir}/stateshape
%_kde_iconsdir/hicolor/*/*/stateshape*
%_kde_iconsdir/hicolor/*/*/statetool*

#--------------------------------------------------------------------

%package webshape
Summary:	Calligra Web Shape
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
%rename		webshape

%description webshape
Calligra Web Shape.

%files webshape

#--------------------------------------------------------------------

%define libkomsooxml_major %{defaultmajor}
%define libkomsooxml %mklibname komsooxml %libkomsooxml_major

%package -n %{libkomsooxml}
Summary:	Calligra MS OOXML import library
Group:		System/Libraries

%description -n %{libkomsooxml}
Calligra MS OOXML import library.

%files -n %{libkomsooxml}
%defattr(-,root,root)
%{_libdir}/libkomsooxml.so.%{libkomsooxml_major}*

#--------------------------------------------------------------------

%define libkoodf_major %{defaultmajor}
%define libkoodf %mklibname koodf %libkoodf_major

%package -n %{libkoodf}
Summary:	Calligra ODF library
Group:		System/Libraries

%description -n %{libkoodf}
Calligra ODF library.

%files -n %{libkoodf}
%defattr(-,root,root)
%{_libdir}/libkoodf.so.%{libkoodf_major}*


#--------------------------------------------------------------------

%define libbraindumpcore_major %{defaultmajor}
%define libbraindumpcore %mklibname braindumpcore %libbraindumpcore_major

%package -n %{libbraindumpcore}
Summary:	Calligra Braindump core library
Group:	System/Libraries

%description -n %{libbraindumpcore}
Calligra Braindump core library.

%files -n %{libbraindumpcore}
%defattr(-,root,root)
%{_libdir}/libbraindumpcore.so.%{libbraindumpcore_major}*


#--------------------------------------------------------------------

%package braindump
Summary:	Calligra mind mapping tool
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	%{libbraindumpcore} = %{EVRD}
%rename		braindump

%description braindump
Braindump is a tool to dump and organize the content of your brain (ideas,
drawings, images, texts...) to your computer. It works by allowing to create
and edit whiteboards, which are infinite canvas on which you can add texts,
images, charts, drawings. You can also organize your ideas into diagrams
and flowcharts.

%files braindump
%{_bindir}/braindump
%_kde_applicationsdir/braindump.desktop
%{_kde_appsdir}/braindump
%_kde_servicetypes/braindump_extensions.desktop
%_kde_iconsdir/*/*/*/braindump.*
%{_datadir}/kde4/services/calligra/braindump_*.desktop
%{_libdir}/kde4/braindump_shape_*.so
%{_datadir}/appdata/braindump.appdata.xml

#--------------------------------------------------------------------
%if 1
%package active
Summary:	A document viewer for touch based tablets
Group:		Graphical desktop/KDE
Requires:	%{name}-words = %{EVRD}
Requires:	%{name}-sheets = %{EVRD}
Requires:	%{name}-stage = %{EVRD}

%description active
Calligra's QML UI.

%files active
%defattr(0755,root,root,0755)
%{_bindir}/calligraactive
%defattr(0644,root,root,0755)
%{_datadir}/applications/kde4/calligraactive.desktop
%{_datadir}/calligraactive
%endif
#--------------------------------------------------------------------

%define libkotextlayout_major %{defaultmajor}
%define libkotextlayout %mklibname kotextlayout %libkotextlayout_major

%package -n %{libkotextlayout}
Summary:	Calligra core library
Group:		System/Libraries

%description -n %{libkotextlayout}
Calligra core library.


%files -n %{libkotextlayout}
%defattr(-,root,root)
%{_libdir}/libkotextlayout.so.%{libkotextlayout_major}*

#--------------------------------------------------------------------

%define libcalligradb_major %{defaultmajor}
%define libcalligradb %mklibname calligradb %libcalligradb_major

%package -n %{libcalligradb}
Summary:	Calligra core library
Group:		System/Libraries

%description -n %{libcalligradb}
Calligra core library.

%files -n %{libcalligradb}
%{_libdir}/libcalligradb.so.%{libcalligradb_major}*


#----------------------------------------------------------------------

%define libkoreport_major %{defaultmajor}
%define libkoreport %mklibname koreport %libkoreport_major

%package -n %{libkoreport}
Summary:	Calligra core library
Group:		System/Libraries

%description -n %{libkoreport}
Calligra core library.
It's an application-independent reporting library for the generation of both
printed and ODS and HTML reports from various sources of data. It provides a
gui based designer and renderer, and is currently used by Kexi for the
generation of database reports, and Calligra Plan for the generation of
planning reports.

%files -n %{libkoreport}
%defattr(-,root,root)
%{_libdir}/libkoreport.so.%{libkoreport_major}*

#--------------------------------------------------------------------

%define libkokross_major %{defaultmajor}
%define libkokross %mklibname kokross %libkokross_major

%package -n %libkokross
Summary: Calligra core library
Group: System/Libraries

%description -n %libkokross
Calligra core library.

%files -n %libkokross
%defattr(-,root,root)
%{_libdir}/libkokross.so.%{libkokross_major}*

#--------------------------------------------------------------------

%define libkomain_major %{defaultmajor}
%define libkomain %mklibname komain %libkomain_major

%package -n %libkomain
Summary: Calligra core library
Group: System/Libraries
Suggests: %{name}-l10n

%description -n %libkomain
Calligra core library.

%files -n %libkomain
%defattr(-,root,root)
%{_libdir}/libkomain.so.%{libkomain_major}*

#--------------------------------------------------------------------

%define libkopageapp_major %{defaultmajor}
%define libkopageapp %mklibname kopageapp %libkopageapp_major

%package -n %libkopageapp
Summary: Calligra core library
Group: System/Libraries

%description -n %libkopageapp
Calligra core library.

%files -n %libkopageapp
%defattr(-,root,root)
%{_libdir}/libkopageapp.so.%{libkopageapp_major}*

#--------------------------------------------------------------------

%define libkotext_major %{defaultmajor}
%define libkotext %mklibname kotext %libkotext_major

%package -n %libkotext
Summary: Calligra core library
Group: System/Libraries

%description -n %libkotext
Calligra core library.
KoText is the library that offers rich text layout and OpenDocument Format
loading/saving. 

%files -n %libkotext
%defattr(-,root,root)
%{_libdir}/libkotext.so.%{libkotext_major}*

#--------------------------------------------------------------------
%define libkoodf2_major %{defaultmajor}
%define libkoodf2 %mklibname koodf2 %libkoodf2_major

%package -n %libkoodf2
Summary: Calligra core library
Group: System/Libraries

%description -n %libkoodf2
Calligra core library.
ODF Library

%files -n %libkoodf2
%defattr(-,root,root)
%{_libdir}/libkoodf2.so.%{libkoodf2_major}*

#--------------------------------------------------------------------

%define libbasicflakes_major %{defaultmajor}
%define libbasicflakes %mklibname basicflakes %libbasicflakes_major

%package -n %libbasicflakes
Summary: Calligra core library
Group: System/Libraries

%description -n %libbasicflakes
Calligra core library.
Flake is the object library for Calligra. It provides a basic concept of a
'shape' which can be a square, circle or any other form. The shape can contain
any sort of media because it is responsible for painting itself. This means
that Words can provide a textShape which has text flowing inside.

%files -n %libbasicflakes
%defattr(-,root,root)
%{_libdir}/libbasicflakes.so.%{libbasicflakes_major}*

#--------------------------------------------------------------------

%define libkordf_major %{defaultmajor}
%define libkordf %mklibname kordf %libkordf_major

%package -n %libkordf
Summary: Calligra core library
Group: System/Libraries

%description -n %libkordf
Calligra core library.

%files -n %libkordf
%defattr(-,root,root)
%{_libdir}/libkordf.so.%{libkordf_major}*

#--------------------------------------------------------------------

%define libkowidgetutils_major %{defaultmajor}
%define libkowidgetutils %mklibname kowidgetutils %libkowidgetutils_major

%package -n %libkowidgetutils
Summary: Calligra core library
Group: System/Libraries

%description -n %libkowidgetutils
Calligra core library.

%files -n %libkowidgetutils
%defattr(-,root,root)
%{_libdir}/libkowidgetutils.so.%{libkowidgetutils_major}*

#--------------------------------------------------------------------

%define libkoodfreader_major %{defaultmajor}
%define libkoodfreader %mklibname koodfreader %libkoodfreader_major

%package -n %libkoodfreader
Summary: Calligra core library
Group: System/Libraries

%description -n %libkoodfreader
Calligra core library.

%files -n %libkoodfreader
%defattr(-,root,root)
%{_libdir}/libkoodfreader.so.%{libkoodfreader_major}*

#--------------------------------------------------------------------

%define libflake_major %{defaultmajor}
%define libflake %mklibname flake %libflake_major

%package -n %libflake
Summary: Calligra core library
Group: System/Libraries

%description -n %libflake
Calligra core library.
Flake is the object library for Calligra. It provides a basic concept of a
'shape' which can be a square, circle or any other form. The shape can contain
any sort of media because it is responsible for painting itself. This means
that Words can provide a textShape which has text flowing inside.

%files -n %libflake
%defattr(-,root,root)
%{_libdir}/libflake.so.%{libflake_major}*

#--------------------------------------------------------------------

%define libpigmentcms_major %{defaultmajor}
%define libpigmentcms %mklibname pigmentcms %libpigmentcms_major

%package -n %libpigmentcms
Summary: Calligra core library
Group: System/Libraries
Obsoletes:   %{_lib}libpigmentpigment1 < 1:1.9.95.3-0.766453.1
Obsoletes:   %{_lib}libpigmentcms1 < 1:1.9.95.3-0.766453.1
Obsoletes:   %{_lib}libpigmentcms1 < 1:1.9.95.3-0.766453.1

%description -n %libpigmentcms
Calligra core library.
Pigment is the Color Manipulation System library for Calligra, this include but
it is not limited to full color management. Originating from Krita it provides
a generic KoColor class wich represents the notion of a color. The same color
can often be specified in different colorspaces. Some colors however can only
be specified in some colorspaces. 

%files -n %libpigmentcms
%defattr(-,root,root)
%{_libdir}/libpigmentcms.so.%{libpigmentcms_major}*

#--------------------------------------------------------------------

%define libkformdesigner_major %{defaultmajor}
%define libkformdesigner %mklibname kformdesigner %libkformdesigner_major

%package -n %libkformdesigner
Summary: Calligra core library
Group: System/Libraries

%description -n %libkformdesigner
Calligra core library.

%files -n %libkformdesigner
%defattr(-,root,root)
%{_libdir}/libkformdesigner.so.%{libkformdesigner_major}*

#--------------------------------------------------------------------

%define kundo2_major %{defaultmajor}
%define libkundo2 %mklibname kundo2_ %kundo2_major

%package -n %libkundo2
Summary: Calligra core library
Group: System/Libraries

%description -n %libkundo2
Calligra core library.

%files -n %libkundo2

%{_libdir}/libkundo2.so.%{kundo2_major}*

#--------------------------------------------------------------------
%define rtfreader_major %{defaultmajor}
%define librtfreader %mklibname rtfreader %rtfreader_major

%package -n %librtfreader
Summary: Calligra core library
Group: System/Libraries

%description -n %librtfreader
Calligra core library.

%files -n %librtfreader

%{_libdir}/libRtfReader.so.%{rtfreader_major}*

#--------------------------------------------------------------------

%define librcps_plan_major %{defaultmajor}
%define librcps_plan %mklibname rcps_plan %librcps_plan_major

%package -n %librcps_plan
Summary: Calligra core library
Group: System/Libraries

%description -n %librcps_plan
Calligra core library.

%files -n %librcps_plan
%{_libdir}/librcps_plan.so.%{librcps_plan_major}*

#--------------------------------------------------------------------

%define wordsprivate_major %{defaultmajor}
%define libwordsprivate %mklibname wordsprivate %wordsprivate_major

%package -n %libwordsprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libwordsprivate
Calligra core library.

%files -n %libwordsprivate
%defattr(-,root,root)
%{_libdir}/libwordsprivate.so.%{wordsprivate_major}*

#--------------------------------------------------------------------
%define kplatomodels_major %{defaultmajor}
%define  libkplatomodels %mklibname kplatomodels %kplatomodels_major

%package -n %libkplatomodels
Summary: Calligra core library
Group: System/Libraries

%description -n %libkplatomodels
Calligra core library.

%files -n %libkplatomodels
%defattr(-,root,root)
%{_libdir}/libkplatomodels.so.%{kplatomodels_major}*

#-------------------------------------------------------------------

%define  kplatokernel_major %{defaultmajor}
%define  libkplatokernel %mklibname kplatokernel %kplatokernel_major

%package -n %libkplatokernel
Summary: Calligra core library
Group: System/Libraries

%description -n %libkplatokernel
Calligra core library.

%files -n %libkplatokernel
%defattr(-,root,root)
%{_libdir}/libkplatokernel.so.%{kplatokernel_major}*

#--------------------------------------------------------------------

%define planprivate_major %{defaultmajor}
%define libplanprivate %mklibname planprivate %planprivate_major

%package -n %libplanprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libplanprivate
Calligra core library.

%files -n %libplanprivate
%defattr(-,root,root)
%{_libdir}/libplanprivate.so.%{planprivate_major}*

#--------------------------------------------------------------------

%define kplatoui_major %{defaultmajor}
%define libkplatoui %mklibname kplatoui %kplatoui_major

%package -n %libkplatoui
Summary: Calligra core library
Group: System/Libraries

%description -n %libkplatoui
Calligra core library.

%files -n %libkplatoui
%defattr(-,root,root)
%{_libdir}/libkplatoui.so.%{kplatoui_major}*

#--------------------------------------------------------------------

%define planworkapp_major %{defaultmajor}
%define libplanworkapp %mklibname planworkapp %planworkapp_major

%package -n %libplanworkapp
Summary: Calligra core library
Group: System/Libraries

%description -n %libplanworkapp
Calligra core library.

%files -n %libplanworkapp
%defattr(-,root,root)
%{_libdir}/libplanworkapp.so.%{planworkapp_major}*

#--------------------------------------------------------------------

%define kplatoworkfactory_major %{defaultmajor}
%define libplanworkfactory %mklibname kplatoworkfactory %kplatoworkfactory_major

%package -n %libplanworkfactory
Summary: Calligra core library
Group: System/Libraries
Obsoletes: %{_lib}kplatoworkapp8 < %{EVRD}

%description -n %libplanworkfactory
Calligra core library.

%files -n %libplanworkfactory
%defattr(-,root,root)
%{_libdir}/libplanworkfactory.so.%{kplatoworkfactory_major}*

#--------------------------------------------------------------------

%define sheets_major %{defaultmajor}
%define libcalligrasheetscommon %mklibname calligrasheetscommon %sheets_major

%package -n %libcalligrasheetscommon
Summary: Calligra core library
Group: System/Libraries
Obsoletes: %mklibname calligratablescommon 9

%description -n %libcalligrasheetscommon
Calligra core library.

%files -n %libcalligrasheetscommon
%defattr(-,root,root)
%{_libdir}/libcalligrasheetscommon.so.%{sheets_major}*

#--------------------------------------------------------------------

%define sheetsodf_major %{defaultmajor}
%define libcalligrasheetsodf %mklibname calligrasheetsodf %sheetsodf_major

%package -n %libcalligrasheetsodf
Summary: Calligra core library
Group: System/Libraries
Obsoletes: %mklibname calligratablesodf 9

%description -n %libcalligrasheetsodf
Calligra core library.

%files -n %libcalligrasheetsodf
%defattr(-,root,root)
%{_libdir}/libcalligrasheetsodf.so.%{sheetsodf_major}*

#--------------------------------------------------------------------

%define calligrastageprivate_major %{defaultmajor}
%define libcalligrastageprivate %mklibname calligrastageprivate %calligrastageprivate_major

%package -n %libcalligrastageprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libcalligrastageprivate
Calligra core library.

%files -n %libcalligrastageprivate
%defattr(-,root,root)
%{_libdir}/libcalligrastageprivate.so.%{calligrastageprivate_major}*

#--------------------------------------------------------------------

%define  calligrakdchart_major %{defaultmajor}
%define  libcalligrakdchart %mklibname calligrakdchart  %calligrakdchart_major

%package -n %libcalligrakdchart
Summary: Calligra chart library
Group: System/Libraries

%description -n %libcalligrakdchart
Calligra chart library.

%files -n %libcalligrakdchart
%defattr(-,root,root)
%{_libdir}/libcalligrakdchart.so.%{calligrakdchart_major}*

#--------------------------------------------------------------------

%define libcalligrakdgantt_major %{defaultmajor}
%define libcalligrakdgantt %mklibname calligrakdgantt %libcalligrakdgantt_major

%package -n %libcalligrakdgantt
Summary: Calligra Gantt library
Group: System/Libraries

%description -n %libcalligrakdgantt
Calligra Gantt library.

%files -n %libcalligrakdgantt
%{_libdir}/libcalligrakdgantt.so.%{libcalligrakdgantt_major}*


#--------------------------------------------------------------------

%package katelier
Summary:	Krita and karbon meta package
Group:		Graphical desktop/KDE
Requires:	%{name}-krita = %{EVRD}
Requires:	%{name}-karbon = %{EVRD}

%description katelier
Krita and karbon meta package

%files katelier

#--------------------------------------------------------------------

%define  libkritaui_major %{defaultmajor}
%define  libkritaui %mklibname kritaui  %libkritaui_major

%package -n %libkritaui
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritaui
Calligra core library.

%files -n %libkritaui
%defattr(-,root,root)
%{_libdir}/libkritaui.so.%{libkritaui_major}*

#--------------------------------------------------------------------

%define  libkritaimage_major %{defaultmajor}
%define  libkritaimage %mklibname kritaimage  %libkritaimage_major

%package -n %libkritaimage
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritaimage
Calligra core library.

%files -n %libkritaimage
%defattr(-,root,root)
%{_libdir}/libkritaimage.so.%{libkritaimage_major}*

#--------------------------------------------------------------------

%define  libkritalibbrush_major %{defaultmajor}
%define  libkritalibbrush %mklibname kritalibbrush  %libkritalibbrush_major

%package -n %libkritalibbrush
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritalibbrush
Calligra core library.

%files -n %libkritalibbrush
%defattr(-,root,root)
%{_libdir}/libkritalibbrush.so.%{libkritalibbrush_major}*

#--------------------------------------------------------------------

%define  libkritalibpaintop_major %{defaultmajor}
%define  libkritalibpaintop %mklibname kritalibpaintop  %libkritalibpaintop_major

%package -n %libkritalibpaintop
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritalibpaintop
Calligra core library.

%files -n %libkritalibpaintop
%defattr(-,root,root)
%{_libdir}/libkritalibpaintop.so.%{libkritalibpaintop_major}*

#--------------------------------------------------------------------

%define  libkoplugin_major %{defaultmajor}
%define  libkoplugin %mklibname koplugin  %libkoplugin_major

%package -n %libkoplugin
Summary: Calligra core library
Group: System/Libraries

%description -n %libkoplugin
Calligra core library.

%files -n %libkoplugin
%defattr(-,root,root)
%{_libdir}/libkoplugin.so.%{libkoplugin_major}*

#--------------------------------------------------------------------

%define  libkowidgets_major %{defaultmajor}
%define  libkowidgets %mklibname kowidgets  %libkowidgets_major
#
%package -n %libkowidgets
Summary: Calligra core library
Group: System/Libraries

%description -n %libkowidgets
Calligra core library.

%files -n %libkowidgets
%defattr(-,root,root)
%{_libdir}/libkowidgets.so.%{libkowidgets_major}*

#--------------------------------------------------------------------


%define  karboncommon_major %{defaultmajor}
%define  libkarboncommon %mklibname karboncommon  %karboncommon_major

%package -n %libkarboncommon
Summary: Calligra core library
Group: System/Libraries

%description -n %libkarboncommon
Calligra core library.

%files -n %libkarboncommon
%defattr(-,root,root)
%{_libdir}/libkarboncommon.so.%{karboncommon_major}*

#--------------------------------------------------------------------

%define  karbonui_major %{defaultmajor}
%define  libkarbonui %mklibname karbonui  %karbonui_major

%package -n %libkarbonui
Summary: Calligra core library
Group: System/Libraries

%description -n %libkarbonui
Calligra core library.

%files -n %libkarbonui
%defattr(-,root,root)
%{_libdir}/libkarbonui.so.%{karbonui_major}*

#--------------------------------------------------------------------

%define libkformula_major %{defaultmajor}
%define libkformula %mklibname kformula %libkformula_major

%package -n %libkformula
Summary: Calligra core library
Group: System/Libraries

%description -n %libkformula
Calligra core library.

%files -n %libkformula
%defattr(-,root,root)
%{_libdir}/libkformula.so.%{libkformula_major}*

#--------------------------------------------------------------------
   
%define libkexicore_major %{defaultmajor}
%define libkexicore %mklibname kexicore %libkexicore_major
   
%package -n %libkexicore
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexicore
Calligra core library.

%files -n %libkexicore
%defattr(-,root,root)
%{_libdir}/libkexicore.so.%{libkexicore_major}*

#--------------------------------------------------------------------

%define libkexidatatable_major %{defaultmajor}
%define libkexidatatable %mklibname kexidatatable %libkexidatatable_major

%package -n %libkexidatatable
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexidatatable
Calligra core library.

%files -n %libkexidatatable
%defattr(-,root,root)
%{_libdir}/libkexidatatable.so.%{libkexidatatable_major}*

#--------------------------------------------------------------------

%define libkexidb_major %{defaultmajor}
%define libkexidb %mklibname kexidb %libkexidb_major

%package -n %libkexidb
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexidb
Calligra core library.

%files -n %libkexidb
%defattr(-,root,root)
%{_libdir}/libkexidb.so.%{libkexidb_major}*

#--------------------------------------------------------------------

%define libkexiextendedwidgets_major %{defaultmajor}
%define libkexiextendedwidgets %mklibname kexiextendedwidgets %libkexiextendedwidgets_major

%package -n %libkexiextendedwidgets
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexiextendedwidgets
Calligra core library.

%files -n %libkexiextendedwidgets
%defattr(-,root,root)
%{_libdir}/libkexiextendedwidgets.so.%{libkexiextendedwidgets_major}*

#--------------------------------------------------------------------

%define libkexiformutils_major %{defaultmajor}
%define libkexiformutils %mklibname kexiformutils %libkexiformutils_major

%package -n %libkexiformutils
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexiformutils
Calligra core library.

%files -n %libkexiformutils
%defattr(-,root,root)
%{_libdir}/libkexiformutils.so.%{libkexiformutils_major}*

#--------------------------------------------------------------------

%define libkeximain_major %{defaultmajor}
%define libkeximain %mklibname keximain %libkeximain_major

%package -n %libkeximain
Summary: Calligra core library
Group: System/Libraries

%description -n %libkeximain
Calligra core library.

%files -n %libkeximain
%defattr(-,root,root)
%{_libdir}/libkeximain.so.%{libkeximain_major}*

#--------------------------------------------------------------------

%define libkeximigrate_major %{defaultmajor}
%define libkeximigrate %mklibname keximigrate %libkeximigrate_major

%package -n %libkeximigrate
Summary: Calligra core library
Group: System/Libraries

%description -n %libkeximigrate
Calligra core library.

%files -n %libkeximigrate
%defattr(-,root,root)
%{_libdir}/libkeximigrate.so.%{libkeximigrate_major}*

#--------------------------------------------------------------------

%define libkexirelationsview_major %{defaultmajor}
%define libkexirelationsview %mklibname kexirelationsview %libkexirelationsview_major

%package -n %libkexirelationsview
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexirelationsview
Calligra core library.

%files -n %libkexirelationsview
%defattr(-,root,root)
%{_libdir}/libkexirelationsview.so.%{libkexirelationsview_major}*

#--------------------------------------------------------------------

%define libkexiutils_major %{defaultmajor}
%define libkexiutils %mklibname kexiutils %libkexiutils_major
   
%package -n %libkexiutils
Summary: Calligra core library
Group: System/Libraries
   
%description -n %libkexiutils
Calligra core library.
   
%files -n %libkexiutils
%defattr(-,root,root)
%{_libdir}/libkexiutils.so.%{libkexiutils_major}*

#--------------------------------------------------------------------

%define libkexiguiutils_major %{defaultmajor}
%define libkexiguiutils %mklibname kexiguiutils %libkexiguiutils_major

%package -n %libkexiguiutils
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexiguiutils
Calligra core library.

%files -n %libkexiguiutils
%defattr(-,root,root)
%{_libdir}/libkexiguiutils.so.%{libkexiguiutils_major}*

#--------------------------------------------------------------------

%define libkexidataviewcommon_major %{defaultmajor}
%define libkexidataviewcommon %mklibname kexidataviewcommon %libkexidataviewcommon_major

%package -n %libkexidataviewcommon
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexidataviewcommon
Calligra core library.

%files -n %libkexidataviewcommon
%defattr(-,root,root)
%{_libdir}/libkexidataviewcommon.so.%{libkexidataviewcommon_major}*

#-------------------------------------------------------------------- 

%define libkowv2_major 9
%define libkowv2 %mklibname kowv2_ %libkowv2_major
   
%package -n %libkowv2
Summary: Calligra core library
Group: System/Libraries
   
%description -n %libkowv2
Calligra core library.
   
%files -n %libkowv2
%defattr(-,root,root)
%{_libdir}/libkowv2.so.%{libkowv2_major}*

#--------------------------------------------------------------------

%define libkoproperty_major %{defaultmajor}
%define libkoproperty %mklibname koproperty %libkoproperty_major
   
%package -n %libkoproperty
Summary: Calligra core library
Group: System/Libraries
   
%description -n %libkoproperty
Calligra core library.
   
%files -n %libkoproperty
%defattr(-,root,root)
%{_libdir}/libkoproperty.so.%{libkoproperty_major}*

#--------------------------------------------------------------------

%define libflowprivate_major %{defaultmajor}
%define libflowprivate %mklibname flowprivate %libflowprivate_major

%package -n %libflowprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libflowprivate
Calligra core library.

%files -n %libflowprivate
%defattr(-,root,root)
%{_libdir}/libflowprivate.so.%{libflowprivate_major}*

#--------------------------------------------------------------------

%define kovectorimage_major %{defaultmajor}
%define libkovectorimage %mklibname kovectorimage %kovectorimage_major

%package -n %libkovectorimage
Summary: Calligra core library
Group: System/Libraries

%description -n %libkovectorimage
Calligra core library.

%files -n %libkovectorimage
%{_libdir}/libkovectorimage.so.%{kovectorimage_major}*

#--------------------------------------------------------------------

%package devel
Group:		Development/KDE and Qt
Summary:	Header files for developing calligra applications
Requires:	%libflake = %{EVRD}
Requires:	%libcalligrakdgantt = %{EVRD} 
Requires:	%libkarboncommon = %{EVRD}
Requires:	%libkarbonui = %{EVRD}
Requires:	%libcalligrakdchart = %{EVRD}
Requires:	%libkexicore = %{EVRD}
Requires:	%libkexidatatable = %{EVRD}
Requires:	%libkexidataviewcommon = %{EVRD}
Requires:	%libkexidb = %{EVRD}
Requires:	%libkexiextendedwidgets = %{EVRD}
Requires:	%libkexiformutils = %{EVRD}
Requires:	%libkexiguiutils = %{EVRD}
Requires:	%libkeximain = %{EVRD}
Requires:	%libkeximigrate = %{EVRD}
Requires:	%libkexirelationsview = %{EVRD}
Requires:	%libkexiutils = %{EVRD}
Requires:	%libkformdesigner = %{EVRD}
Requires:	%libkformula = %{EVRD}
Requires:	%libkokross = %{EVRD}
Requires:	%libkomain = %{EVRD}
Requires:	%libkoodf2 = %{EVRD}
Requires:	%libkopageapp = %{EVRD}
Requires:	%libkoplugin = %{EVRD}
Requires:	%libkoproperty = %{EVRD}
Requires:	%libkoreport = %{EVRD}
Requires:	%libkotext = %{EVRD}
Requires:	%libkowidgets = %{EVRD}
Requires:	%libkowv2 = %{EVRD}
Requires:	%libkplatokernel = %{EVRD}
Requires:	%libkplatomodels = %{EVRD}
Requires:	%libplanprivate = %{EVRD}
Requires:	%libkplatoui = %{EVRD}
Requires:	%libplanworkapp = %{EVRD}
Requires:	%libplanworkfactory = %{EVRD}
Requires:	%libcalligrastageprivate = %{EVRD}
Requires:	%libkritaimage = %{EVRD}
Requires:	%libkritalibbrush = %{EVRD}
Requires:	%libkritalibpaintop = %{EVRD}
Requires:	%libkritaui = %{EVRD}
Requires:	%libcalligradb = %{EVRD}
Requires:	%libcalligrasheetscommon = %{EVRD}
Requires:	%libcalligrasheetsodf = %{EVRD}
Requires:	%libwordsprivate = %{EVRD}
Requires:	%libkovectorimage = %{EVRD}
Requires:	%libpigmentcms = %{EVRD}
Requires:	%libkundo2 = %{EVRD}
Requires:	%librtfreader = %{EVRD}
Requires:	%librcps_plan = %{EVRD}
Requires:	%{name}-core = %{EVRD}
Conflicts:	karbon < 11:1.9.95.8-3
Conflicts:	kchart < 11:1.9.95.8-3
Conflicts:	kivio < 11:1.9.95.8-3
Conflicts:	kplato < 11:1.9.95.8-3
Conflicts:	kpresenter < 11:1.9.95.8-3
Conflicts:	krita < 11:1.9.95.8-3
Conflicts:	kspread < 11:1.9.95.8-3
Conflicts:	koffice-core < 11:1.9.98.5-3
Conflicts:	kword < 11:1.9.95.8-3
Obsoletes:	koffice2-devel
Obsoletes:	koffice-devel

%description devel
Header files needed for developing calligra applications.

%files devel
%defattr(-,root,root)
%{_kde_appsdir}/cmake/*/*
%_kde_includedir/*
%{_libdir}/libkomsooxml.so
%{_libdir}/libkoodf.so
%{_libdir}/libcalligradb.so
%{_libdir}/libbasicflakes.so
%{_libdir}/libflake.so
%{_libdir}/libkoodfreader.so
%{_libdir}/libkotextlayout.so
%{_libdir}/libkovectorimage.so
%{_libdir}/libkarboncommon.so
%{_libdir}/libkarbonui.so
%{_libdir}/libkordf.so
%{_libdir}/libkoversion.so
%{_libdir}/libkowidgetutils.so
%{_libdir}/libkritacolor.so
%{_libdir}/libkritacolord.so
%{_libdir}/libkritasketchlib.so
%{_libdir}/libcalligrakdchart.so
%{_libdir}/libcalligrakdgantt.so
%{_libdir}/libkexicore.so
%{_libdir}/libkexidatatable.so
%{_libdir}/libkexidataviewcommon.so
%{_libdir}/libkexidb.so
%{_libdir}/libkexiextendedwidgets.so
%{_libdir}/libkexiformutils.so
%{_libdir}/libkexiguiutils.so
%{_libdir}/libkeximain.so
%{_libdir}/libkeximigrate.so
%{_libdir}/libkexirelationsview.so
%{_libdir}/libkexiutils.so
%{_libdir}/libkformdesigner.so
%{_libdir}/libkformula.so
%{_libdir}/libkokross.so
%{_libdir}/libkomain.so
%{_libdir}/libkoodf2.so
%{_libdir}/libkopageapp.so
%{_libdir}/libkoplugin.so
%{_libdir}/libkoproperty.so
%{_libdir}/libkoreport.so
%{_libdir}/libkotext.so
%{_libdir}/libkowidgets.so
%{_libdir}/libkowv2.so
%{_libdir}/libkplatokernel.so
%{_libdir}/libkplatomodels.so
%{_libdir}/libplanprivate.so
%{_libdir}/libkplatoui.so
%{_libdir}/libplanworkapp.so
%{_libdir}/libplanworkfactory.so
%{_libdir}/libcalligrastageprivate.so
%{_libdir}/libkritaimage.so
%{_libdir}/libkritalibbrush.so
%{_libdir}/libkritalibpaintop.so
%{_libdir}/libkritaui.so
%{_libdir}/libcalligrasheetscommon.so
%{_libdir}/libcalligrasheetsodf.so
%{_libdir}/libwordsprivate.so
%{_libdir}/libpigmentcms.so
%{_libdir}/libflowprivate.so
%{_libdir}/libkundo2.so
%{_libdir}/libRtfReader.so
%{_libdir}/librcps_plan.so

#--------------------------------------------------------------------
%if %_mobile
%package mobile
Summary:	mobile user interaction of Calligra Suite
Group:		Graphical desktop/KDE

%description mobile
Calligra Mobile is a mobile user interaction of Calligra Suite.

%files mobile
%defattr(0755,root,root,0755)
%{_bindir}/calligramobile
%defattr(0644,root,root,0755)
%{_datadir}/applications/hildon/calligramobile.desktop
%{_datadir}/calligramobile-templates/
%{_datadir}/dbus-1/services/com.nokia.CalligraMobile.service
%_kde_iconsdir/hicolor/178x200/apps/calligramobile.png
%_kde_iconsdir/hicolor/48x48/hildon/Document.png
%_kde_iconsdir/hicolor/48x48/hildon/Presenter.png
%_kde_iconsdir/hicolor/48x48/hildon/SpreadSheet.png
%_kde_iconsdir/hicolor/64x64/apps/calligramobile.png

%endif
#--------------------------------------------------------------------

%prep
%setup -q
%patch2 -p0 -b .xbase312~
%patch3 -p1 -b .staging~
%patch4 -p1 -b .libpqxx~

%build
# clang build causes issues with pigment
# and libvc
export CXX=g++
export CC=gcc
#sh initrepo.sh
%if %_mobile
%cmake_kde4 -DIHAVEPATCHEDQT:BOOL=TRUE -DCALLIGRA_SHOULD_BUILD_STAGING:BOOL=ON -DPACKAGERS_BUILD=ON
%else
%cmake_kde4 -Wno-dev -DBUILD_mobile=OFF -DIHAVEPATCHEDQT:BOOL=TRUE -DCALLIGRA_SHOULD_BUILD_STAGING:BOOL=ON -DPACKAGERS_BUILD=ON
%endif
%make

%if %{compile_apidox}
%make apidox
%endif

%install
%makeinstall_std -C build

%if %compile_apidox
make install-apidox DESTDIR=%{buildroot}/
list=`ls -d */ -1`;
echo $list;
for i in $list ; do
	cd $i;
		if grep '^include .*Doxyfile.am' Makefile.am; then
			echo "installing apidox from $i" ;	
			make install-apidox DESTDIR=%{buildroot}/ ; 
		fi
	cd ../;
done;
%endif

# Remove shebang from non-executable files
find %{buildroot}%{_kde_appsdir}/ -type f -name '*.py' -exec sed -i '1s/^#!.*$//' {} \;
