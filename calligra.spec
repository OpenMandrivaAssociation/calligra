%global optflags %{optflags} -Wno-register

# Seems to be broken at the moment
%bcond_without okular

%define compile_apidox 0
%define _mobile 0
%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define major 19

#define snapshot 20240806

%define stable %([ `echo %{version} |cut -d. -f3` -ge 70 ] && echo -n un; echo -n stable)

Summary:	Set of office applications for KDE
Name:		calligra
Version:	25.08.2
Release:	%{?snapshot:0.%{snapshot}.}1
Group:		Office
License:	GPLv2+ and LGPLv2+ and GFDL
Url:		https://www.calligra.org
%if 0%{?snapshot:1}
Source0:	https://invent.kde.org/office/calligra/-/archive/master/calligra-master.tar.bz2#/calligra-%{snapshot}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Source1:	%{name}.rpmlintrc
Patch0:		calligra-buildfix.patch
#Patch1:		calligra-libgit-api-update.patch

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Eigen3)
BuildRequires:	locales-extra-charsets
BuildRequires:	ninja
BuildRequires:	pstoedit
BuildRequires:	boost-devel
BuildRequires:	freetds-devel
BuildRequires:	getfem-devel
BuildRequires:	glpk-devel
BuildRequires:	jbig-devel
BuildRequires:	plasma6-marble-devel
BuildRequires:	mariadb-devel
%if %{with okular}
BuildRequires:	plasma6-okular-devel
%endif
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
BuildRequires:	pkgconfig(libodfgen-0.1)
BuildRequires:	pkgconfig(libpqxx)
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(libvisio-0.1)
BuildRequires:	pkgconfig(libwpd-0.10)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libwps-0.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(python)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KChart6)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
%if %compile_apidox
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
# No longer included in 3.x, but might come back at some point
Obsoletes:	%{name}-semanticitem < %{EVRD}
Obsoletes:	%{name}-author < %{EVRD}
Obsoletes:	%{name}-kchart < %{EVRD}
Obsoletes:	%{name}-kformula < %{EVRD}
Obsoletes:	%{name}-stateshape < %{EVRD}
Obsoletes:	%{name}-active < %{EVRD}
Recommends:	%{name}-flow
Recommends:	%{name}-karbon
Recommends:	%{name}-sheets
Recommends:	%{name}-stage
Recommends:	%{name}-words
Recommends:	%{name}-plan

%if !%{with okular}
Obsoletes:	%{name}-okular-odp <= %{EVRD}
Obsoletes:	%{name}-okular-odt <= %{EVRD}
%endif

Obsoletes:	%mklibname koversion

# Those were in KDE4 versions of calligra...
%define obsoletelibs14 calligradb calligrakdchart calligrakdgantt flowprivate kformdesigner kformula kokross koproperty kordf koreport kplatokernel kplatomodels kplatoui planprivate planworkapp rcps_plan planworkfactory
%{expand:%(for lib in %{obsoletelibs14}; do echo Obsoletes: %%mklibname $lib 14; echo; done)}
# Those were in Calligra 3.2
%define obsoletelibs18 calligrasheetscommon calligrasheetsodf
%{expand:%(for lib in %{obsoletelibs18}; do echo Obsoletes: %%mklibname $lib 18; echo; done)}

%description
Office applications for the K Desktop Environment.

Calligra contains:
   * Words: word processor
   * Table: spreadsheet
   * Stage: presentations
   * Flow: diagram generator
   * Some filters (Excel 97, Winword 97/2000, etc.)
   * karbon: the scalable vector drawing application for KDE.
   * plan: a project management.

%files

%define libpackage()\
%{expand:%%define nib %(echo %{1} | sed 's,[0-9]$,&_,' )}\
%{expand:%%global lib%{1} %%mklibname %{nib}}\
%%package -n %{expand:%{lib%{1}}}\
Summary: The %{1} library, a part of %{name}\
Group: System/Libraries\
%%description -n %{expand:%{lib%{1}}}\
The %{1} library, a part of %{name}.\
%%files -n %{expand:%{lib%{1}}}\
%{_libdir}/lib%{1}.so.*\
%{nil}

