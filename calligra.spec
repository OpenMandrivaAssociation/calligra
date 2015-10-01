%define compile_apidox 0
%define _mobile 0
%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define major 14

%define service(s) %{_libdir}/kde4/%{1}.so \
%{_datadir}/kde4/services/calligra/%{1}.desktop
%define optional_service(s) %optional %{_libdir}/kde4/%{1}.so \
%optional %{_datadir}/kde4/services/calligra/%{1}.desktop
%define kservice(s) %{_libdir}/kde4/%{1}.so \
%{_datadir}/kde4/services/%{1}.desktop

Summary:	Set of office applications for KDE
Name:		calligra
#koffice has epoch 15. We need a higher epoch
Epoch:		16
Version:	2.9.7
Release:	6
Group:		Office
License:	GPLv2+ and LGPLv2+ and GFDL
Url:		http://www.calligra.org
Source0:	http://download.kde.org/stable/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch2:		calligra-2.6.0-xbase-3.1.2.patch
Patch3:		calligra-optionize-staging.patch
Patch4:		calligra-2.8.0-libpqxx-4.0.patch
Patch5:		0001-adapt-to-libwps-0.4.patch
BuildRequires:	pstoedit
BuildRequires:	boost-devel
BuildRequires:	freetds-devel
BuildRequires:	getfem-devel
BuildRequires:	glpk-devel
BuildRequires:	gmic-devel
BuildRequires:	jbig-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	marble-devel
BuildRequires:	mysql-devel
BuildRequires:	nepomuk-core-devel
BuildRequires:	nepomuk-widgets-devel
BuildRequires:	okular-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	tiff-devel
BuildRequires:	vc-devel
BuildRequires:	xbase-devel
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:	pkgconfig(OpenColorIO)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libctemplate)
BuildRequires:	pkgconfig(libetonyek-0.1)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libkdcraw)
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(libodfgen-0.1)
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(libpqxx)
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(libvisio-0.1)
BuildRequires:	pkgconfig(libwpd-0.10)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libwps-0.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(sqlite3)
%if %compile_apidox
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
Suggests:	%{name}-braindump
Suggests:	%{name}-flow
Suggests:	%{name}-karbon
Suggests:	%{name}-kchart
Suggests:	%{name}-kexi
Suggests:	%{name}-kformula
Suggests:	%{name}-krita
Suggests:	%{name}-plan
Suggests:	%{name}-sheets
Suggests:	%{name}-stage
Suggests:	%{name}-words

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
### MD the libpackage macro is missing a few bits.
### this fixes a couple until a better solution is found
%define libpackage()\
%{expand:%%define nib %(echo %{1} | sed 's,[0-9]$,&_,' )}\
%{expand:%%global lib%{1} %%mklibname %{nib} %{2}}\
%%package -n %{expand:%{lib%{1}}}\
Summary: The %{1} library, a part of %{name}\
Group: System/Libraries\
%%description -n %{expand:%{lib%{1}}}\
The %{1} library, a part of %{name}.\
%%files -n %{expand:%{lib%{1}}}\
%{_libdir}/lib%{1}.so.%{2}*\
%{nil}

# libpackages
%define calligralibs basicflakes calligradb calligrakdchart calligrakdgantt calligrasheetscommon calligrasheetsodf calligrastageprivate flake flowprivate karboncommon karbonui kexicore kexidatatable kexidataviewcommon kexidb kexiextendedwidgets kexiformutils kexiguiutils keximain keximigrate kexirelationsview kexiutils kformdesigner kformula kokross komain komsooxml koodf koodfreader kopageapp koplugin koproperty kordf koreport kotext kotextlayout kovectorimage koversion kowidgets kowidgetutils kplatokernel kplatomodels kplatoui kritacolor kritaglobal kritaimage kritalibbrush kritalibpaintop kritapsd kritaui kundo2 pigmentcms planprivate planworkapp rcps_plan wordsprivate
%{expand:%(for lib in %{calligralibs}; do cat <<EOF
%%libpackage $lib %{major}
EOF
done)}
%libpackage kowv2 9
# MD there is no devel library for braindumpcore
%libpackage braindumpcore %{major}

