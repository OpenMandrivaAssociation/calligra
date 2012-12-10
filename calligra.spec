%define compile_apidox 0
%define _mobile 0
%define prerel %nil

#koffice has epoch 15. We need upper epoch
Epoch: 16
Name: calligra
URL:     http://www.calligra-suite.org
Summary: Set of office applications for KDE
Version: 2.5.3
%if "%prerel" != ""
Release: -c %prerel 1
%else
Release: 1
%endif
Source0: http://master.kde.org/stable/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1: %{name}.rpmlintrc
Patch1: calligra-2.4.0-find-openjpeg.patch
Group: Office
License: GPLv2+ and LGPLv2+ and GFDL
BuildRequires: kdepimlibs4-devel
#Source100: %name.rpmlintrc

#For version upper or equal 2012
BuildRequires: pkgconfig(libkexiv2)
#BuildRequires:	kdegraphics4-devel
BuildRequires: libkdcraw-devel
#For version upper or equal 2012
BuildRequires: okular-devel
BuildRequires: lcms2-devel
BuildRequires: qca2-devel
BuildRequires: xbase-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: pkgconfig(QtShiva) >= 0.9.2
BuildRequires: libexif-devel
BuildRequires: libexiv-devel
BuildRequires: boost-devel
BuildRequires: pkgconfig(poppler-qt4)
BuildRequires: jbig-devel
BuildRequires: openjpeg-devel >= 1.5
BuildRequires: libxml2-devel >= 2.4.28-2mdk
BuildRequires: python-devel
BuildRequires: readline-devel
BuildRequires: libpqxx-devel
BuildRequires: postgresql-devel
BuildRequires: eigen2
BuildRequires: pstoedit
BuildRequires: mysql-devel
BuildRequires: qimageblitz-devel
BuildRequires: gsl-devel
BuildRequires: qca2-devel
BuildRequires: glpk-devel
BuildRequires: freeglut-devel
BuildRequires: glew-devel
BuildRequires: pkgconfig(GraphicsMagick)
BuildRequires: opengtl-devel >= 0.9.16
BuildRequires: mysql-devel
BuildRequires: wv2-devel >= 0.4.2
BuildRequires: getfem++
BuildRequires: ctemplate-devel
BuildRequires: freetds-devel
BuildRequires: sqlite-devel
BuildRequires: marble-devel
BuildRequires: fftw3-devel >= 3.2
BuildRequires: libvisio-devel
BuildRequires: libwps-devel
%if %compile_apidox
BuildRequires: graphviz
BuildRequires: doxygen
%endif
Suggests: %name-words
Suggests: sheets
Suggests: karbon
Suggests: stage
Suggests: krita
Suggests: plan
Suggests: kchart
Suggests: kformula
Suggests: kexi
Suggests: flow
Suggests: braindump
Obsoletes: f-office
Obsoletes: koshell
Obsoletes: kugar
Obsoletes: kivio
Obsoletes: koffice-kivio < 1.6.3-20
Obsoletes: koffice

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

%package core
Group: Office
Summary: Set of office applications for KDE
Obsoletes: koffice-core < 15:2.4
Obsoletes: %{_lib}kopainter5
Obsoletes: koffice2-core
Obsoletes: koffice-common
Obsoletes: koshell
Obsoletes: kugar
Obsoletes: kplatowork
Obsoletes: kivio
Requires: kdebase4-runtime

%description core
Common files for Calligra

%files core
%defattr(0755,root,root,0755)
%_kde_bindir/calligra
%_kde_bindir/calligraconverter
%_kde_bindir/cstester
%_kde_bindir/cstrunner
%_kde_bindir/visualimagecompare
%_kde_libdir/kde4/artistictextshape.so
%_kde_libdir/kde4/autocorrect.so
%_kde_libdir/kde4/changecase.so
%_kde_libdir/kde4/commentshape.so
%_kde_libdir/kde4/defaulttools.so
%_kde_libdir/kde4/kodocinfopropspage.so
%_kde_libdir/kde4/calligradockers.so
%_kde_libdir/kde4/calligrathumbnail.so
%_kde_libdir/kde4/calligragoogledocs.so
%_kde_libdir/kde4/kolcmsengine.so
%_kde_libdir/kde4/kopabackgroundtool.so
%_kde_libdir/kde4/koreport_barcodeplugin.so
%_kde_libdir/kde4/koreport_chartplugin.so
%_kde_libdir/kde4/koreport_mapsplugin.so
%_kde_libdir/kde4/koreport_webplugin.so
%_kde_libdir/kde4/musicshape.so
%_kde_libdir/kde4/spreadsheetshape-deferred.so
%_kde_libdir/kde4/pathshapes.so
%_kde_libdir/kde4/pictureshape.so
%_kde_libdir/kde4/pluginshape.so
%_kde_libdir/kde4/spellcheck.so
%_kde_libdir/kde4/textshape.so
%_kde_libdir/kde4/textvariables.so
%_kde_libdir/kde4/thesaurustool.so
%_kde_libdir/kde4/vectorshape.so
%_kde_libdir/kde4/videoshape.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/calligra.desktop
%_kde_appsdir/calligra
%_kde_appsdir/koproperty
%_kde_appsdir/musicshape
%_kde_appsdir/pigmentcms
%_kde_datadir/color/icc/pigment/*.icm
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
%_kde_iconsdir/*/*/actions/x-shape-chart.*
%_kde_iconsdir/*/*/actions/x-shape-connection.*
%_kde_iconsdir/*/*/actions/x-shape-formula.*
%_kde_iconsdir/*/*/actions/x-shape-image.*
%_kde_iconsdir/*/*/actions/x-shape-text.*
%_kde_services/artistictextshape.desktop
%_kde_services/autocorrect.desktop
%_kde_services/changecase.desktop
%_kde_services/commentshape.desktop
%_kde_services/defaulttools.desktop
%_kde_services/kodocinfopropspage.desktop
%_kde_services/calligradockers.desktop
%_kde_services/calligrathumbnail.desktop
%_kde_services/kolcmsengine.desktop
%_kde_services/kopabackgroundtool.desktop
%_kde_services/koreport_barcodeplugin.desktop
%_kde_services/koreport_chartplugin.desktop
%_kde_services/koreport_mapsplugin.desktop
%_kde_services/koreport_webplugin.desktop
%_kde_services/musicshape.desktop
#%_kde_services/paragraphtool.desktop
%_kde_services/pathshapes.desktop
%_kde_services/pictureshape.desktop
%_kde_services/pluginshape.desktop
%_kde_services/spellcheck.desktop
%_kde_services/textshape.desktop
%_kde_services/textvariables.desktop
%_kde_services/thesaurustool.desktop
%_kde_services/vectorshape.desktop
%_kde_services/videoshape.desktop
%_kde_servicetypes/calligra_application.desktop
%_kde_servicetypes/flake.desktop
%_kde_servicetypes/flakedevice.desktop
%_kde_servicetypes/flakeshape.desktop
%_kde_servicetypes/flaketool.desktop
%_kde_servicetypes/inlinetextobject.desktop
%_kde_servicetypes/kochart.desktop
%_kde_servicetypes/calligradocker.desktop
%_kde_servicetypes/calligrapart.desktop
%_kde_servicetypes/kofilter.desktop
%_kde_servicetypes/kofilterwrapper.desktop
%_kde_servicetypes/koplugin.desktop
%_kde_servicetypes/koreport_itemplugin.desktop
%_kde_servicetypes/pigment.desktop
%_kde_servicetypes/pigmentextension.desktop
%_kde_servicetypes/scripteventaction.desktop
%_kde_servicetypes/texteditingplugin.desktop
%_kde_servicetypes/textvariableplugin.desktop
%_kde_servicetypes/calligra_deferred_plugin.desktop
%_kde_datadir/mime/packages/msooxml-all.xml
%doc %_kde_docdir/HTML/en/calligra

