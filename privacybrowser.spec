Name:		privacybrowser
Version:	0.8
Release:	1
Source0:	https://download.stoutner.com/privacybrowser-pc/privacybrowser-%{version}.tar.xz
Summary:	A privary respecting browser
URL:		https://www.stoutner.com/privacy-browser-pc/
License:	GPL-3.0+
Group:		Applications/Internet
BuildRequires:	cmake
BuildSystem:	cmake
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	atomic-devel
BuildRequires:	cmake(Qt6QmlMeta)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6BreezeIcons)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6QmlWorkerScript)

%description
Privacy Browser is an open source web browser focused on user privacy
based on Qt WebEgnine. It is released under the GPLv3+ license.

Privacy Browser has two primary goals.

1. Minimize the data that is sent to the internet.
2. Minimize the data that is stored on the device.

Most browsers silently give websites massive amounts of information that allows
them to track you and compromise your privacy. Websites and ad networks use
technologies like JavaScript, cookies, DOM storage, user agents, and many other
things to uniquely identify each user and track them between visits and across
the web.

In contrast, privacy sensitive features are disabled by default in Privacy
Browser. If one of these technologies is required for a website to function
correctly, the user may choose to turn it on for just that visit. Or, they can
use domain settings to automatically turn on certain features when entering a
specific website and turn them off again when leaving.

%prep
%autosetup -p1

%files -f %{name}.lang
%{_bindir}/privacybrowser
%{_datadir}/applications/com.stoutner.privacybrowser.desktop
%{_datadir}/icons/hicolor/*/apps/privacybrowser*
%{_datadir}/knotifications6/privacybrowser.notifyrc
%{_datadir}/kxmlgui5/privacybrowser
%{_datadir}/metainfo/com.stoutner.privacybrowser.metainfo.xml