#--------------------------------------------------------------------

%define libkoodf2 %mklibname koodf2 %{major}

%package -n %{libkoodf2}
Summary:        Calligra library
Group:          System/Libraries
%rename %{_lib}koodf214

%description -n %{libkoodf2}
Calligra library.

%files -n %{libkoodf2}
%{_libdir}/libkoodf2.so.%{major}*

#--------------------------------------------------------------------

%define libRtfReader %mklibname RtfReader %{major}

%package -n %{libRtfReader}
Summary:        Calligra library
Group:          System/Libraries
%rename %{_lib}rtfreader14

%description -n %{libRtfReader}
Calligra library.

%files -n %{libRtfReader}
%{_libdir}/libRtfReader.so.%{major}*

#--------------------------------------------------------------------

%define libplanworkfactory %mklibname planworkfactory %{major}

%package -n %{libplanworkfactory}
Summary:        Calligra library
Group:          System/Libraries
%rename	%{_lib}kplatoworkfactory14

%description -n %{libplanworkfactory}
Calligra library.

%files -n %{libplanworkfactory}
%{_libdir}/libplanworkfactory.so.%{major}*

#--------------------------------------------------------------------

# MD This lib is missing a soname, but it is req'd by libkritacolor
# and causing the devel pkg to be install by default.
%define libkritacolord %mklibname kritacolord

%package -n %{libkritacolord}
Summary:	Calligra library
Group:		System/Libraries
Conflicts:	%{name}-devel < 16:2.9.7-2

%description -n %{libkritacolord}
Calligra library.

%files -n %{libkritacolord}
%{_libdir}/libkritacolord.so

#--------------------------------------------------------------------