#--------------------------------------------------------------------

%package      words
Summary:	    Word processor for calligra
Group:		    Graphical desktop/KDE
URL:            http://www.calligra-suite.org/words/
Requires:	    %name-core = %{EVRD}
Requires:	    wordnet
Provides:	    %name-apps
Obsoletes:      koffice-kword
Obsoletes:      koffice2-kword
Obsoletes:      kword


%description    words
Words is an intuitive word processor application with desktop publishing
features.
With it, you can create informative and attractive documents with ease.

%files words
%defattr(755,root,root)
%_kde_bindir/calligrawords
%_kde_libdir/kde4/applixwordimport.so
%_kde_libdir/kde4/asciiimport.so
%_kde_libdir/kde4/docximport.so
%_kde_libdir/kde4/htmlodf_export.so
#%_kde_libdir/kde4/krossmodulekword.so
%_kde_libdir/kde4/wordspart.so
%_kde_libdir/kde4/mswordodf_import.so
%_kde_libdir/kde4/rtfimport.so
%_kde_libdir/kde4/wpsimport.so
%_kde_libdir/libkdeinit4_calligrawords.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/words.desktop
#%_kde_appsdir/kword
%_kde_appsdir/words
%_kde_configdir/wordsrc
%_kde_iconsdir/hicolor/*/apps/words.*
%_kde_services/ServiceMenus/words_konqi.desktop
%_kde_services/html-odf_export.desktop
#%_kde_services/krossmodulekword.desktop
%_kde_services/words*.desktop
%_kde_datadir/templates/.source/TextDocument.odt
%_kde_datadir/templates/TextDocument.desktop

#--------------------------------------------------------------------

%package -n plan
Summary:	Project management application for Calligra
Group:		Graphical desktop/KDE
URL:            http://www.calligra-suite.org/plan/
Requires:	%name-core = %{EVRD}
Provides:       %name-apps
Provides:       kplato2
Obsoletes:      kplatowork
Obsoletes:      kplato
Obsoletes:      %{_lib}kplatoworkprivat5
Obsoletes:      koffice-kplato
Obsoletes:      koffice2-kplato
%rename		%{name}-plan


%description -n plan
Plan is a project management application.
It is intended for managing moderately large projects with multiple resources.


%files -n plan
%defattr(0755,root,root,0755)
%_kde_bindir/calligraplan
%_kde_bindir/calligraplanwork
%_kde_libdir/libkdeinit4_calligraplan.so
%_kde_libdir/libkdeinit4_calligraplanwork.so
%_kde_libdir/kde4/krossmoduleplan.so
%_kde_libdir/kde4/planpart.so
%_kde_libdir/kde4/planworkpart.so
%_kde_libdir/kde4/planicalexport.so
%_kde_libdir/kde4/plankplatoimport.so
%{_kde_libdir}/kde4/plantjscheduler.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/plan.desktop
%_kde_applicationsdir/planwork.desktop
%_kde_appsdir/plan
%_kde_appsdir/planwork
%_kde_datadir/config/planrc
%_kde_services/krossmoduleplan.desktop
%_kde_services/plan_icalendar_export.desktop
%_kde_services/planpart.desktop
%_kde_services/planworkpart.desktop
%_kde_services/plan_kplato_import.desktop
%_kde_services/planrcpsscheduler.desktop
%_kde_services/plantjscheduler.desktop
%_kde_servicetypes/plan_schedulerplugin.desktop
%_kde_iconsdir/hicolor/*/*/calligraplan*
%_kde_iconsdir/hicolor/*/*/application-x-vnd.kde.plan*
%_kde_datadir/config.kcfg/plansettings.kcfg
%_kde_datadir/config.kcfg/planworksettings.kcfg
%_kde_datadir/config/planworkrc

#--------------------------------------------------------------------

%package -n sheets
Summary:	SpreadSheet for calligra
Group:		Graphical desktop/KDE
URL:            http://www.calligra-suite.org/sheets/
Requires:	%name-core = %{EVRD}
Provides:       %name-apps
Obsoletes:      koffice-kspread
Obsoletes:      koffice2-kspread
Obsoletes:      kspread
# Sheets used to be called tables in early betas
%rename		tables
%rename		%{name}-sheets
Conflicts:      kword < 11:2.1.91-2


%description -n sheets
Sheets is a fully-featured calculation and spreadsheet tool.
Use it to quickly create and calculate various business-related spreadsheets,
such as income and expenditure, employee working hours, etc.

