# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teamPlayerLQdLVP.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import new_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 583)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"padding:2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(500, 500))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ToolBar = QFrame(self.centralwidget)
        self.ToolBar.setObjectName(u"ToolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToolBar.sizePolicy().hasHeightForWidth())
        self.ToolBar.setSizePolicy(sizePolicy1)
        self.ToolBar.setAutoFillBackground(False)
        self.ToolBar.setStyleSheet(u"background-color: #0db7ed;")
        self.ToolBar.setFrameShape(QFrame.StyledPanel)
        self.ToolBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Logo = QFrame(self.ToolBar)
        self.Logo.setObjectName(u"Logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy2)
        self.Logo.setMaximumSize(QSize(50, 70))
        self.Logo.setSizeIncrement(QSize(0, 0))
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 6, 0, -1)
        self.logo_img = QLabel(self.Logo)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMinimumSize(QSize(0, 0))
        self.logo_img.setMaximumSize(QSize(100, 70))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.logo_img.setFont(font1)
        self.logo_img.setStyleSheet(u"color:white;\n"
"margin-left:9px")
        self.logo_img.setPixmap(QPixmap(u"icons/assets/stats-free-icon-font (1).png"))
        self.logo_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.logo_img)


        self.horizontalLayout.addWidget(self.Logo)

        self.Icons = QFrame(self.ToolBar)
        self.Icons.setObjectName(u"Icons")
        sizePolicy1.setHeightForWidth(self.Icons.sizePolicy().hasHeightForWidth())
        self.Icons.setSizePolicy(sizePolicy1)
        self.Icons.setFrameShape(QFrame.StyledPanel)
        self.Icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Icons)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_icon = QFrame(self.Icons)
        self.sidebar_icon.setObjectName(u"sidebar_icon")
        self.sidebar_icon.setMaximumSize(QSize(190, 50))
        self.sidebar_icon.setCursor(QCursor(Qt.ArrowCursor))
        self.sidebar_icon.setStyleSheet(u"")
        self.sidebar_icon.setFrameShape(QFrame.StyledPanel)
        self.sidebar_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_icon)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo_name = QLabel(self.sidebar_icon)
        self.logo_name.setObjectName(u"logo_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logo_name.sizePolicy().hasHeightForWidth())
        self.logo_name.setSizePolicy(sizePolicy3)
        self.logo_name.setMinimumSize(QSize(0, 0))
        self.logo_name.setMaximumSize(QSize(90, 16777215))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        self.logo_name.setFont(font2)
        self.logo_name.setStyleSheet(u"color:white;\n"
"")

        self.horizontalLayout_4.addWidget(self.logo_name)

        self.open_close_side_bar = QPushButton(self.sidebar_icon)
        self.open_close_side_bar.setObjectName(u"open_close_side_bar")
        self.open_close_side_bar.setMaximumSize(QSize(100, 16777215))
        self.open_close_side_bar.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_close_side_bar.setStyleSheet(u"margin-left:19px")
        icon = QIcon()
        icon.addFile(u"icons/assets/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar.setIcon(icon)
        self.open_close_side_bar.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar)


        self.horizontalLayout_2.addWidget(self.sidebar_icon)

        self.control_icons = QFrame(self.Icons)
        self.control_icons.setObjectName(u"control_icons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.control_icons.sizePolicy().hasHeightForWidth())
        self.control_icons.setSizePolicy(sizePolicy4)
        self.control_icons.setMaximumSize(QSize(150, 50))
        self.control_icons.setFrameShape(QFrame.StyledPanel)
        self.control_icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.control_icons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.minimize = QPushButton(self.control_icons)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/assets/minus-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimize, 0, Qt.AlignRight|Qt.AlignTop)

        self.expand = QPushButton(self.control_icons)
        self.expand.setObjectName(u"expand")
        self.expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand.setStyleSheet(u"margin-right:15px;\n"
"margin-left:15px;")
        icon2 = QIcon()
        icon2.addFile(u"icons/assets/expand-arrows-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand.setIcon(icon2)
        self.expand.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.expand, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.out = QPushButton(self.control_icons)
        self.out.setObjectName(u"out")
        self.out.setCursor(QCursor(Qt.PointingHandCursor))
        self.out.setStyleSheet(u"margin-right: 5px")
        icon3 = QIcon()
        icon3.addFile(u"icons/assets/cross-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.out.setIcon(icon3)
        self.out.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.out, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.control_icons, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.Icons)


        self.verticalLayout.addWidget(self.ToolBar)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setMinimumSize(QSize(500, 0))
        self.Body.setStyleSheet(u"background-color:#F0F1F3;\n"
"padding:0px;")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Body)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_body = QFrame(self.frame)
        self.left_body.setObjectName(u"left_body")
        sizePolicy4.setHeightForWidth(self.left_body.sizePolicy().hasHeightForWidth())
        self.left_body.setSizePolicy(sizePolicy4)
        self.left_body.setMinimumSize(QSize(0, 0))
        self.left_body.setMaximumSize(QSize(210, 16777215))
        self.left_body.setStyleSheet(u"background-color:#384d54;")
        self.left_body.setFrameShape(QFrame.StyledPanel)
        self.left_body.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.left_body)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.choices = QFrame(self.left_body)
        self.choices.setObjectName(u"choices")
        self.choices.setMinimumSize(QSize(0, 0))
        self.choices.setFrameShape(QFrame.StyledPanel)
        self.choices.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.choices)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 22, 0, 0)
        self.home_button = QPushButton(self.choices)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(220, 70))
        self.home_button.setMaximumSize(QSize(220, 70))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.home_button.setFont(font3)
        self.home_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-right:75px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/assets/home-free-icon-font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon4)
        self.home_button.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.home_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.upload_button = QPushButton(self.choices)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setMinimumSize(QSize(220, 70))
        self.upload_button.setMaximumSize(QSize(220, 70))
        font4 = QFont()
        font4.setPointSize(13)
        self.upload_button.setFont(font4)
        self.upload_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-left: 5px;\n"