%package core
Group:		Office
Summary:	Set of office applications for KDE
Obsoletes:	koffice-core < 15:2.4
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
%{_libdir}/calligra/imports/org/calligra/CalligraComponents
%{_libdir}/kde4/calligraimagethumbnail.so
%{_libdir}/kde4/calligrathumbnail.so
%{service calligra_docker_defaults}
%{service calligra_shape_artistictext}
%{service calligra_shape_music}
%{service calligra_shape_paths}
%{service calligra_shape_picture}
%{service calligra_shape_plugin}
%{service calligra_shape_text}
%{service calligra_shape_threed}
%{service calligra_shape_vector}
%{service calligra_shape_video}
%{service calligra_textediting_autocorrect}
%{service calligra_textediting_changecase}
%{service calligra_textediting_spellcheck}
%{service calligra_textediting_thesaurus}
%{service calligra_textinlineobject_variables}
%{service calligra_tool_basicflakes}
%{service calligra_tool_defaults}
%{service calligradocinfopropspage}
%{service kolcmsengine}
%{service kopabackgroundtool}
%{service koreport_barcodeplugin}
%{service koreport_chartplugin}
%{optional_service koreport_mapsplugin}
%{service koreport_webplugin}
%defattr(0644,root,root,0755)
%doc %{_kde_docdir}/HTML/en/calligra
%optional %{_datadir}/kde4/services/calligra/calligra_docker_textdocumentinspection.desktop
%{_datadir}/kde4/servicetypes/kopa_tool.desktop
%{_datadir}/kde4/servicetypes/kpr_tool.desktop
%{_datadir}/mime/packages/calligra_svm.xml
%{_datadir}/mime/packages/msooxml-all.xml
%{_iconsdir}/*/*/*/insert-tableofcontents.*
%{_kde_applicationsdir}/calligra.desktop
%{_kde_appsdir}/calligra
%{_kde_appsdir}/koproperty
%{_kde_appsdir}/musicshape
%{_kde_iconsdir}/*/*/actions/black.*
%{_kde_iconsdir}/*/*/actions/curve-connector.*
%{_kde_iconsdir}/*/*/actions/highlight.*
%{_kde_iconsdir}/*/*/actions/insert-endnote.png
%{_kde_iconsdir}/*/*/actions/insert-footnote.png
%{_kde_iconsdir}/*/*/actions/lines-connector.png
%{_kde_iconsdir}/*/*/actions/object-align-horizontal-center-calligra.*
%{_kde_iconsdir}/*/*/actions/object-align-horizontal-left-calligra.*
%{_kde_iconsdir}/*/*/actions/object-align-horizontal-right-calligra.*
%{_kde_iconsdir}/*/*/actions/object-align-vertical-bottom-calligra.*
%{_kde_iconsdir}/*/*/actions/object-align-vertical-bottom-top-calligra.*
%{_kde_iconsdir}/*/*/actions/object-align-vertical-center-calligra.*
%{_kde_iconsdir}/*/*/actions/object-align-vertical-top-calligra.*
%{_kde_iconsdir}/*/*/actions/object-group-calligra.*
%{_kde_iconsdir}/*/*/actions/object-order-back-calligra.*
%{_kde_iconsdir}/*/*/actions/object-order-front-calligra.*
%{_kde_iconsdir}/*/*/actions/object-order-lower-calligra.*
%{_kde_iconsdir}/*/*/actions/object-order-raise-calligra.*
%{_kde_iconsdir}/*/*/actions/object-ungroup-calligra.*
%{_kde_iconsdir}/*/*/actions/pen.*
%{_kde_iconsdir}/*/*/actions/shape-choose.* 
%{_kde_iconsdir}/*/*/actions/standard-connector.*
%{_kde_iconsdir}/*/*/actions/straight-connector.*
%{_kde_iconsdir}/*/*/actions/table.*
%{_kde_iconsdir}/*/*/actions/x-shape-connection.*
%{_kde_iconsdir}/*/*/actions/x-shape-formula.*
%{_kde_iconsdir}/*/*/actions/x-shape-image.*
%{_kde_iconsdir}/*/*/actions/x-shape-text.*
%{_kde_services}/calligra_odg_thumbnail.desktop
%{_kde_servicetypes}/calligra_application.desktop
%{_kde_servicetypes}/calligra_deferred_plugin.desktop
%{_kde_servicetypes}/calligra_filter.desktop
%{_kde_servicetypes}/calligra_part.desktop
%{_kde_servicetypes}/calligradocker.desktop
%{_kde_servicetypes}/flake.desktop
%{_kde_servicetypes}/flakedevice.desktop
%{_kde_servicetypes}/flakeshape.desktop
%{_kde_servicetypes}/flaketool.desktop
%{_kde_servicetypes}/inlinetextobject.desktop
%{_kde_servicetypes}/koreport_itemplugin.desktop
%{_kde_servicetypes}/pigment.desktop
%{_kde_servicetypes}/pigmentextension.desktop
%{_kde_servicetypes}/scripteventaction.desktop
%{_kde_servicetypes}/texteditingplugin.desktop

#--------------------------------------------------------------------

%package semanticitem
Group:		Office
Summary:	RDF Support for %{name}
Requires:	%{name}-core = %{EVRD}
Obsoletes:	koffice-core < 15:2.4
Conflicts:	core < 16:2.9.7-2

%description semanticitem
RDF Support for %{name}.

%files semanticitem
%{_kde_servicetypes}/calligra_semanticitem.desktop
%{service calligra_semanticitem_contact}
%{service calligra_semanticitem_event}
%{service calligra_semanticitem_location}

#--------------------------------------------------------------------

%package words
Summary:	Word processor for calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	wordnet

%description    words
Words is an intuitive word processor application with desktop publishing
features.
With it, you can create informative and attractive documents with ease.

