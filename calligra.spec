%global optflags %{optflags} -Wno-register

%bcond_without okular

%define compile_apidox 0
%define _mobile 0
%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define major 17

%define stable %([ `echo %{version} |cut -d. -f3` -ge 70 ] && echo -n un; echo -n stable)

Summary:	Set of office applications for KDE
Name:		calligra
#koffice has epoch 15. We need a higher epoch
Epoch:		16
Version:	3.2.1
Release:	1
Group:		Office
License:	GPLv2+ and LGPLv2+ and GFDL
Url:		http://www.calligra.org
%if "%{stable}" == "stable"
Source0:	http://download.kde.org/%{stable}/%{name}/%{version}/%{name}-%{version}.tar.xz
%else
Source0:	http://download.kde.org/%{stable}/%{name}/%{name}-%{version}.tar.xz
%endif
Source1:	%{name}.rpmlintrc

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	cmake(ECM)
BuildRequires:	pstoedit
BuildRequires:	boost-devel
BuildRequires:	freetds-devel
BuildRequires:	getfem-devel
BuildRequires:	glpk-devel
BuildRequires:	gmic-devel
BuildRequires:	jbig-devel
BuildRequires:	marble-devel
BuildRequires:	mariadb-devel
%if %{with okular}
BuildRequires:	okular-devel
%endif
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
# We could do this, but it's in contrib
#BuildRequires:	spnav-devel
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
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DesignerPlugin)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JS)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5UnitConversion)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KGantt)
BuildRequires:	cmake(KPropertyWidgets)
BuildRequires:	cmake(KReport)
BuildRequires:	cmake(KF5Holidays)
%if %compile_apidox
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
# No longer included in 3.x, but might come back at some point
Obsoletes:	%{name}-semanticitem < %{EVRD}
Obsoletes:	%{name}-author < %{EVRD}
Obsoletes:	%{name}-braindump < %{EVRD}
Obsoletes:	%{name}-kchart < %{EVRD}
Obsoletes:	%{name}-kformula < %{EVRD}
Obsoletes:	%{name}-stateshape < %{EVRD}
Obsoletes:	%{name}-active < %{EVRD}
Suggests:	%{name}-flow
Suggests:	%{name}-karbon
Suggests:	%{name}-sheets
Suggests:	%{name}-stage
Suggests:	%{name}-words
Suggests:	%{name}-plan

%if !%{with okular}
Obsoletes:	%{name}-okular-odp <= %{EVRD}
Obsoletes:	%{name}-okular-odt <= %{EVRD}
%endif

# Those were in KDE4 versions of calligra...
%define obsoletelibs calligradb calligrakdchart calligrakdgantt flowprivate kformdesigner kformula kokross koproperty kordf koreport kplatokernel kplatomodels kplatoui planprivate planworkapp rcps_plan braindumpcore planworkfactory
%{expand:%(for lib in %{obsoletelibs}; do echo Obsoletes: %%mklibname $lib 14; echo; done)}

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
%define calligralibs basicflakes calligrasheetscommon calligrasheetsodf calligrastageprivate flake karboncommon karbonui komain komsooxml koodf koodfreader kopageapp koplugin kotext kotextlayout kovectorimage koversion kowidgets kowidgetutils kundo2 pigmentcms wordsprivate koformula kookularGenerator_odp kookularGenerator_odt kostore
%{expand:%(for lib in %{calligralibs}; do cat <<EOF
%%libpackage $lib %{major}
EOF
done)}
%libpackage kowv2 9

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

%package core
Group:		Office
Summary:	Set of office applications for KDE
Obsoletes:	koffice-core < 15:2.4

%description core
Common files for Calligra.