%files -n sheets
%defattr(0755,root,root,0755)
%_kde_bindir/calligrasheets
%_kde_libdir/kde4/applixspreadimport.so
%_kde_libdir/kde4/calligrasheetspart.so
%_kde_libdir/kde4/csvexport.so
%_kde_libdir/kde4/csvimport.so
%_kde_libdir/kde4/dbaseimport.so
%_kde_libdir/kde4/excelimporttodoc.so
%_kde_libdir/kde4/gnumericexport.so
%_kde_libdir/kde4/gnumericimport.so
%_kde_libdir/kde4/kplatorcpsscheduler.so
%_kde_libdir/kde4/kspread*.so
%_kde_libdir/kde4/krossmodulekspread.so
%_kde_libdir/kde4/opencalcexport.so
%_kde_libdir/kde4/opencalcimport.so
%_kde_libdir/kde4/qproimport.so
%_kde_libdir/kde4/spreadsheetshape.so
%_kde_libdir/kde4/xlsximport.so
%_kde_libdir/libkdeinit4_calligrasheets.so
%defattr(0644,root,root,0755)
%_kde_datadir/applications/kde4/sheets.desktop
%_kde_datadir/config.kcfg/sheets.kcfg
%_kde_services/sheetspart.desktop
%_kde_appsdir/tables
%_kde_appsdir/sheets
%_kde_datadir/config/sheetsrc
%_kde_datadir/templates/SpreadSheet.desktop
%_kde_services/krossmodulekspread.desktop
%_kde_services/kspread*.desktop
%_kde_datadir/templates/.source/SpreadSheet.ods
%_kde_iconsdir/hicolor/*/apps/sheets.png
%_kde_services/ServiceMenus/kspread_konqi.desktop
%_kde_services/spreadsheetshape.desktop
%_kde_services/spreadsheetshape-deferred.desktop
%_kde_servicetypes/sheets_plugin.desktop
%doc %_docdir/HTML/en/sheets
#--------------------------------------------------------------------

%package -n stage
Summary:	Presentation for calligra-suite
Group:		Graphical desktop/KDE
URL:            http://www.calligra-suite.org/stage/
Requires:	%name-core = %{EVRD}
Requires:	xdg-utils
Provides:       %name-apps
Obsoletes:      koffice-kpresenter
Obsoletes:      koffice2-kpresenter
Obsoletes:      kpresenter
%rename		%{name}-stage


%description -n stage
Stage is an easy to use yet still flexible presentation application. You can
easily create presentations containing a rich variety of elements,
from graphics to text, from charts to images.
Stage is extensible through a plugin system, so it is easy to add new effects,
new content elements or even new ways of managing your presentation. Because of
the integration with Calligra, all the power and flexibility of the Calligra
content elements are available to Stage.

%files -n stage
%defattr(0755,root,root,0755)
%_kde_bindir/calligrastage
%_kde_libdir/kde4/calligrastagepart.so
%_kde_libdir/kde4/kpr_pageeffect_barwipe.so
%_kde_libdir/kde4/kpr_pageeffect_clockwipe.so
%_kde_libdir/kde4/kpr_pageeffect_edgewipe.so
%_kde_libdir/kde4/kpr_pageeffect_iriswipe.so
%_kde_libdir/kde4/kpr_pageeffect_matrixwipe.so
%_kde_libdir/kde4/kpr_pageeffect_slidewipe.so
%_kde_libdir/kde4/kpr_pageeffect_fade.so
%_kde_libdir/kde4/kpr_pageeffect_spacerotation.so
%_kde_libdir/kde4/kpr_pageeffect_swapeffect.so
%_kde_libdir/kde4/kpr_shapeanimation_example.so
%_kde_libdir/kde4/calligrastageeventactions.so 
%_kde_libdir/kde4/calligrastagetoolanimation.so
%_kde_libdir/kde4/kprvariables.so
%_kde_libdir/kde4/powerpointimport.so
%_kde_libdir/kde4/Filterkpr2odf.so
%_kde_libdir/kde4/pptximport.so
%_kde_libdir/libkdeinit4_calligrastage.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/stage.desktop
%_kde_services/ServiceMenus/kpresenter_konqi.desktop
%_kde_appsdir/stage
%_kde_datadir/templates/Presentation.desktop
%_kde_datadir/templates/.source/Presentation.odp
%_kde_datadir/config/stagerc
%_kde_iconsdir/hicolor/*/apps/stage.png
%_kde_services/calligrastageeventactions.desktop
%_kde_servicetypes/presentationeventaction.desktop
%_kde_services/kpr_pageeffect_barwipe.desktop
%_kde_services/kpr_pageeffect_clockwipe.desktop
%_kde_services/kpr_pageeffect_edgewipe.desktop
%_kde_services/kpr_pageeffect_iriswipe.desktop
%_kde_services/kpr_pageeffect_matrixwipe.desktop
%_kde_services/kpr_pageeffect_slidewipe.desktop
%_kde_services/kpr_shapeanimation_example.desktop
%_kde_services/kpr_pageeffect_fade.desktop
%_kde_services/kpr_pageeffect_spacerotation.desktop
%_kde_services/kpr_pageeffect_swapeffect.desktop
%_kde_services/calligrastagetoolanimation.desktop
%_kde_services/kpresenter_powerpoint_import.desktop
%_kde_services/kpresenter_pptx_import.desktop
%_kde_services/kprvariables.desktop
%_kde_services/Filterkpr2odf.desktop
%_kde_servicetypes/kpr_pageeffect.desktop
%_kde_servicetypes/kpr_shapeanimation.desktop
%_kde_datadir/kde4/services/stagepart.desktop
%doc %_docdir/HTML/en/stage

#--------------------------------------------------------------------

%package -n kchart
Summary:        Chart and diagram drawing
Group:          Graphical desktop/KDE
Requires:       %name-core = %{EVRD}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kchart2
Obsoletes:      %name-kchart
Provides:       %name-kchart = %{EVRD}
Obsoletes:      koffice2-kchart
Provides:       koffice2-kchart = %{EVRD}
%rename		%{name}-kchart


%description -n kchart
Kchart is a chart and diagram drawing program.

%files -n kchart
%defattr(0755,root,root,0755)
%_kde_libdir/kde4/chartshape.so
%defattr(0644,root,root,0755)
%_kde_services/chartshape.desktop
%_kde_services/kchartpart.desktop

#--------------------------------------------------------------------

%package -n krita
Summary:        Sketching and painting program
Group:          Graphical desktop/KDE
URL:            http://www.calligra-suite.org/krita/
Requires:       %name-core = %{EVRD}
Requires:       libkdcraw-common
Provides:       %name-apps
Obsoletes:      koffice-krita
Obsoletes:      koffice2-krita
Obsoletes:      %{_lib}kritafilterslistdynamicprogram5
Obsoletes:      %{_lib}krita_gray_u165
Obsoletes:      %{_lib}kritargbf32hdr5
Obsoletes:	%{_lib}krossmodulekrita8
%rename		%{name}-krita

%description -n krita
Krita offers an end–to–end solution for creating digital painting files
from scratch by masters. It supports concept art, creation of comics
and textures for rendering.

%files -n krita
%defattr(0755,root,root,0755)
%_kde_bindir/krita
%_kde_libdir/kde4/*krita*
%_kde_libdir/libkdeinit4_krita.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/krita.desktop
%_kde_applicationsdir/krita_jpeg.desktop
%_kde_applicationsdir/krita_png.desktop
%_kde_applicationsdir/krita_bmp.desktop
%_kde_applicationsdir/krita_odg.desktop
%_kde_applicationsdir/krita_ora.desktop
%_kde_applicationsdir/krita_pdf.desktop
%_kde_applicationsdir/krita_tiff.desktop
%_kde_applicationsdir/krita_raw.desktop
%_kde_applicationsdir/krita_exr.desktop
%_kde_applicationsdir/krita_jp2.desktop
%_kde_applicationsdir/krita_ppm.desktop
%_kde_applicationsdir/krita_xcf.desktop
%_kde_applicationsdir/krita_psd.desktop
%_kde_services/ServiceMenus/krita_konqi.desktop
%_kde_services/*krita*.desktop
%_kde_servicetypes/*krita*.desktop
%_kde_iconsdir/hicolor/*/apps/krita.png
%_kde_appsdir/krita
%_kde_appsdir/kritaplugins
%_kde_configdir/kritarc
%_kde_configdir/krita*.knsrc
%dir %_kde_datadir/color/icc/krita
%_kde_datadir/color/icc/krita/README
%_kde_datadir/color/icc/krita/*.icm
%_kde_appsdir/color-schemes/Krita50.colors
%_kde_appsdir/color-schemes/KritaBlender.colors
%_kde_appsdir/color-schemes/KritaBright.colors
%_kde_appsdir/color-schemes/KritaBrighter.colors
%_kde_appsdir/color-schemes/KritaDark.colors
%_kde_appsdir/color-schemes/KritaDarker.colors
%_kde_datadir/mime/packages/krita_ora.xml

#--------------------------------------------------------------------

%package -n karbon
Summary:	Scalable drawing for calligra
Group:		Graphical desktop/KDE
URL:            http://www.calligra-suite.org/karbon/
Requires:	%name-core = %{EVRD}
Provides:       %name-apps
Obsoletes:      koffice-karbon
Obsoletes:      koffice2-karbon
Conflicts:      oxygen-icon-theme < 1:4.4.2-2
%rename		%{name}-karbon

%description -n karbon
Karbon is a vector drawing application with an user interface that is easy to
use, highly customizable and extensible.
That makes Karbon a great application for users starting to explore the world
of vector graphics as well as for artists wanting to create breathtaking vector
art.

%files -n karbon
%defattr(0755,root,root,0755)
%_kde_bindir/karbon
%_kde_libdir/kde4/karbonfiltereffects.so
%_kde_libdir/kde4/karbon_flattenpathplugin.so
%_kde_libdir/kde4/karbon_whirlpinchplugin.so
%_kde_libdir/kde4/karbonimageexport.so
%_kde_libdir/kde4/karbontools.so
%_kde_libdir/kde4/karbonpart.so
%_kde_libdir/kde4/karbonsvgexport.so
%_kde_libdir/kde4/karbonepsimport.so
%_kde_libdir/kde4/karbonsvgimport.so
%_kde_libdir/kde4/karbonxfigimport.so
%_kde_libdir/kde4/wmfexport.so
%_kde_libdir/kde4/wmfimport.so
%_kde_libdir/kde4/karbon1ximport.so
%_kde_libdir/kde4/karbonpdfimport.so
%_kde_libdir/kde4/wpgimport.so
%_kde_libdir/kde4/karbon_refinepathplugin.so
%_kde_libdir/kde4/karbon_roundcornersplugin.so
%_kde_libdir/libkdeinit4_karbon.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/karbon.desktop
%_kde_iconsdir/*/*/apps/karbon.*
%_kde_configdir/karbonrc
%_kde_appsdir/karbon
%_kde_datadir/templates/Illustration.desktop
%_kde_datadir/templates/.source/Illustration.odg
%_kde_services/ServiceMenus/karbon_konqi.desktop
%_kde_services/karbon*.desktop
%_kde_servicetypes/filtereffect.desktop
%_kde_servicetypes/karbon_module.desktop