%files words
%defattr(755,root,root)
%{_bindir}/calligrawords
%{_datadir}/applications/kde4/calligrawords_ascii.desktop
%{_datadir}/kde4/services/words_*_thumbnail.desktop
%{_datadir}/mime/packages/wiki-format.xml
%{_libdir}/kde4/wordspart.so
%{_libdir}/libkdeinit4_calligrawords.so
%{kservice calligra_filter_odt2wiki}
%{service calligra_filter_applixword2odt}
%{service calligra_filter_ascii2words}
%{service calligra_filter_doc2odt}
%{service calligra_filter_docx2odt}
%{service calligra_filter_odt2ascii}
%{service calligra_filter_odt2docx}
%{service calligra_filter_odt2epub2}
%{service calligra_filter_odt2html}
%{service calligra_filter_odt2mobi}
%{service calligra_filter_rtf2odt}
%{service calligra_filter_wpd2odt}
%{service calligra_filter_wps2odt}
%defattr(0644,root,root,0755)
%{_datadir}/appdata/words.appdata.xml
%{_datadir}/templates/.source/TextDocument.odt
%{_datadir}/templates/TextDocument.desktop
%{_kde_applicationsdir}/words.desktop
%{_kde_appsdir}/words
%{_kde_configdir}/wordsrc
%{_kde_iconsdir}/hicolor/*/*/calligraauthor*
%{_kde_iconsdir}/hicolor/*/*/calligrawords*
%{_kde_iconsdir}/hicolor/*/actions/tool_pagelayout.*
%{_kde_services}/ServiceMenus/calligra/words_print.desktop
%{_kde_services}/calligra/words*.desktop

#--------------------------------------------------------------------

%package author
Summary:	Write ebooks and textbooks
Group:		Office
Requires:	%{name}-words = %{EVRD}

%description author
Write ebooks and textbooks.

%files author
%{_bindir}/calligraauthor
%{_libdir}/libkdeinit4_calligraauthor.so
%{_kde_applicationsdir}/author.desktop
%{_kde_appsdir}/author
%{_kde_configdir}/authorrc
%{service authorpart}

#--------------------------------------------------------------------

%package plan
Summary:	Project management application for Calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
# For M$ Project import filter
BuildRequires:	java-devel-openjdk
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
%{_libdir}/kde4/planicalexport.so
%{_libdir}/kde4/plankplatoimport.so
%{_libdir}/kde4/calligra_filter_mpxj2plan.so
%{_libdir}/kde4/planconvert
%{service krossmoduleplan}
%{service planpart}
%{service plantjscheduler}
%{service planworkpart}
%defattr(0644,root,root,0755)
%{_kde_servicetypes}/plan_schedulerplugin.desktop
%{_kde_servicetypes}/plan_viewplugin.desktop
%{_datadir}/appdata/plan.appdata.xml
%{_datadir}/config.kcfg/plansettings.kcfg
%{_datadir}/config.kcfg/planworksettings.kcfg
%{_datadir}/config/planrc
%{_datadir}/config/planworkrc
%{_datadir}/mime/packages/calligra_planner_mpp.xml
%{_kde_applicationsdir}/plan.desktop
%{_kde_applicationsdir}/planwork.desktop
%{_kde_appsdir}/plan
%{_kde_appsdir}/planwork
%{_kde_iconsdir}/hicolor/*/*/*kde.kplato*
%{_kde_iconsdir}/hicolor/*/*/application-x-vnd.kde.plan*
%{_kde_iconsdir}/hicolor/*/*/calligraplan*
%{_kde_services}/calligra/calligra_filter_mpp2plan.desktop
%{_kde_services}/calligra/calligra_filter_mpx2plan.desktop
%{_kde_services}/calligra/calligra_filter_planner2plan.desktop
%{_kde_services}/calligra/plan_icalendar_export.desktop
%{_kde_services}/calligra/plan_kplato_import.desktop
%{_kde_services}/calligra/planrcpsscheduler.desktop
%{_kde_services}/calligra/planscripting.desktop

#--------------------------------------------------------------------