%files core -f calligra.lang
%{_bindir}/calligra
%{_bindir}/calligraconverter
%{_bindir}/cstester
%{_bindir}/cstrunner
%{_bindir}/visualimagecompare
%{_sysconfdir}/xdg/calligra_stencils.knsrc
%{_datadir}/mime/packages/calligra_svm.xml
%{_datadir}/applications/calligra.desktop
%{_libdir}/qt5/plugins/calligra/colorspaces
%{_libdir}/qt5/plugins/calligra/dockers
%dir %{_libdir}/qt5/plugins/calligra/formatfilters
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_applixspread2kspread.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_applixword2odt.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_ascii2words.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_csv2sheets.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_dbase2kspread.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_doc2odt.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_docx2odt.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_eps2svgai.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_gnumeric2sheets.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_html2ods.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_karbon1x2karbon.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_karbon2image.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_karbon2svg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_karbon2wmf.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_key2odp.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_kpr2odp.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_kspread2tex.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_odt2ascii.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_odt2docx.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_odt2epub2.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_odt2html.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_odt2mobi.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_odt2wiki.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_opencalc2sheets.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_pdf2svg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_ppt2odp.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_pptx2odp.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_qpro2sheets.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_rtf2odt.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_sheets2csv.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_sheets2gnumeric.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_sheets2html.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_sheets2opencalc.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_svg2karbon.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_vsdx2odg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_wmf2svg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_wpd2odt.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_wpg2odg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_wpg2svg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_wps2odt.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_xfig2odg.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_xls2ods.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_xlsx2ods.so
%{_libdir}/qt5/plugins/calligra/pageapptools
%dir %{_libdir}/qt5/plugins/calligra/parts
%{_libdir}/qt5/plugins/calligra/parts/calligrasheetspart.so
%{_libdir}/qt5/plugins/calligra/parts/calligrastagepart.so
%{_libdir}/qt5/plugins/calligra/parts/karbonpart.so
%{_libdir}/qt5/plugins/calligra/presentationeventactions
%{_libdir}/qt5/plugins/calligra/shapefiltereffects
%{_libdir}/qt5/plugins/calligra/shapes
%{_libdir}/qt5/plugins/calligra/textediting
%{_libdir}/qt5/plugins/calligra/textinlineobjects
%{_libdir}/qt5/plugins/calligra/tools
%{_libdir}/qt5/plugins/calligradocinfopropspage.so
%{_libdir}/qt5/plugins/calligraimagethumbnail.so
%{_libdir}/qt5/plugins/calligrathumbnail.so
%{_libdir}/qt5/qml/org/kde/calligra
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
%{_datadir}/kservices5/calligradocinfopropspage.desktop
%{_datadir}/kservices5/calligra_odg_thumbnail.desktop
%{_datadir}/kservices5/ServiceMenus/calligra/words_print.desktop
%doc %lang(ca) %{_docdir}/HTML/ca/calligra
%doc %lang(de) %{_docdir}/HTML/de/calligra
%doc %lang(es) %{_docdir}/HTML/es/calligra
%doc %lang(fr) %{_docdir}/HTML/fr/calligra
%doc %lang(it) %{_docdir}/HTML/it/calligra
%doc %lang(nl) %{_docdir}/HTML/nl/calligra
%doc %lang(pt) %{_docdir}/HTML/pt/calligra
%doc %lang(pt_BR) %{_docdir}/HTML/pt_BR/calligra
%doc %lang(ru) %{_docdir}/HTML/ru/calligra
%doc %lang(sv) %{_docdir}/HTML/sv/calligra
%doc %lang(uk) %{_docdir}/HTML/uk/calligra
%doc %lang(et) %{_docdir}/HTML/et/calligra
%doc %lang(id) %{_docdir}/HTML/id/calligra

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
%{_libdir}/qt5/qml/Calligra/Gemini
%{_datadir}/applications/org.kde.calligragemini.desktop
%{_datadir}/calligragemini
%{_datadir}/icons/*/*/*/calligragemini.*
%{_datadir}/metainfo/org.kde.calligragemini.appdata.xml

#--------------------------------------------------------------------
%package -n okular-rtf
Summary:	RTF viewer plugin for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n okular-rtf
RTF viewer plugin for Okular