#--------------------------------------------------------------------

%package -n kformula
Summary:        Formula Editor for calligra
Group:          Graphical desktop/KDE
URL:            http://www.koffice.org/
Requires:       %name-core = %{EVRD}
%rename		%{name}-kformula


%description -n kformula
Kformula is a formula editor for kde project.

%files -n kformula
%defattr(0755,root,root,0755)
%_kde_libdir/kde4/formulashape.so
%defattr(0644,root,root,0755)
%_kde_datadir/apps/formulashape
%_kde_services/formulashape.desktop
%{_kde_services}/kformulapart.desktop

#--------------------------------------------------------------------

%package -n flow
Summary:        Diagramming and flowcharting apps for calligra
Group:          Graphical desktop/KDE
URL:            http://www.calligra-suite.org/flow/
Requires:       %name-core = %{EVRD}
%rename         %{name}-flow

%description -n flow
Use Flow to make network diagrams, organization charts, flowcharts and much
more. Flow also comes with numerous stencils that can be used to make anything
you want. There are options for Networking, Renewable Energy, Chemistry,
Building sites, and many other options to help you make your diagrams.

%files -n flow
%defattr(0755,root,root,0755)
%_kde_bindir/calligraflow
%_kde_libdir/kde4/flowdockersplugin.so
%_kde_libdir/kde4/flowpart.so
%_kde_libdir/kde4/vsdximport.so
%_kde_libdir/libkdeinit4_calligraflow.so
%defattr(0644,root,root,0755)
%_kde_datadir/applications/kde4/flow.desktop
%_kde_datadir/config/flowrc
%_kde_datadir/config/flow_stencils.knsrc
%_kde_appsdir/flow
%_kde_services/flowdockersplugin.desktop
%_kde_services/flowpart.desktop
%_kde_services/flow_vsdx_import.desktop
%_kde_servicetypes/flow_dock.desktop
%_kde_services/ServiceMenus/flow_konqi.desktop
#--------------------------------------------------------------------

%package -n kexi
Summary:    An integrated environment for managing data
Group:      Graphical desktop/KDE
URL:        http://www.calligra-suite.org/kexi/
Requires:   %name-core = %{EVRD}
Provides:   %name-apps
Obsoletes:  keximdb
%rename     %{name}-kexi


%description -n kexi
Kexi is an integrated data management application.
It can be used for creating database schemas, inserting data, performing
queries, and processing data. Forms can be created to provide a custom
interface to your data. All database objects – tables, queries and forms –
are stored in the database, making it easy to share data and design.

%files -n kexi
%defattr(0755,root,root,0755)
%{_kde_bindir}/kexi
%{_kde_bindir}/kexi_sqlite3_dump
%{_kde_libdir}/kde4/kformdesigner_containers.so
%{_kde_libdir}/kde4/kformdesigner_mapbrowser.so
%{_kde_libdir}/kde4/kformdesigner_kexidbwidgets.so
%{_kde_libdir}/kde4/kformdesigner_stdwidgets.so
%{_kde_libdir}/kde4/kformdesigner_webbrowser.so
%{_kde_libdir}/kde4/kexidb_mysqldriver.so
%{_kde_libdir}/kde4/kexidb_sqlite3driver.so
%{_kde_libdir}/kde4/kexidb_sqlite3_icu.so
%{_kde_libdir}/kde4/kexidb_sybasedriver.so
%{_kde_libdir}/kde4/kexidb_xbasedriver.so
%{_kde_libdir}/kde4/kexihandler_csv_importexport.so
%{_kde_libdir}/kde4/kexihandler_form.so
%{_kde_libdir}/kde4/kexihandler_migration.so
%{_kde_libdir}/kde4/kexihandler_query.so
%{_kde_libdir}/kde4/kexihandler_script.so
%{_kde_libdir}/kde4/kexihandler_table.so
#%{_kde_libdir}/kde4/keximigrate_kspread.so
%{_kde_libdir}/kde4/keximigrate_mdb.so
%{_kde_libdir}/kde4/keximigrate_mysql.so
%{_kde_libdir}/kde4/keximigrate_sybase.so
%{_kde_libdir}/kde4/keximigrate_txt.so
%{_kde_libdir}/kde4/keximigrate_spreadsheet.so
%{_kde_libdir}/kde4/keximigrate_xbase.so
%{_kde_libdir}/kde4/kexirelationdesignshape.so
%{_kde_libdir}/kde4/krossmodulekexidb.so
%{_kde_libdir}/kde4/kexihandler_report.so
%defattr(0644,root,root,0755)
%{_kde_appsdir}/kexi
%{_kde_datadir}/config/kexirc
%{_kde_services}/kexi
%{_kde_services}/kexidb_mysqldriver.desktop
%{_kde_services}/kexidb_sqlite3driver.desktop
%{_kde_services}/kexidb_sybasedriver.desktop
%{_kde_services}/kexidb_xbasedriver.desktop
#%{_kde_services}/keximigrate_kspread.desktop
%{_kde_services}/keximigrate_mdb.desktop
%{_kde_services}/keximigrate_mysql.desktop
%{_kde_services}/keximigrate_sybase.desktop
%{_kde_services}/keximigrate_txt.desktop
%{_kde_services}/keximigrate_spreadsheet.desktop
%{_kde_services}/keximigrate_xbase.desktop
%{_kde_services}/kexirelationdesignshape.desktop
%{_kde_services}/kformdesigner
%{_kde_servicetypes}/widgetfactory.desktop
%{_kde_servicetypes}/kexidb_driver.desktop
%{_kde_servicetypes}/kexihandler.desktop
%{_kde_servicetypes}/keximigration_driver.desktop
%{_kde_applicationsdir}/kexi.desktop
%doc %_docdir/HTML/en/kexi

#--------------------------------------------------------------------

%package -n okular-odp
Summary:	ODP file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%name-core = %{EVRD}
Requires:	okular
%rename		%{name}-okular-odp

%description -n okular-odp
ODP file renderer for Okular.

%files -n okular-odp
%defattr(0755,root,root,0755)
%_kde_libdir/kde4/okularGenerator_odp.so
%defattr(0644,root,root,0755)
%_kde_applicationsdir/okularApplication_odp.desktop
%_kde_services/libokularGenerator_odp.desktop
%_kde_services/okularOdp.desktop