"padding-right:19px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/assets/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upload_button.setIcon(icon5)
        self.upload_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.upload_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.search_button = QPushButton(self.choices)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(220, 70))
        self.search_button.setMaximumSize(QSize(220, 70))
        self.search_button.setFont(font4)
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-left: 0px;\n"
"padding-right:13px;\n"
"margin-right:70px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/assets/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon6)
        self.search_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.search_button, 0, Qt.AlignLeft)


        self.vboxLayout.addWidget(self.choices, 0, Qt.AlignTop)

        self.out_2 = QFrame(self.left_body)
        self.out_2.setObjectName(u"out_2")
        self.out_2.setMinimumSize(QSize(0, 70))
        self.out_2.setMaximumSize(QSize(16777215, 70))
        self.out_2.setFrameShape(QFrame.StyledPanel)
        self.out_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.out_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.out_2)
        self.exit_button.setObjectName(u"exit_button")
        font5 = QFont()
        font5.setPointSize(15)
        self.exit_button.setFont(font5)
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-left: 15px;\n"
"padding-right:13px;\n"
"margin-right:5px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/assets/sign-out-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon7)
        self.exit_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.exit_button)


        self.vboxLayout.addWidget(self.out_2)


        self.horizontalLayout_6.addWidget(self.left_body)

        self.right_body = QFrame(self.frame)
        self.right_body.setObjectName(u"right_body")
        self.right_body.setFrameShape(QFrame.StyledPanel)
        self.right_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.right_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font6 = QFont()
        font6.setBold(False)
        font6.setKerning(False)
        self.stackedWidget.setFont(font6)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_5 = QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 120, -1, -1)
        self.label_2 = QLabel(self.home_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(270, 270))
        self.label_2.setMaximumSize(QSize(270, 270))
        font7 = QFont()
        font7.setPointSize(20)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"margin-top:10px;\n"