%package sheets
Summary:	SpreadSheet for calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
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
%{_datadir}/kde4/services/sheets_*_thumbnail.desktop
%{_kde_services}/calligra/sheetsscripting.desktop
%{_kde_servicetypes}/sheets_viewplugin.desktop
%{_libdir}/kde4/calligrasheetspart.so
%{_libdir}/kde4/kplatorcpsscheduler.so
%{_libdir}/kde4/kspread*.so
%{_libdir}/libkdeinit4_calligrasheets.so
%{service calligra_filter_applixspread2kspread}
%{service calligra_filter_csv2sheets}
%{service calligra_filter_dbase2kspread}
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
%{service calligra_shape_spreadsheet-deferred}
%{service calligra_shape_spreadsheet}
%{service krossmodulesheets}
%{service sheetssolver}
%defattr(0644,root,root,0755)
%doc %{_docdir}/HTML/en/sheets
%{_datadir}/appdata/sheets.appdata.xml
%{_datadir}/applications/kde4/sheets.desktop
%{_datadir}/config.kcfg/sheets.kcfg
%{_datadir}/config/sheetsrc
%{_datadir}/templates/.source/SpreadSheet.ods
%{_datadir}/templates/SpreadSheet.desktop
%{_kde_appsdir}/sheets
%{_kde_iconsdir}/hicolor/*/*/calligrasheets*
%{_kde_services}/ServiceMenus/calligra/sheets_print.desktop
%{_kde_services}/calligra/kspread*.desktop
%{_kde_services}/calligra/sheetspart.desktop
%{_kde_servicetypes}/sheets_plugin.desktop

#--------------------------------------------------------------------