# libpackages
# Gone in 4.0.1: braindumpcore
%global calligralibs basicflakes calligrastageprivate flake karboncommon karbonui komain komsooxml koodf koodfreader kopageapp koplugin kotext kotextlayout kovectorimage kowidgets kowidgetutils kundo2 pigmentcms wordsprivate koformula kostore autocorrection calligrasheetscore calligrasheetsengine calligrasheetspartlib calligrasheetsui
%if %{with okular}
%global calligralibs %{calligralibs} kookularGenerator_odp kookularGenerator_odt
%endif
%{expand:%(for lib in %{calligralibs}; do cat <<EOF
%%libpackage $lib %{major}
EOF
done)}
%libpackage kowv2 9

#--------------------------------------------------------------------

%define oldlibkoodf2 %mklibname koodf2 18
%define libkoodf2 %mklibname koodf2

%package -n %{libkoodf2}
Summary:        Calligra library
Group:          System/Libraries
%rename %{_lib}koodf214
%rename %{oldlibkoodf2}

%description -n %{libkoodf2}
Calligra library.

%files -n %{libkoodf2}
%{_libdir}/libkoodf2.so.*

#--------------------------------------------------------------------

%define oldlibRtfReader %mklibname RtfReader 18
%define libRtfReader %mklibname RtfReader

%package -n %{libRtfReader}
Summary:        Calligra library
Group:          System/Libraries
%rename %{_lib}rtfreader14
%rename %{oldlibRtfReader}

%description -n %{libRtfReader}
Calligra library.

%files -n %{libRtfReader}
%{_libdir}/libRtfReader.so.*

#--------------------------------------------------------------------

%package core
Group:		Office
Summary:	Set of office applications for KDE
Obsoletes:	koffice-core < 15:2.4

%description core
Common files for Calligra.

%files core -f calligra.lang -f koconverter.lang -f kocolorspaces.lang -f calligralauncher.lang
%{_bindir}/calligraconverter
%{_bindir}/calligralauncher
%{_bindir}/cstester
%{_bindir}/cstrunner
%{_bindir}/visualimagecompare
%{_datadir}/mime/packages/calligra_svm.xml
%{_datadir}/applications/calligra.desktop
%{_datadir}/applications/org.kde.calligra.desktop
%{_datadir}/calligra_shape_state
%{_qtdir}/plugins/calligra/colorspaces
%{_qtdir}/plugins/calligra/dockers
%dir %{_qtdir}/plugins/calligra/formatfilters
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_applixspread2kspread.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_applixword2odt.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_ascii2words.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_csv2sheets.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_dbase2kspread.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_doc2odt.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_docx2odt.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_eps2svgai.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_gnumeric2sheets.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_html2ods.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_karbon1x2karbon.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_karbon2image.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_karbon2svg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_karbon2wmf.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_key2odp.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_kpr2odp.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_kspread2tex.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_odt2ascii.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_odt2docx.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_odt2epub2.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_odt2html.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_odt2mobi.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_odt2wiki.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_opencalc2sheets.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_pdf2svg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_ppt2odp.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_pptx2odp.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_qpro2sheets.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_rtf2odt.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_sheets2csv.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_sheets2gnumeric.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_sheets2html.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_sheets2opencalc.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_svg2karbon.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_vsdx2odg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_wmf2svg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_wpd2odt.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_wpg2odg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_wpg2svg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_wps2odt.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_xfig2odg.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_xls2ods.so
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_xlsx2ods.so
%{_qtdir}/plugins/kf6/propertiesdialog/calligradocinfopropspage.so
%{_qtdir}/plugins/calligra/pageapptools
%dir %{_qtdir}/plugins/calligra/parts
%{_qtdir}/plugins/calligra/parts/calligrasheetspart.so
%{_qtdir}/plugins/calligra/parts/calligrastagepart.so
%{_qtdir}/plugins/calligra/parts/karbonpart.so
%{_qtdir}/plugins/calligra/presentationeventactions
%{_qtdir}/plugins/calligra/shapefiltereffects
%{_qtdir}/plugins/calligra/shapes
%{_qtdir}/plugins/calligra/textediting
%{_qtdir}/plugins/calligra/textinlineobjects
%{_qtdir}/plugins/calligra/tools
%{_qtdir}/qml/org/kde/calligra
%dir %{_datadir}/calligra
%{_datadir}/calligra/autocorrect
%{_datadir}/calligra/calligra_shell.rc
%{_datadir}/calligra/cursors
%{_datadir}/calligra/icons
%{_datadir}/calligra/palettes
%{_datadir}/calligra/pics
%{_datadir}/calligra/stencils
%{_datadir}/calligra/styles
%{_datadir}/calligra/thesaurus
%{_datadir}/calligra_shape_music
%{_datadir}/color/icc/calligra
%{_datadir}/icons/*/*/*/calligrastage.*
%{_datadir}/icons/*/*/*/calligrakarbon.*
%{_datadir}/icons/*/*/*/office-chart-stock-candlestick.*
%{_datadir}/icons/*/*/*/office-chart-stock-hlc.*
%{_datadir}/icons/*/*/*/office-chart-stock-ohlc.*
%{_qtdir}/plugins/kf6/thumbcreator/calligraimagethumbnail.so
%{_qtdir}/plugins/kf6/thumbcreator/calligrathumbnail.so
%{_datadir}/metainfo/org.kde.calligra.metainfo.xml