%files -n okular-rtf
%{_datadir}/kservices5/okularRtf_calligra.desktop
%{_datadir}/applications/okularApplication_rtf_calligra.desktop
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_rtf_calligra.so

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
%{_sysconfdir}/xdg/calligrawordsrc
%{_datadir}/applications/org.kde.calligrawords_ascii.desktop
%{_bindir}/calligrawords
%{_datadir}/kservices5/words_*_thumbnail.desktop
%{_datadir}/mime/packages/wiki-format.xml
%{_libdir}/qt5/plugins/calligra/parts/calligrawordspart.so
%{_datadir}/calligrawords
%{_datadir}/kxmlgui5/calligrawords
%{_datadir}/metainfo/org.kde.calligrawords.appdata.*
%{_datadir}/templates/.source/TextDocument.odt
%{_datadir}/templates/TextDocument.desktop
%{_libdir}/libkdeinit5_calligrawords.so
%{_datadir}/applications/org.kde.calligrawords.desktop
%{_datadir}/icons/*/*/*/calligrawords.*

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
%{_sysconfdir}/xdg/calligrasheetsrc
%{_bindir}/calligrasheets
%{_datadir}/kservices5/sheets_*_thumbnail.desktop
%{_datadir}/kxmlgui5/calligrasheets
%{_datadir}/calligrasheets
%{_libdir}/qt5/plugins/calligrasheets
%{_datadir}/metainfo/org.kde.calligrasheets.appdata.*
%{_datadir}/config.kcfg/calligrasheets.kcfg
%{_datadir}/templates/.source/SpreadSheet.ods
%{_datadir}/templates/SpreadSheet.desktop
%{_datadir}/kservices5/ServiceMenus/calligra/sheets_print.desktop
%{_datadir}/icons/*/*/*/calligrasheets.*
%{_libdir}/libkdeinit5_calligrasheets.so
%{_datadir}/applications/org.kde.calligrasheets.desktop
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_sheets2xls.so
%doc %lang(ca) %{_docdir}/HTML/ca/sheets
%doc %lang(de) %{_docdir}/HTML/de/sheets
%doc %lang(es) %{_docdir}/HTML/es/sheets
%doc %lang(nl) %{_docdir}/HTML/nl/sheets
%doc %lang(pt) %{_docdir}/HTML/pt/sheets
%doc %lang(pt_BR) %{_docdir}/HTML/pt_BR/sheets
%doc %lang(ru) %{_docdir}/HTML/ru/sheets
%doc %lang(sv) %{_docdir}/HTML/sv/sheets
%doc %lang(uk) %{_docdir}/HTML/uk/sheets
%doc %lang(it) %{_docdir}/HTML/it/sheets

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

%files stage
%{_bindir}/calligrastage
%{_libdir}/libkdeinit5_calligrastage.so
%{_libdir}/qt5/plugins/calligra/formatfilters/calligra_filter_pdf2odg.so
%{_datadir}/applications/org.kde.calligrastage.desktop
%doc %lang(ca) %{_docdir}/HTML/ca/stage
%doc %lang(de) %{_docdir}/HTML/de/stage
%doc %lang(es) %{_docdir}/HTML/es/stage
%doc %lang(fr) %{_docdir}/HTML/fr/stage
%doc %lang(nl) %{_docdir}/HTML/nl/stage
%doc %lang(pt) %{_docdir}/HTML/pt/stage
%doc %lang(pt_BR) %{_docdir}/HTML/pt_BR/stage
%doc %lang(sv) %{_docdir}/HTML/sv/stage
%doc %lang(uk) %{_docdir}/HTML/uk/stage
%doc %lang(it) %{_docdir}/HTML/it/stage
%{_datadir}/kservices5/ServiceMenus/calligra/stage_print.desktop
%{_datadir}/metainfo/org.kde.calligrastage.appdata.xml

%{_sysconfdir}/xdg/calligrastagerc
%{_datadir}/kservices5/stage_*_thumbnail.desktop
%{_datadir}/kxmlgui5/calligrastage
%{_datadir}/calligrastage
%{_libdir}/qt5/plugins/calligrastage
%{_datadir}/templates/.source/Presentation.odp
%{_datadir}/templates/Presentation.desktop

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

%files karbon
%{_sysconfdir}/xdg/karbonrc
%{_bindir}/karbon
%{_libdir}/qt5/plugins/karbon
%{_datadir}/metainfo/org.kde.karbon.appdata.*
%{_datadir}/kservices5/karbon_*_thumbnail.desktop
%{_datadir}/templates/.source/Illustration.odg
%{_datadir}/templates/Illustration.desktop
%{_datadir}/kxmlgui5/karbon
%{_datadir}/karbon
%{_datadir}/kservices5/ServiceMenus/calligra/karbon_print.desktop
%{_libdir}/libkdeinit5_karbon.so
%{_datadir}/applications/org.kde.karbon.desktop

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
%{_datadir}/kservices5/flow_*_thumbnail.desktop

#--------------------------------------------------------------------

%if %{with okular}
%package okular-odp
Summary:	ODP file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular
%rename		okular-odp

%description okular-odp
ODP file renderer for Okular.

%files okular-odp
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_odp_calligra.so
%{_datadir}/applications/okularApplication_odp_calligra.desktop
%{_datadir}/kservices5/okularOdp_calligra.desktop

#--------------------------------------------------------------------

%package okular-odt
Summary:	ODT file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-odt
ODT file renderer for Okular.