#--------------------------------------------------------------------

%package -n stateshape
Summary:	State Shape
Group:		Graphical desktop/KDE
Requires:	%name-core = %{EVRD}
%rename		%{name}-stateshape

%description -n stateshape
Calligra State Shape.

%files -n stateshape
%defattr(0755,root,root,0755)
%_kde_libdir/kde4/stateshape.so
%defattr(0644,root,root,0755)
%_kde_appsdir/stateshape
%_kde_iconsdir/hicolor/*/*/stateshape*
%_kde_iconsdir/hicolor/*/*/statetool*
%_kde_services/stateshape.desktop

#--------------------------------------------------------------------

%package -n webshape
Summary:	Calligra Web Shape
Group:		Graphical desktop/KDE
Requires:	%name-core = %{EVRD}
%rename		%{name}-webshape

%description -n webshape
Calligra Web Shape.

%files -n webshape
%defattr(0755,root,root,0755)
%_kde_libdir/kde4/webshape.so
%defattr(0644,root,root,0755)
%_kde_services/webshape.desktop

#--------------------------------------------------------------------

%define libbraindumpcore_major 10
%define libbraindumpcore %mklibname braindumpcore %libbraindumpcore_major

%package -n %libbraindumpcore
Summary: Calligra Braindump core library
Group: System/Libraries

%description -n %libbraindumpcore
Calligra Braindump core library.

%files -n %libbraindumpcore
%defattr(-,root,root)
%_kde_libdir/libbraindumpcore.so.%{libbraindumpcore_major}*

#--------------------------------------------------------------------

%package -n braindump
Summary:	Calligra mind mapping tool
Group:		Graphical desktop/KDE
Requires:	%name-core = %{EVRD}
Requires:	%libbraindumpcore = %{EVRD}
%rename		%{name}-braindump

%description -n braindump
Braindump is a tool to dump and organize the content of your brain (ideas,
drawings, images, texts...) to your computer. It works by allowing to create
and edit whiteboards, which are infinite canvas on which you can add texts,
images, charts, drawings. You can also organize your ideas into diagrams
and flowcharts.

%files -n braindump
%defattr(0755,root,root,0755)
%_kde_bindir/braindump
%defattr(0644,root,root,0755)
%_kde_applicationsdir/braindump.desktop
%_kde_appsdir/braindump
%_kde_servicetypes/braindump_extensions.desktop
%_kde_iconsdir/*/*/*/braindump.*

#--------------------------------------------------------------------

%package active
Summary:        A document viewer for touch based tablets
Group:          Graphical desktop/KDE
Requires:       %{name}-words = %{EVRD}
Requires:	sheets = %{EVRD}
Requires:	stage = %{EVRD}

%description active
Calligra's QML UI.

%files active
%defattr(0755,root,root,0755)
%{_kde_bindir}/calligraactive
%defattr(0644,root,root,0755)
%{_kde_datadir}/applications/calligraactive.desktop
%{_kde_datadir}/calligraactive

#--------------------------------------------------------------------

%define libtextlayout_major 10
%define libtextlayout %mklibname textlayout %libtextlayout_major

%package -n %libtextlayout
Summary: Calligra core library
Group: System/Libraries

%description -n %libtextlayout
Calligra core library.


%files -n %libtextlayout
%defattr(-,root,root)
%_kde_libdir/libtextlayout.so.%{libtextlayout_major}*

#----------------------------------------------------------------------

%define libkoreport_major 10
%define libkoreport %mklibname koreport %libkoreport_major

%package -n %libkoreport
Summary: Calligra core library
Group: System/Libraries

%description -n %libkoreport
Calligra core library.
It's an application-independent reporting library for the generation of both
printed and ODS and HTML reports from various sources of data. It provides a
gui based designer and renderer, and is currently used by Kexi for the
generation of database reports, and Calligra Plan for the generation of
planning reports.

%files -n %libkoreport
%defattr(-,root,root)
%_kde_libdir/libkoreport.so.%{libkoreport_major}*

#--------------------------------------------------------------------

%define libkokross_major 10
%define libkokross %mklibname kokross %libkokross_major

%package -n %libkokross
Summary: Calligra core library
Group: System/Libraries

%description -n %libkokross
Calligra core library.

%files -n %libkokross
%defattr(-,root,root)
%_kde_libdir/libkokross.so.%{libkokross_major}*

#--------------------------------------------------------------------

%define libkomain_major 10
%define libkomain %mklibname komain %libkomain_major

%package -n %libkomain
Summary: Calligra core library
Group: System/Libraries
Requires: %name-l10n

%description -n %libkomain
Calligra core library.

%files -n %libkomain
%defattr(-,root,root)
%_kde_libdir/libkomain.so.%{libkomain_major}*

#--------------------------------------------------------------------

%define libkopageapp_major 10
%define libkopageapp %mklibname kopageapp %libkopageapp_major

%package -n %libkopageapp
Summary: Calligra core library
Group: System/Libraries

%description -n %libkopageapp
Calligra core library.

%files -n %libkopageapp
%defattr(-,root,root)
%_kde_libdir/libkopageapp.so.%{libkopageapp_major}*

#--------------------------------------------------------------------

%define libkotext_major 10
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
%_kde_libdir/libkotext.so.%{libkotext_major}*

#--------------------------------------------------------------------
%define libkoodf_major 10
%define libkoodf %mklibname koodf %libkoodf_major

%package -n %libkoodf
Summary: Calligra core library
Group: System/Libraries

%description -n %libkoodf
Calligra core library.
ODF Library

%files -n %libkoodf
%defattr(-,root,root)
%_kde_libdir/libkoodf.so.%{libkoodf_major}*

#--------------------------------------------------------------------

%define liblibwmf_major 10
%define liblibwmf %mklibname libwmf %liblibwmf_major

%package -n %liblibwmf
Summary: Calligra core library
Group: System/Libraries

%description -n %liblibwmf
Calligra core library.

%files -n %liblibwmf
%defattr(-,root,root)
%_kde_libdir/liblibwmf.so.%{liblibwmf_major}*

#--------------------------------------------------------------------

%define libflake_major 10
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
%_kde_libdir/libflake.so.%{libflake_major}*

#--------------------------------------------------------------------

%define libpigmentcms_major 10
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
%_kde_libdir/libpigmentcms.so.%{libpigmentcms_major}*

#--------------------------------------------------------------------

%define libkformdesigner_major 10
%define libkformdesigner %mklibname kformdesigner %libkformdesigner_major

%package -n %libkformdesigner
Summary: Calligra core library
Group: System/Libraries

%description -n %libkformdesigner
Calligra core library.

%files -n %libkformdesigner
%defattr(-,root,root)
%_kde_libdir/libkformdesigner.so.%{libkformdesigner_major}*

#--------------------------------------------------------------------

%define libkochart_major 10
%define libkochart %mklibname kochart %libkochart_major

%package -n %libkochart
Summary: Calligra core library
Group: System/Libraries

%description -n %libkochart
Calligra core library.

%files -n %libkochart
%defattr(-,root,root)
%_kde_libdir/libkochart.so.%{libkochart_major}*

#--------------------------------------------------------------------
%define kundo2_major 10
%define libkundo2 %mklibname kundo2_ %kundo2_major

%package -n %libkundo2
Summary: Calligra core library
Group: System/Libraries

%description -n %libkundo2
Calligra core library.

%files -n %libkundo2

%_kde_libdir/libkundo2.so.%{kundo2_major}*