%if 0
# Seems to be dead (at least disabled) -- not in 4.0.1
#--------------------------------------------------------------------
%package gemini
Summary:	Mobile version of the Calligra office suite
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%libpackage gemini %{major}

%description gemini
Mobile version of the Calligra office suite

%files gemini
%{_bindir}/calligragemini*
%{_datadir}/applications/org.kde.calligra.gemini.desktop
%{_qtdir}/qml/Calligra/Gemini
%{_datadir}/calligragemini
%{_datadir}/icons/*/*/*/calligragemini.*
%{_datadir}/metainfo/org.kde.calligra.gemini.metainfo.xml
%endif

#--------------------------------------------------------------------

%package braindump
Summary:	Braindump for calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description braindump
A tool that helps visualize the contents of your brain

%files braindump -f braindump.lang
%{_bindir}/braindump
%{_libdir}/libbraindumpcore.so*
%{_datadir}/applications/org.kde.calligra.braindump.desktop
%{_datadir}/icons/hicolor/*/apps/braindump.*
%{_datadir}/icons/hicolor/*/apps/org.kde.calligra.braindump.*
%{_datadir}/kxmlgui5/braindump
%{_datadir}/metainfo/org.kde.calligra.braindump.metainfo.xml

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

%files words -f calligrawords.lang
%{_sysconfdir}/xdg/calligrawordsrc
%{_datadir}/applications/org.kde.calligrawords_ascii.desktop
%{_bindir}/calligrawords
%{_datadir}/mime/packages/wiki-format.xml
%{_qtdir}/plugins/calligra/parts/calligrawordspart.so
%{_datadir}/calligrawords
%{_datadir}/kxmlgui5/calligrawords
%{_datadir}/templates/.source/TextDocument.odt
%{_datadir}/templates/TextDocument.desktop
%{_datadir}/icons/*/*/*/calligrawords.*
%{_datadir}/kio/servicemenus/words_print.desktop
%{_datadir}/applications/org.kde.calligra.words.desktop
%{_datadir}/metainfo/org.kde.calligra.words.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.kde.calligra.words.svg

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

%files sheets -f calligrasheets.lang -f sheets.lang
%{_sysconfdir}/xdg/calligrasheetsrc
%{_bindir}/calligrasheets
%{_datadir}/kxmlgui5/calligrasheets
%{_datadir}/calligrasheets
%{_qtdir}/plugins/calligrasheets
%{_datadir}/config.kcfg/calligrasheets.kcfg
%{_datadir}/templates/.source/SpreadSheet.ods
%{_datadir}/templates/SpreadSheet.desktop
%{_datadir}/icons/*/*/*/calligrasheets.*
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_sheets2xls.so
%{_datadir}/kio/servicemenus/sheets_print.desktop
%{_datadir}/applications/org.kde.calligra.sheets.desktop
%{_datadir}/metainfo/org.kde.calligra.sheets.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.kde.calligra.sheets.svg

#--------------------------------------------------------------------

%package stage
Summary:	Presentation for calligra-suite
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	xdg-utils
Requires:	pstoedit
%rename	stage