"border:7px solid #0db7ed;\n"
"border-radius:100px;\n"
"padding: 30px;")
        self.label_2.setPixmap(QPixmap(u"icons/assets/analysis.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setMinimumSize(QSize(182, 0))
        font8 = QFont()
        font8.setPointSize(35)
        font8.setBold(True)
        self.label.setFont(font8)
        self.label.setStyleSheet(u"color:#384d54;\n"
"")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.home_page)
        self.search_page = QWidget()
        self.search_page.setObjectName(u"search_page")
        self.verticalLayout_6 = QVBoxLayout(self.search_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.time_nav = QFrame(self.search_page)
        self.time_nav.setObjectName(u"time_nav")
        self.time_nav.setMaximumSize(QSize(16777215, 60))
        self.time_nav.setFrameShape(QFrame.StyledPanel)
        self.time_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.time_nav)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.time_nav_1 = QFrame(self.time_nav)
        self.time_nav_1.setObjectName(u"time_nav_1")
        self.time_nav_1.setMinimumSize(QSize(0, 50))
        self.time_nav_1.setMaximumSize(QSize(16777215, 50))
        self.time_nav_1.setStyleSheet(u"QFrame{\n"
"border:2px solid #384d54;\n"
"border-radius:15px;\n"
"background-color:#0db7ed;\n"
"\n"
"}\n"
"")
        self.time_nav_1.setFrameShape(QFrame.StyledPanel)
        self.time_nav_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.time_nav_1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_2 = QLineEdit(self.time_nav_1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"border-radius:9px;\n"
"")

        self.horizontalLayout_11.addWidget(self.lineEdit_2, 0, Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.time_nav_1)


        self.verticalLayout_6.addWidget(self.time_nav)

        self.time_graph = QFrame(self.search_page)
        self.time_graph.setObjectName(u"time_graph")
        self.time_graph.setFrameShape(QFrame.StyledPanel)
        self.time_graph.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.time_graph)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.time_nav_2 = QFrame(self.time_graph)
        self.time_nav_2.setObjectName(u"time_nav_2")
        self.time_nav_2.setMinimumSize(QSize(0, 50))
        self.time_nav_2.setMaximumSize(QSize(16777215, 50))
        self.time_nav_2.setStyleSheet(u"QFrame{\n"
"border:2px solid #384d54;\n"
"border-radius:15px;\n"
"background-color:#0db7ed \n"
"}\n"
"")
        self.time_nav_2.setFrameShape(QFrame.StyledPanel)
        self.time_nav_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.time_nav_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_3 = QLineEdit(self.time_nav_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"border-radius:9px;\n"
"")

        self.horizontalLayout_16.addWidget(self.lineEdit_3, 0, Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.time_nav_2)


        self.verticalLayout_6.addWidget(self.time_graph, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.search_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(500, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.show_nba = QLineEdit(self.frame_3)
        self.show_nba.setObjectName(u"show_nba")
        self.show_nba.setEnabled(False)
        self.show_nba.setMinimumSize(QSize(0, 468))
        self.show_nba.setStyleSheet(u"margin-bottom:450px;\n"
"color: black;\n"
"font-size: 17px;\n"
"padding-left:10px\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.show_nba)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.time_download = QFrame(self.search_page)
        self.time_download.setObjectName(u"time_download")
        self.time_download.setMaximumSize(QSize(16777215, 80))
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(True)
        self.time_download.setFont(font9)
        self.time_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.time_download.setFrameShape(QFrame.StyledPanel)
        self.time_download.setFrameShadow(QFrame.Raised)
        self.time_download.setLineWidth(3)
        self.horizontalLayout_8 = QHBoxLayout(self.time_download)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.time_download)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
        self.pushButton.setMaximumSize(QSize(210, 16777215))
        font10 = QFont()
        font10.setBold(True)
        self.pushButton.setFont(font10)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius: 7px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"  padding: 17px;\n"
"  font-size:22px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}\n"
"")
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_6.addWidget(self.time_download)

        self.stackedWidget.addWidget(self.search_page)
        self.uplad_page = QWidget()
        self.uplad_page.setObjectName(u"uplad_page")
        self.verticalLayout_7 = QVBoxLayout(self.uplad_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.uplad_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QSize(300, 40))
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"border: 2px solid #000;\n"
"border-radius:9px;\n"
"background-color:#384d54;\n"
"color: #f3f4f7")

        self.verticalLayout_10.addWidget(self.lineEdit)


        self.verticalLayout_7.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.freq_graph = QFrame(self.uplad_page)
        self.freq_graph.setObjectName(u"freq_graph")
        self.freq_graph.setFrameShape(QFrame.StyledPanel)
        self.freq_graph.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.freq_graph)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.browse_button = QPushButton(self.freq_graph)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.browse_button.sizePolicy().hasHeightForWidth())
        self.browse_button.setSizePolicy(sizePolicy5)
        self.browse_button.setMinimumSize(QSize(220, 0))
        self.browse_button.setMaximumSize(QSize(220, 16777215))
        self.browse_button.setFont(font10)
        self.browse_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_button.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius: 7px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"  padding: 17px;\n"
"  font-size:20px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}\n"
"")
        self.browse_button.setIcon(icon5)
        self.browse_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.browse_button)


        self.verticalLayout_7.addWidget(self.freq_graph, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.uplad_page)
        self.compare_page = QWidget()
        self.compare_page.setObjectName(u"compare_page")
        self.verticalLayout_8 = QVBoxLayout(self.compare_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget.addWidget(self.compare_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.right_body)


        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_img.setText("")
        self.logo_name.setText(QCoreApplication.translate("MainWindow", u"NBA", None))
        self.open_close_side_bar.setText("")
        self.minimize.setText("")
        self.expand.setText("")
        self.out.setText("")
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u" Upload Dataset", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u" Exit", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"   NBA ", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.show_nba.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Search", None))
        self.lineEdit.setText("")
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
    # retranslateUi