#--------------------------------------------------------------------
%define rtfreader_major 10
%define librtfreader %mklibname rtfreader %rtfreader_major

%package -n %librtfreader
Summary: Calligra core library
Group: System/Libraries

%description -n %librtfreader
Calligra core library.

%files -n %librtfreader

%_kde_libdir/libRtfReader.so.%{rtfreader_major}*

#--------------------------------------------------------------------

%define librcps_plan_major 10
%define librcps_plan %mklibname rcps_plan %librcps_plan_major

%package -n %librcps_plan
Summary: Calligra core library
Group: System/Libraries

%description -n %librcps_plan
Calligra core library.

%files -n %librcps_plan
%_kde_libdir/librcps_plan.so.%{librcps_plan_major}*

#--------------------------------------------------------------------

%define wordsprivate_major 10
%define libwordsprivate %mklibname wordsprivate %wordsprivate_major

%package -n %libwordsprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libwordsprivate
Calligra core library.

%files -n %libwordsprivate
%defattr(-,root,root)
%_kde_libdir/libwordsprivate.so.%{wordsprivate_major}*

#--------------------------------------------------------------------

%define chartshapelib_major 10
%define libchartshapelib %mklibname chartshapelib %chartshapelib_major

%package -n %libchartshapelib
Summary: Calligra core library
Group: System/Libraries

%description -n %libchartshapelib
Calligra core library.

%files -n %libchartshapelib
%defattr(-,root,root)
%_kde_libdir/libchartshapelib.so.%{chartshapelib_major}*

#--------------------------------------------------------------------
%define kplatomodels_major 10
%define  libkplatomodels %mklibname kplatomodels %kplatomodels_major

%package -n %libkplatomodels
Summary: Calligra core library
Group: System/Libraries

%description -n %libkplatomodels
Calligra core library.

%files -n %libkplatomodels
%defattr(-,root,root)
%_kde_libdir/libkplatomodels.so.%{kplatomodels_major}*

#-------------------------------------------------------------------

%define  kplatokernel_major 10
%define  libkplatokernel %mklibname kplatokernel %kplatokernel_major

%package -n %libkplatokernel
Summary: Calligra core library
Group: System/Libraries

%description -n %libkplatokernel
Calligra core library.

%files -n %libkplatokernel
%defattr(-,root,root)
%_kde_libdir/libkplatokernel.so.%{kplatokernel_major}*

#--------------------------------------------------------------------

%define planprivate_major 10
%define libplanprivate %mklibname planprivate %planprivate_major

%package -n %libplanprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libplanprivate
Calligra core library.

%files -n %libplanprivate
%defattr(-,root,root)
%_kde_libdir/libplanprivate.so.%{planprivate_major}*

#--------------------------------------------------------------------

%define kplatoui_major 10
%define libkplatoui %mklibname kplatoui %kplatoui_major

%package -n %libkplatoui
Summary: Calligra core library
Group: System/Libraries

%description -n %libkplatoui
Calligra core library.

%files -n %libkplatoui
%defattr(-,root,root)
%_kde_libdir/libkplatoui.so.%{kplatoui_major}*

#--------------------------------------------------------------------

%define planworkapp_major 10
%define libplanworkapp %mklibname planworkapp %planworkapp_major

%package -n %libplanworkapp
Summary: Calligra core library
Group: System/Libraries

%description -n %libplanworkapp
Calligra core library.

%files -n %libplanworkapp
%defattr(-,root,root)
%_kde_libdir/libplanworkapp.so.%{planworkapp_major}*

#--------------------------------------------------------------------

%define kplatoworkfactory_major 10
%define libplanworkfactory %mklibname kplatoworkfactory %kplatoworkfactory_major

%package -n %libplanworkfactory
Summary: Calligra core library
Group: System/Libraries
Obsoletes: %{_lib}kplatoworkapp8 < %{EVRD}

%description -n %libplanworkfactory
Calligra core library.

%files -n %libplanworkfactory
%defattr(-,root,root)
%_kde_libdir/libplanworkfactory.so.%{kplatoworkfactory_major}*

#--------------------------------------------------------------------

%define sheets_major 10
%define libcalligrasheetscommon %mklibname calligrasheetscommon %sheets_major

%package -n %libcalligrasheetscommon
Summary: Calligra core library
Group: System/Libraries
Obsoletes: %mklibname calligratablescommon 9

%description -n %libcalligrasheetscommon
Calligra core library.

%files -n %libcalligrasheetscommon
%defattr(-,root,root)
%_kde_libdir/libcalligrasheetscommon.so.%{sheets_major}*

#--------------------------------------------------------------------

%define sheetsodf_major 10
%define libcalligrasheetsodf %mklibname calligrasheetsodf %sheetsodf_major

%package -n %libcalligrasheetsodf
Summary: Calligra core library
Group: System/Libraries
Obsoletes: %mklibname calligratablesodf 9

%description -n %libcalligrasheetsodf
Calligra core library.

%files -n %libcalligrasheetsodf
%defattr(-,root,root)
%_kde_libdir/libcalligrasheetsodf.so.%{sheetsodf_major}*

#--------------------------------------------------------------------

%define calligrastageprivate_major 10
%define libcalligrastageprivate %mklibname calligrastageprivate %calligrastageprivate_major

%package -n %libcalligrastageprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libcalligrastageprivate
Calligra core library.

%files -n %libcalligrastageprivate
%defattr(-,root,root)
%_kde_libdir/libcalligrastageprivate.so.%{calligrastageprivate_major}*

#--------------------------------------------------------------------

%define  kdchart_major 10
%define  libkdchart %mklibname kdchart  %kdchart_major

%package -n %libkdchart
Summary: Calligra core library
Group: System/Libraries

%description -n %libkdchart
Calligra core library.

%files -n %libkdchart
%defattr(-,root,root)
%_kde_libdir/libkdchart.so.%{kdchart_major}*

#--------------------------------------------------------------------

%package -n katelier
Summary: Krita and karbon meta package
Group: Graphical desktop/KDE
Requires: krita = %{EVRD}
Requires: karbon = %{EVRD}

%description -n katelier
Krita and karbon meta package

%files -n katelier

#--------------------------------------------------------------------

%define  libkritaui_major 10
%define  libkritaui %mklibname kritaui  %libkritaui_major

%package -n %libkritaui
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritaui
Calligra core library.

%files -n %libkritaui
%defattr(-,root,root)
%_kde_libdir/libkritaui.so.%{libkritaui_major}*

#--------------------------------------------------------------------

%define  libkritaimage_major 10
%define  libkritaimage %mklibname kritaimage  %libkritaimage_major

%package -n %libkritaimage
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritaimage
Calligra core library.

%files -n %libkritaimage
%defattr(-,root,root)
%_kde_libdir/libkritaimage.so.%{libkritaimage_major}*

#--------------------------------------------------------------------

%define  libkritalibbrush_major 10
%define  libkritalibbrush %mklibname kritalibbrush  %libkritalibbrush_major

%package -n %libkritalibbrush
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritalibbrush
Calligra core library.

%files -n %libkritalibbrush
%defattr(-,root,root)
%_kde_libdir/libkritalibbrush.so.%{libkritalibbrush_major}*

#--------------------------------------------------------------------

%define  libkritalibpaintop_major 10
%define  libkritalibpaintop %mklibname kritalibpaintop  %libkritalibpaintop_major

%package -n %libkritalibpaintop
Summary: Calligra core library
Group: System/Libraries