%package stage
Summary:	Presentation for calligra-suite
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	xdg-utils
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
%{_datadir}/kde4/services/stage_*_thumbnail.desktop
%{_datadir}/mime/packages/x-iwork-keynote-sffkey.xml
%{_libdir}/kde4/calligrastagepart.so
%{_libdir}/libkdeinit4_calligrastage.so
%{service calligra_filter_key2odp}
%{service calligra_filter_kpr2odp}
%{service calligra_filter_ppt2odp}
%{service calligra_filter_pptx2odp}
%{service calligrastageeventactions}
%{service calligrastagetoolanimation}
%{service kpr_pageeffect_barwipe}
%{service kpr_pageeffect_clockwipe}
%{service kpr_pageeffect_edgewipe}
%{service kpr_pageeffect_fade}
%{service kpr_pageeffect_iriswipe}
%{service kpr_pageeffect_matrixwipe}
%{service kpr_pageeffect_slidewipe}
%{service kpr_pageeffect_spacerotation}
%{service kpr_pageeffect_swapeffect}
%{service kpr_shapeanimation_example}
%{service kprvariables}
%defattr(0644,root,root,0755)
%doc %{_docdir}/HTML/en/stage
%{_datadir}/appdata/stage.appdata.xml
%{_datadir}/config/stagerc
%{_datadir}/kde4/services/calligra/stagepart.desktop
%{_datadir}/templates/.source/Presentation.odp
%{_datadir}/templates/Presentation.desktop
%{_kde_applicationsdir}/stage.desktop
%{_kde_appsdir}/stage
%{_kde_iconsdir}/hicolor/*/apps/calligrastage.*
%{_kde_services}/ServiceMenus/calligra/stage_print.desktop
%{_kde_servicetypes}/kpr_pageeffect.desktop
%{_kde_servicetypes}/kpr_shapeanimation.desktop
%{_kde_servicetypes}/presentationeventaction.desktop

#--------------------------------------------------------------------

%package kchart
Summary:	Chart and diagram drawing
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
%rename		kchart

%description kchart
Kchart is a chart and diagram drawing program.

%files kchart
%{service calligra_shape_chart}

#--------------------------------------------------------------------

%package krita
%define __noautoreq 'devel.*|calligra-devel'
Summary:	Sketching and painting program
Group:		Graphics
Requires:	%{name}-core = %{EVRD}
Requires:	libkdcraw-common
%rename		krita

%description krita
Krita offers an end–to–end solution for creating digital painting files
from scratch by masters. It supports concept art, creation of comics
and textures for rendering.

%files krita
%defattr(0755,root,root,0755)
%{_bindir}/gmicparser
%{_bindir}/krita
%{_datadir}/appdata/krita.appdata.xml
%{_datadir}/applications/kde4/krita_heightmap.desktop
%{_datadir}/applications/kde4/krita_tga.desktop
%{_datadir}/apps/color-schemes/KritaNeutral.colors
%{_datadir}/apps/kritaanimation
%{_datadir}/apps/kritasketch
%{_datadir}/color/icc/krita/CMakeLists.txt
%{_datadir}/kde4/services/krita_*_thumbnail.desktop
%{_datadir}/kde4/services/qimageioplugins/kra.desktop
%{_datadir}/kde4/services/qimageioplugins/ora.desktop
%{_libdir}/calligra/imports/org/krita
%{_libdir}/kde4/*krita*
%{_libdir}/kde4/plugins/imageformats/kimg_kra.so
%{_libdir}/kde4/plugins/imageformats/kimg_ora.so
%defattr(0644,root,root,0755)
%dir %{_datadir}/color/icc/krita
%{_datadir}/color/icc/krita/*.icc
%{_datadir}/color/icc/krita/*.icm
%{_datadir}/color/icc/krita/README
%{_datadir}/mime/packages/krita.xml
%{_datadir}/mime/packages/krita_ora.xml
%{_kde_applicationsdir}/krita.desktop
%{_kde_applicationsdir}/krita_bmp.desktop
%{_kde_applicationsdir}/krita_exr.desktop
%{_kde_applicationsdir}/krita_jp2.desktop
%{_kde_applicationsdir}/krita_jpeg.desktop
%{_kde_applicationsdir}/krita_odg.desktop
%{_kde_applicationsdir}/krita_ora.desktop
%{_kde_applicationsdir}/krita_pdf.desktop
%{_kde_applicationsdir}/krita_png.desktop
%{_kde_applicationsdir}/krita_ppm.desktop
%{_kde_applicationsdir}/krita_psd.desktop
%optional %{_kde_applicationsdir}/krita_raw.desktop
%{_kde_applicationsdir}/krita_tiff.desktop
%{_kde_applicationsdir}/krita_xcf.desktop
%{_kde_appsdir}/color-schemes/KritaBlender.colors
%{_kde_appsdir}/color-schemes/KritaBright.colors
%{_kde_appsdir}/color-schemes/KritaDark.colors
%{_kde_appsdir}/krita
%{_kde_appsdir}/kritaplugins
%{_kde_configdir}/krita*.knsrc
%{_kde_configdir}/kritarc
%{_kde_iconsdir}/hicolor/*/apps/calligrakrita.*
%{_kde_services}/ServiceMenus/calligra/krita_print.desktop
%{_kde_services}/calligra/*krita*.desktop
%{_kde_servicetypes}/*krita*.desktop

#--------------------------------------------------------------------

%package gemini
Summary:	Unified interface for Krita and Krita Sketch
Group:		Graphics

%description gemini
Unified interface for Krita and Krita Sketch.

%files gemini
%{_bindir}/calligragemini
%{_bindir}/calligrageminithumbnailhelper
%{_datadir}/applications/kde4/calligragemini.desktop
%{_datadir}/apps/calligragemini
%{_datadir}/apps/kritagemini
%{_iconsdir}/hicolor/*/apps/calligragemini.png
%{_iconsdir}/hicolor/*/apps/kritagemini.png
%{_iconsdir}/hicolor/*/apps/kritasketch.png
%{_libdir}/calligra/imports/Calligra/Gemini

#--------------------------------------------------------------------