%files okular-odt
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_odt_calligra.so
%{_datadir}/applications/okularApplication_odt_calligra.desktop
%{_datadir}/kservices5/okularOdt_calligra.desktop

#--------------------------------------------------------------------

%package okular-doc
Summary:	Doc file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-doc
Doc file renderer for Okular.

%files okular-doc
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_doc_calligra.so
%{_datadir}/applications/okularApplication_doc_calligra.desktop
%{_datadir}/kservices5/okularDoc_calligra.desktop

#--------------------------------------------------------------------

%package okular-docx
Summary:	Docx file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-docx
Docx file renderer for Okular.

%files okular-docx
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_docx_calligra.so
%{_datadir}/applications/okularApplication_docx_calligra.desktop
%{_datadir}/kservices5/okularDocx_calligra.desktop

#--------------------------------------------------------------------

%package okular-powerpoint
Summary:	Powerpoint file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-powerpoint
Powerpoint file renderer for Okular.

%files okular-powerpoint
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_powerpoint_calligra.so
%{_datadir}/applications/okularApplication_powerpoint_calligra.desktop
%{_datadir}/kservices5/okularPowerpoint_calligra.desktop

#--------------------------------------------------------------------

%package okular-pptx
Summary:	PPTX file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-pptx
PPTX file renderer for Okular.

%files okular-pptx
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_pptx_calligra.so
%{_datadir}/applications/okularApplication_pptx_calligra.desktop
%{_datadir}/kservices5/okularPptx_calligra.desktop

#--------------------------------------------------------------------

%package okular-wpd
Summary:	WPD file renderer for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	okular

%description okular-wpd
WPD file renderer for Okular.

%files okular-wpd
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_wpd_calligra.so
%{_datadir}/applications/okularApplication_wpd_calligra.desktop
%{_datadir}/kservices5/okularWpd_calligra.desktop
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
%{_libdir}/lib${lib}.so
EOF
done)}
%{_libdir}/libgemini.so
%{_libdir}/libkowv2.so
%{_libdir}/libRtfReader.so
%{_libdir}/libkoodf2.so

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
#sh initrepo.sh
export CXXFLAGS="%{optflags} -std=gnu++17"
%if %_mobile
%cmake_kde5 -DIHAVEPATCHEDQT:BOOL=TRUE -DCALLIGRA_SHOULD_BUILD_STAGING:BOOL=ON \
	-DPACKAGERS_BUILD=ON -G "Unix Makefiles"
%else
%cmake_kde5 -DIHAVEPATCHEDQT:BOOL=TRUE -DCALLIGRA_SHOULD_BUILD_STAGING:BOOL=ON -DGHNS:BOOL=ON -DINSTALL_XLS_EXPORT_FILTER:BOOL=ON  \
	-DPACKAGERS_BUILD=ON -G "Unix Makefiles"
%endif
%make_build

%if %{compile_apidox}
%make_build apidox
%endif

%install
%make_install -C build

%if %compile_apidox
%make_build install-apidox DESTDIR=%{buildroot}/
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

%find_lang calligra \
KarbonFilterEffects \
KarbonTools \
braindump \
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
calligra_textediting_autocorrect \
calligra_textediting_changecase \
calligra_textediting_spellcheck \
calligra_textediting_thesaurus \
calligra_textinlineobject_variables \
calligrafilters \
calligraplan \
calligraplan_scheduler_rcps \
calligraplan_scheduler_tj \
calligraplanlibs \
calligraplanwork \
calligrasheets \
calligrasheets_calendar \
calligrasheets_solver \
calligrastage \
calligrawords \
desktop_calligra_calligra \
desktop_calligra_kexi \
desktop_calligra_krita \
flow \
json_calligra_calligra \
json_calligra_kexi \
karbon \
kexi \
kexiforms_mapwidgetplugin \
kexiforms_webbrowserwidgetplugin \
keximigrate_mdb \
keximigrate_spreadsheet \
kocolorspaces \
koconverter \
krita \
krossmoduleplan \
krossmodulesheets \
krossmodulewords \
okularGenerator_odp \
okularGenerator_odt \
org.kde.braindump.appdata \
org.kde.calligraflow.appdata \
org.kde.calligraplan.appdata \
org.kde.calligrasheets.appdata \
org.kde.calligrastage.appdata \
org.kde.calligrawords.appdata \
org.kde.karbon.appdata \
org.kde.kexi.appdata \
org.kde.krita.appdata \
calligra.lang --with-html