%description -n %libkritalibpaintop
Calligra core library.

%files -n %libkritalibpaintop
%defattr(-,root,root)
%_kde_libdir/libkritalibpaintop.so.%{libkritalibpaintop_major}*

#--------------------------------------------------------------------

%define  libkoplugin_major 10
%define  libkoplugin %mklibname koplugin  %libkoplugin_major

%package -n %libkoplugin
Summary: Calligra core library
Group: System/Libraries

%description -n %libkoplugin
Calligra core library.

%files -n %libkoplugin
%defattr(-,root,root)
%_kde_libdir/libkoplugin.so.%{libkoplugin_major}*

#--------------------------------------------------------------------

%define  libkowidgets_major 10
%define  libkowidgets %mklibname kowidgets  %libkowidgets_major
#
%package -n %libkowidgets
Summary: Calligra core library
Group: System/Libraries

%description -n %libkowidgets
Calligra core library.

%files -n %libkowidgets
%defattr(-,root,root)
%_kde_libdir/libkowidgets.so.%{libkowidgets_major}*

#--------------------------------------------------------------------


%define  karboncommon_major 10
%define  libkarboncommon %mklibname karboncommon  %karboncommon_major

%package -n %libkarboncommon
Summary: Calligra core library
Group: System/Libraries

%description -n %libkarboncommon
Calligra core library.

%files -n %libkarboncommon
%defattr(-,root,root)
%_kde_libdir/libkarboncommon.so.%{karboncommon_major}*

#--------------------------------------------------------------------

%define  karbonui_major 10
%define  libkarbonui %mklibname karbonui  %karbonui_major

%package -n %libkarbonui
Summary: Calligra core library
Group: System/Libraries

%description -n %libkarbonui
Calligra core library.

%files -n %libkarbonui
%defattr(-,root,root)
%_kde_libdir/libkarbonui.so.%{karbonui_major}*

#--------------------------------------------------------------------



%define libkformulalib_major 10
%define libkformulalib %mklibname kformulalib %libkformulalib_major

%package -n %libkformulalib
Summary: Calligra core library
Group: System/Libraries

%description -n %libkformulalib
Calligra core library.

%files -n %libkformulalib
%defattr(-,root,root)
%_kde_libdir/libkformulalib.so.%{libkformulalib_major}*

#--------------------------------------------------------------------
   
%define libkexicore_major 10
%define libkexicore %mklibname kexicore %libkexicore_major
   
%package -n %libkexicore
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexicore
Calligra core library.

%files -n %libkexicore
%defattr(-,root,root)
%_kde_libdir/libkexicore.so.%{libkexicore_major}*

#--------------------------------------------------------------------

%define libkexidatatable_major 10
%define libkexidatatable %mklibname kexidatatable %libkexidatatable_major

%package -n %libkexidatatable
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexidatatable
Calligra core library.

%files -n %libkexidatatable
%defattr(-,root,root)
%_kde_libdir/libkexidatatable.so.%{libkexidatatable_major}*

#--------------------------------------------------------------------

%define libkexidb_major 10
%define libkexidb %mklibname kexidb %libkexidb_major

%package -n %libkexidb
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexidb
Calligra core library.

%files -n %libkexidb
%defattr(-,root,root)
%_kde_libdir/libkexidb.so.%{libkexidb_major}*

#--------------------------------------------------------------------

%define libkexiextendedwidgets_major 10
%define libkexiextendedwidgets %mklibname kexiextendedwidgets %libkexiextendedwidgets_major

%package -n %libkexiextendedwidgets
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexiextendedwidgets
Calligra core library.

%files -n %libkexiextendedwidgets
%defattr(-,root,root)
%_kde_libdir/libkexiextendedwidgets.so.%{libkexiextendedwidgets_major}*

#--------------------------------------------------------------------

%define libkexiformutils_major 10
%define libkexiformutils %mklibname kexiformutils %libkexiformutils_major

%package -n %libkexiformutils
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexiformutils
Calligra core library.

%files -n %libkexiformutils
%defattr(-,root,root)
%_kde_libdir/libkexiformutils.so.%{libkexiformutils_major}*

#--------------------------------------------------------------------

%define libkeximain_major 10
%define libkeximain %mklibname keximain %libkeximain_major

%package -n %libkeximain
Summary: Calligra core library
Group: System/Libraries

%description -n %libkeximain
Calligra core library.

%files -n %libkeximain
%defattr(-,root,root)
%_kde_libdir/libkeximain.so.%{libkeximain_major}*

#--------------------------------------------------------------------

%define libkeximigrate_major 10
%define libkeximigrate %mklibname keximigrate %libkeximigrate_major

%package -n %libkeximigrate
Summary: Calligra core library
Group: System/Libraries

%description -n %libkeximigrate
Calligra core library.

%files -n %libkeximigrate
%defattr(-,root,root)
%_kde_libdir/libkeximigrate.so.%{libkeximigrate_major}*

#--------------------------------------------------------------------

%define libkexirelationsview_major 10
%define libkexirelationsview %mklibname kexirelationsview %libkexirelationsview_major

%package -n %libkexirelationsview
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexirelationsview
Calligra core library.

%files -n %libkexirelationsview
%defattr(-,root,root)
%_kde_libdir/libkexirelationsview.so.%{libkexirelationsview_major}*

#--------------------------------------------------------------------

%define libkexiutils_major 10
%define libkexiutils %mklibname kexiutils %libkexiutils_major
   
%package -n %libkexiutils
Summary: Calligra core library
Group: System/Libraries
   
%description -n %libkexiutils
Calligra core library.
   
%files -n %libkexiutils
%defattr(-,root,root)
%_kde_libdir/libkexiutils.so.%{libkexiutils_major}*

#--------------------------------------------------------------------

%define libkexiguiutils_major 10
%define libkexiguiutils %mklibname kexiguiutils %libkexiguiutils_major

%package -n %libkexiguiutils
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexiguiutils
Calligra core library.

%files -n %libkexiguiutils
%defattr(-,root,root)
%_kde_libdir/libkexiguiutils.so.%{libkexiguiutils_major}*

#--------------------------------------------------------------------

%define libkexidataviewcommon_major 10
%define libkexidataviewcommon %mklibname kexidataviewcommon %libkexidataviewcommon_major

%package -n %libkexidataviewcommon
Summary: Calligra core library
Group: System/Libraries

%description -n %libkexidataviewcommon
Calligra core library.

%files -n %libkexidataviewcommon
%defattr(-,root,root)
%_kde_libdir/libkexidataviewcommon.so.%{libkexidataviewcommon_major}*

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
%_kde_libdir/libkowv2.so.%{libkowv2_major}*

#--------------------------------------------------------------------

%define libmsooxml_major 10
%define libmsooxml %mklibname msooxml %libmsooxml_major
   
%package -n %libmsooxml
Summary: Calligra core library
Group: System/Libraries

%description -n %libmsooxml
Calligra core library.
   
%files -n %libmsooxml
%defattr(-,root,root)
%_kde_libdir/libmsooxml.so.%{libmsooxml_major}*

#--------------------------------------------------------------------

%define libkoproperty_major 10
%define libkoproperty %mklibname koproperty %libkoproperty_major
   
%package -n %libkoproperty
Summary: Calligra core library
Group: System/Libraries
   
%description -n %libkoproperty
Calligra core library.
   
%files -n %libkoproperty
%defattr(-,root,root)
%_kde_libdir/libkoproperty.so.%{libkoproperty_major}*