%package karbon
Summary:	Scalable drawing for calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
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
%{_kde_servicetypes}/karbon_dock.desktop
%{_kde_servicetypes}/karbon_viewplugin.desktop
%{_libdir}/kde4/karbon_flattenpathplugin.so
%{_libdir}/kde4/karbon_refinepathplugin.so
%{_libdir}/kde4/karbon_roundcornersplugin.so
%{_libdir}/kde4/karbon_whirlpinchplugin.so
%{_libdir}/kde4/karbonfiltereffects.so
%{_libdir}/kde4/karbonpart.so
%{_libdir}/kde4/karbontools.so
%{_libdir}/libkdeinit4_karbon.so
%{optional_service calligra_filter_eps2svgai}
%{service calligra_filter_karbon1x2karbon}
%{service calligra_filter_karbon2image}
%{service calligra_filter_karbon2svg}
%{service calligra_filter_karbon2wmf}
%{service calligra_filter_pdf2svg}
%{service calligra_filter_svg2karbon}
%{service calligra_filter_wmf2svg}
%{service calligra_filter_wpg2odg}
%{service calligra_filter_wpg2svg}
%{service calligra_filter_xfig2odg}
%defattr(0644,root,root,0755)
%{_datadir}/appdata/karbon.appdata.xml
%{_datadir}/kde4/services/karbon_*_thumbnail.desktop
%{_datadir}/templates/.source/Illustration.odg
%{_datadir}/templates/Illustration.desktop
%{_kde_applicationsdir}/karbon.desktop
%{_kde_appsdir}/karbon
%{_kde_configdir}/karbonrc
%{_kde_iconsdir}/*/*/apps/calligrakarbon.*
%{_kde_services}/ServiceMenus/calligra/karbon_print.desktop
%{_kde_services}/calligra/karbon*.desktop
%{_kde_servicetypes}/filtereffect.desktop

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
%{_libdir}/libkdeinit4_calligraflow.so
%{service calligra_filter_vsdx2odg}
%{service flowdockersplugin}
%{service flowpart}
%defattr(0644,root,root,0755)
%{_datadir}/appdata/flow.appdata.xml
%{_datadir}/applications/kde4/flow.desktop
%{_datadir}/config/flow_stencils.knsrc
%{_datadir}/config/flowrc
%{_datadir}/kde4/services/flow_*_thumbnail.desktop
%{_kde_appsdir}/flow
%{_kde_iconsdir}/hicolor/*/*/calligraflow*
%{_kde_services}/ServiceMenus/calligra/flow_print.desktop
%{_kde_servicetypes}/flow_dock.desktop

#--------------------------------------------------------------------