%description stage
Stage is an easy to use yet still flexible presentation application. You can
easily create presentations containing a rich variety of elements,
from graphics to text, from charts to images.
Stage is extensible through a plugin system, so it is easy to add new effects,
new content elements or even new ways of managing your presentation. Because of
the integration with Calligra, all the power and flexibility of the Calligra
content elements are available to Stage.

%files stage -f calligrastage.lang -f stage.lang
%{_bindir}/calligrastage
%{_qtdir}/plugins/calligra/formatfilters/calligra_filter_pdf2odg.so
%{_datadir}/applications/org.kde.calligra.stage.desktop

%{_sysconfdir}/xdg/calligrastagerc
%{_datadir}/kxmlgui5/calligrastage
%{_datadir}/calligrastage
%{_qtdir}/plugins/calligrastage
%{_datadir}/templates/.source/Presentation.odp
%{_datadir}/templates/Presentation.desktop
%{_datadir}/metainfo/org.kde.calligra.stage.metainfo.xml
%{_datadir}/kio/servicemenus/stage_print.desktop
%{_datadir}/icons/hicolor/*/apps/org.kde.calligra.stage.svg

#--------------------------------------------------------------------

%package karbon
Summary:	Scalable drawing for calligra
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	pstoedit
%rename		karbon

%description karbon
Karbon is a vector drawing application with an user interface that is easy to
use, highly customizable and extensible.
That makes Karbon a great application for users starting to explore the world
of vector graphics as well as for artists wanting to create breathtaking vector
art.

%files karbon -f karbon.lang
%{_sysconfdir}/xdg/karbonrc
%{_bindir}/karbon
%{_qtdir}/plugins/karbon
%{_datadir}/templates/.source/Illustration.odg
%{_datadir}/templates/Illustration.desktop
%{_datadir}/kxmlgui5/karbon
%{_datadir}/karbon
%{_datadir}/kio/servicemenus/karbon_print.desktop
%{_datadir}/applications/org.kde.calligra.karbon.desktop
%{_datadir}/metainfo/org.kde.calligra.karbon.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.kde.calligra.karbon.svg

#--------------------------------------------------------------------

%if %{with okular}
#--------------------------------------------------------------------
%package -n okular-rtf
Summary:	RTF viewer plugin for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n okular-rtf
RTF viewer plugin for Okular

%files -n okular-rtf
%{_datadir}/applications/okularApplication_rtf_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_rtf_calligra.so

#--------------------------------------------------------------------
%package okular-odp
Summary:	ODP file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular
%rename		okular-odp

%description okular-odp
ODP file renderer for Okular.

%files okular-odp -f okularGenerator_odp.lang
%{_datadir}/applications/okularApplication_odp_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_odp_calligra.so

#--------------------------------------------------------------------
%package okular-odt
Summary:	ODT file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-odt
ODT file renderer for Okular.

%files okular-odt -f okularGenerator_odt.lang
%{_datadir}/applications/okularApplication_odt_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_odt_calligra.so

#--------------------------------------------------------------------

%package okular-doc
Summary:	Doc file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-doc
Doc file renderer for Okular.

%files okular-doc
%{_datadir}/applications/okularApplication_doc_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_doc_calligra.so

#--------------------------------------------------------------------

%package okular-docx
Summary:	Docx file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-docx
Docx file renderer for Okular.

%files okular-docx
%{_datadir}/applications/okularApplication_docx_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_docx_calligra.so

#--------------------------------------------------------------------

%package okular-powerpoint
Summary:	Powerpoint file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-powerpoint
Powerpoint file renderer for Okular.

%files okular-powerpoint
%{_datadir}/applications/okularApplication_powerpoint_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_powerpoint_calligra.so

#--------------------------------------------------------------------

%package okular-pptx
Summary:	PPTX file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-pptx
PPTX file renderer for Okular.

%files okular-pptx
%{_datadir}/applications/okularApplication_pptx_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_pptx_calligra.so

#--------------------------------------------------------------------

%package okular-wpd
Summary:	WPD file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-wpd
WPD file renderer for Okular.

%files okular-wpd
%{_datadir}/applications/okularApplication_wpd_calligra.desktop
%{_qtdir}/plugins/okular_generators/okularGenerator_wpd_calligra.so
%endif

#--------------------------------------------------------------------

%if %_mobile
%package mobile
Summary:	mobile user interaction of Calligra Suite
Group:		Graphical desktop/KDE

%description mobile
Calligra Mobile is a mobile user interaction of Calligra Suite.

%files mobile
%{_bindir}/calligramobile
%{_datadir}/applications/hildon/calligramobile.desktop
%{_datadir}/calligramobile-templates/
%{_datadir}/dbus-1/services/com.nokia.CalligraMobile.service
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
Requires:	%{libRtfReader} = %{EVRD}
Requires:	%{libkoodf2} = %{EVRD}

%description devel
Header files needed for developing calligra applications.

%files devel
%{expand:%(for lib in %{calligralibs}; do cat <<EOF
%%optional %{_libdir}/lib${lib}.so
EOF
done)}
#{_libdir}/libgemini.so
%{_libdir}/libkowv2.so
%{_libdir}/libRtfReader.so
%{_libdir}/libkoodf2.so

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n calligra-%{?snapshot:master}%{!?snapshot:%{version}}

%build
#sh initrepo.sh
%if %_mobile
%cmake -DIHAVEPATCHEDQT:BOOL=TRUE -DCALLIGRA_SHOULD_BUILD_STAGING:BOOL=ON \
	-DPACKAGERS_BUILD=ON -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON -DBUILD_WITH_QT6:BOOL=ON -G Ninja
%else
%cmake -DIHAVEPATCHEDQT:BOOL=TRUE -DCALLIGRA_SHOULD_BUILD_STAGING:BOOL=ON -DGHNS:BOOL=ON -DINSTALL_XLS_EXPORT_FILTER:BOOL=ON -DAKONADI_DBUS_INTERFACES_DIR=/usr/share/dbus-1/interfaces -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON -DBUILD_WITH_QT6:BOOL=ON \
	-DPACKAGERS_BUILD=ON -G Ninja
%endif
%ninja_build || ninja

%if %{compile_apidox}
%ninja_build apidox
%endif

%install
%ninja_install -C build

%if %compile_apidox
%ninja_build install-apidox DESTDIR=%{buildroot}/
list=`ls -d */ -1`;
echo $list;
for i in $list ; do
	cd $i;
		if grep '^include .*Doxyfile.am' Makefile.am; then
			echo "installing apidox from $i" ;
			ninja install-apidox DESTDIR=%{buildroot}/ ;
		fi
	cd ../;
done;
%endif

%if ! %{with okular}
# If we can't build okular bits, we don't need their translations
rm -rf %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/okular*
%endif

for i in \
	braindump \
	calligra \
	KarbonFilterEffects \
	KarbonTools \
	calligra-defaulttools \
	calligra-dockers \
	calligra-opener \
	calligra_semanticitem_contact \
	calligra_semanticitem_event \
	calligra_semanticitem_location \
	calligra_shape_artistictext \
	calligra_shape_chart \
	calligra_shape_comment \
	calligra_shape_formula \
	calligra_shape_music \
	calligra_shape_paths \
	calligra_shape_picture \
	calligra_shape_plugin \
	calligra_shape_spreadsheet \
	calligra_shape_template \
	calligra_shape_text \
	calligra_shape_threed \
	calligra_shape_vector \
	calligra_shape_video \
	calligra_shape_webshape \
	calligra_textediting_autocorrect \
	calligra_textediting_changecase \
	calligra_textediting_spellcheck \
	calligra_textediting_thesaurus \
	calligra_textinlineobject_variables \
	calligrafilters \
	calligralauncher \
	calligrasheets \
	calligrasheets_calendar \
	calligrasheets_solver \
	calligrastage \
	calligrawords \
	karbon \
	kocolorspaces \
	koconverter \
%if %{with okular}
	okularGenerator_odp \
	okularGenerator_odt \
%endif
	sheets \
	stage \
	; do
	%find_lang $i --with-html
done

cat calligra-*.lang calligra_*.lang calligrafilters.lang >>calligra.lang
cat calligrasheets_*.lang >>calligrasheets.lang
cat Karbon*.lang >>karbon.lang