#--------------------------------------------------------------------

%define libflowprivate_major 10
%define libflowprivate %mklibname flowprivate %libflowprivate_major

%package -n %libflowprivate
Summary: Calligra core library
Group: System/Libraries

%description -n %libflowprivate
Calligra core library.

%files -n %libflowprivate
%defattr(-,root,root)
%_kde_libdir/libflowprivate.so.%{libflowprivate_major}*

#--------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files for developing calligra applications
Requires: %libchartshapelib = %{EVRD}
Requires: %libflake = %{EVRD}
Requires: %libkarboncommon = %{EVRD}
Requires: %libkarbonui = %{EVRD}
Requires: %libkdchart = %{EVRD}
Requires: %libkexicore = %{EVRD}
Requires: %libkexidatatable = %{EVRD}
Requires: %libkexidataviewcommon = %{EVRD}
Requires: %libkexidb = %{EVRD}
Requires: %libkexiextendedwidgets = %{EVRD}
Requires: %libkexiformutils = %{EVRD}
Requires: %libkexiguiutils = %{EVRD}
Requires: %libkeximain = %{EVRD}
Requires: %libkeximigrate = %{EVRD}
Requires: %libkexirelationsview = %{EVRD}
Requires: %libkexiutils = %{EVRD}
Requires: %libkformdesigner = %{EVRD}
Requires: %libkformulalib = %{EVRD}
Requires: %libkochart = %{EVRD}
Requires: %libkokross = %{EVRD}
Requires: %libkomain = %{EVRD}
Requires: %libkoodf = %{EVRD}
Requires: %libkopageapp = %{EVRD}
Requires: %libkoplugin = %{EVRD}
Requires: %libkoproperty = %{EVRD}
Requires: %libkoreport = %{EVRD}
Requires: %libkotext = %{EVRD}
Requires: %libkowidgets = %{EVRD}
Requires: %libkowv2 = %{EVRD}
Requires: %libkplatokernel = %{EVRD}
Requires: %libkplatomodels = %{EVRD}
Requires: %libplanprivate = %{EVRD}
Requires: %libkplatoui = %{EVRD}
Requires: %libplanworkapp = %{EVRD}
Requires: %libplanworkfactory = %{EVRD}
Requires: %libcalligrastageprivate = %{EVRD}
Requires: %libkritaimage = %{EVRD}
Requires: %libkritalibbrush = %{EVRD}
Requires: %libkritalibpaintop = %{EVRD}
Requires: %libkritaui = %{EVRD}
Requires: %libcalligrasheetscommon = %{EVRD}
Requires: %libcalligrasheetsodf = %{EVRD}
Requires: %libwordsprivate = %{EVRD}
Requires: %libmsooxml = %{EVRD}
Requires: %libpigmentcms = %{EVRD}
Requires: %liblibwmf = %{EVRD}
Requires: %libkundo2 = %{EVRD}
Requires: %librtfreader = %{EVRD}
Requires: %librcps_plan = %{EVRD}
Requires: %name-core = %{EVRD}
Conflicts: koffice2-kchart
Conflicts: karbon < 11:1.9.95.8-3
Conflicts: kchart < 11:1.9.95.8-3
Conflicts: kivio < 11:1.9.95.8-3
Conflicts: kplato < 11:1.9.95.8-3
Conflicts: kpresenter < 11:1.9.95.8-3
Conflicts: krita < 11:1.9.95.8-3
Conflicts: kspread < 11:1.9.95.8-3
Conflicts: koffice-core < 11:1.9.98.5-3
Conflicts: kword < 11:1.9.95.8-3
Obsoletes: koffice2-devel
Obsoletes: koffice-devel

%description devel
Header files needed for developing calligra applications.

%files devel
%defattr(-,root,root)
%_kde_appsdir/cmake/*/*
%_kde_includedir/*
%_kde_libdir/libchartshapelib.so
%_kde_libdir/libflake.so
%_kde_libdir/libkarboncommon.so
%_kde_libdir/libkarbonui.so
%_kde_libdir/libkdchart.so
%_kde_libdir/libkexicore.so
%_kde_libdir/libkexidatatable.so
%_kde_libdir/libkexidataviewcommon.so
%_kde_libdir/libkexidb.so
%_kde_libdir/libkexiextendedwidgets.so
%_kde_libdir/libkexiformutils.so
%_kde_libdir/libkexiguiutils.so
%_kde_libdir/libkeximain.so
%_kde_libdir/libkeximigrate.so
%_kde_libdir/libkexirelationsview.so
%_kde_libdir/libkexiutils.so
%_kde_libdir/libkformdesigner.so
%_kde_libdir/libkformulalib.so
%_kde_libdir/libkochart.so
%_kde_libdir/libkokross.so
%_kde_libdir/libkomain.so
%_kde_libdir/libkoodf.so
%_kde_libdir/libkopageapp.so
%_kde_libdir/libkoplugin.so
%_kde_libdir/libkoproperty.so
%_kde_libdir/libkoreport.so
%_kde_libdir/libkotext.so
%_kde_libdir/libkowidgets.so
%_kde_libdir/libkowv2.so
%_kde_libdir/libkplatokernel.so
%_kde_libdir/libkplatomodels.so
%_kde_libdir/libplanprivate.so
%_kde_libdir/libkplatoui.so
%_kde_libdir/libplanworkapp.so
%_kde_libdir/libplanworkfactory.so
%_kde_libdir/libcalligrastageprivate.so
%_kde_libdir/libkritaimage.so
%_kde_libdir/libkritalibbrush.so
%_kde_libdir/libkritalibpaintop.so
%_kde_libdir/libkritaui.so
%_kde_libdir/libcalligrasheetscommon.so
%_kde_libdir/libcalligrasheetsodf.so
%_kde_libdir/libwordsprivate.so
%_kde_libdir/libmsooxml.so
%_kde_libdir/libpigmentcms.so
%_kde_libdir/libflowprivate.so
%_kde_libdir/libtextlayout.so
%_kde_libdir/liblibwmf.so
%_kde_libdir/libkundo2.so
%_kde_libdir/libRtfReader.so
%_kde_libdir/librcps_plan.so

#--------------------------------------------------------------------
%if %_mobile
%package mobile
Summary: mobile user interaction of Calligra Suite
Group:   Graphical desktop/KDE

%description mobile
Calligra Mobile is a mobile user interaction of Calligra Suite

%files mobile
%defattr(0755,root,root,0755)
%_kde_bindir/calligramobile
%defattr(0644,root,root,0755)
%_kde_datadir/applications/hildon/calligramobile.desktop
%_kde_datadir/calligramobile-templates/
%_kde_datadir/dbus-1/services/com.nokia.CalligraMobile.service
%_kde_iconsdir/hicolor/178x200/apps/calligramobile.png
%_kde_iconsdir/hicolor/48x48/hildon/Document.png
%_kde_iconsdir/hicolor/48x48/hildon/Presenter.png
%_kde_iconsdir/hicolor/48x48/hildon/SpreadSheet.png
%_kde_iconsdir/hicolor/64x64/apps/calligramobile.png

%endif
#--------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1 -b .openjpeg~

%build
#sh initrepo.sh
%if %_mobile
%cmake_kde4 -DIHAVEPATCHEDQT:BOOL=TRUE
%else
%cmake_kde4 -DBUILD_mobile=OFF -DIHAVEPATCHEDQT:BOOL=TRUE
%endif
make

%if %{compile_apidox}
make apidox
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