%package kexi
Summary:	An integrated environment for managing data
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
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
%{_libdir}/kde4/kexidb_mysqldriver.so
%{_libdir}/kde4/kexidb_pqxxsqldriver.so
%{_libdir}/kde4/kexidb_sqlite3_icu.so
%{_libdir}/kde4/kexidb_sqlite3driver.so
%{_libdir}/kde4/kexidb_sybasedriver.so
%{_libdir}/kde4/kexidb_xbasedriver.so
%{_libdir}/kde4/kexihandler_csv_importexport.so
%{_libdir}/kde4/kexihandler_form.so
%{_libdir}/kde4/kexihandler_migration.so
%{_libdir}/kde4/kexihandler_query.so
%{_libdir}/kde4/kexihandler_report.so
%{_libdir}/kde4/kexihandler_script.so
%{_libdir}/kde4/kexihandler_table.so
%{_libdir}/kde4/keximigrate_mdb.so
%{_libdir}/kde4/keximigrate_mysql.so
%{_libdir}/kde4/keximigrate_pqxx.so
%{_libdir}/kde4/keximigrate_spreadsheet.so
%{_libdir}/kde4/keximigrate_sybase.so
%{_libdir}/kde4/keximigrate_txt.so
%{_libdir}/kde4/keximigrate_xbase.so
%{_libdir}/kde4/kformdesigner_containers.so
%{_libdir}/kde4/kformdesigner_kexidbwidgets.so
%optional %{_libdir}/kde4/kformdesigner_mapbrowser.so
%{_libdir}/kde4/kformdesigner_stdwidgets.so
%{_libdir}/kde4/kformdesigner_webbrowser.so
%{_libdir}/kde4/krossmodulekexidb.so
%defattr(0644,root,root,0755)
%doc %{_docdir}/HTML/en/kexi
%{_kde_servicetypes}/calligradb_driver.desktop
%{_kde_servicetypes}/kexihandler.desktop
%{_kde_servicetypes}/keximigration_driver.desktop
%{_kde_servicetypes}/widgetfactory.desktop
%{_datadir}/appdata/kexi.appdata.xml
%{_datadir}/config/kexirc
%{_kde_applicationsdir}/kexi.desktop
%{_kde_appsdir}/kexi
%{_kde_iconsdir}/hicolor/*/*/calligrakexi*
%{_kde_services}/calligra/kexi*.desktop
%{_kde_services}/calligra/kformdesigner_*.desktop

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
%{_datadir}/applications/kde4/okularApplication_odp.desktop
%{_kde_services}/libokularGenerator_odp.desktop
%{_kde_services}/okularOdp.desktop

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
%{_datadir}/applications/kde4/okularApplication_odt.desktop
%{_datadir}/kde4/services/libokularGenerator_doc_calligra.desktop
%{_datadir}/kde4/services/libokularGenerator_docx_calligra.desktop
%{_datadir}/kde4/services/libokularGenerator_wpd_calligra.desktop
%{_datadir}/kde4/services/okularDoc_calligra.desktop
%{_datadir}/kde4/services/okularDocx_calligra.desktop
%{_datadir}/kde4/services/okularWpd_calligra.desktop
%{_kde_applicationsdir}/okularApplication_doc_calligra.desktop
%{_kde_applicationsdir}/okularApplication_docx_calligra.desktop
%{_kde_applicationsdir}/okularApplication_wpd_calligra.desktop
%{_kde_services}/libokularGenerator_odt.desktop
%{_kde_services}/okularOdt.desktop

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
%{_kde_iconsdir}/hicolor/*/*/stateshape*
%{_kde_iconsdir}/hicolor/*/*/statetool*

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
%{_kde_servicetypes}/braindump_extensions.desktop
%{_bindir}/braindump
%{_datadir}/appdata/braindump.appdata.xml
%{_datadir}/kde4/services/calligra/braindump_*.desktop
%{_kde_applicationsdir}/braindump.desktop
%{_kde_appsdir}/braindump
%{_kde_iconsdir}/*/*/*/braindump.*
%{_libdir}/kde4/braindump_shape_*.so

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
%{_kde_iconsdir}/hicolor/178x200/apps/calligramobile.png
%{_kde_iconsdir}/hicolor/48x48/hildon/Document.png
%{_kde_iconsdir}/hicolor/48x48/hildon/Presenter.png
%{_kde_iconsdir}/hicolor/48x48/hildon/SpreadSheet.png
%{_kde_iconsdir}/hicolor/64x64/apps/calligramobile.png
%endif

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

%package devel
Group:		Development/KDE and Qt
Summary:	Header files for developing calligra applications
Requires:	%{name}-core = %{EVRD}
%{expand:%(for lib in %{calligralibs}; do cat <<EOF
Requires:	%{lib$lib} = %{EVRD}
EOF
done)}
Requires:	%{libkowv2} = %{EVRD}
Requires:	%{libplanworkfactory} = %{EVRD}
Requires:	%{libRtfReader} = %{EVRD}
Requires:	%{libkoodf2} = %{EVRD}

%description devel
Header files needed for developing calligra applications.

%files devel
%{_kde_appsdir}/cmake/*/*
%{_kde_includedir}/*
%{expand:%(for lib in %{calligralibs}; do cat <<EOF
%{_libdir}/lib${lib}.so
EOF
done)}
%{_libdir}/libkowv2.so
%{_libdir}/libplanworkfactory.so
%{_libdir}/libRtfReader.so
%{_libdir}/libkoodf2.so

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

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

