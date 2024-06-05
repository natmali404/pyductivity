# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from header_utils import ClockLabel
from widgets.square_widget import SquareWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1050, 750))
        MainWindow.setMaximumSize(QSize(1050, 750))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        self.mainbody.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.mainbody)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy1)
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameLabel = QLabel(self.headerFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        font.setPointSize(14)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.nameLabel)

        self.clockLabel = ClockLabel(self.headerFrame)
        self.clockLabel.setObjectName(u"clockLabel")
        font1 = QFont()
        font1.setPointSize(60)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.clockLabel.setFont(font1)
        self.clockLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.clockLabel)


        self.verticalLayout.addWidget(self.headerFrame)

        self.containerFrame = QFrame(self.mainbody)
        self.containerFrame.setObjectName(u"containerFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.containerFrame.sizePolicy().hasHeightForWidth())
        self.containerFrame.setSizePolicy(sizePolicy2)
        self.containerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.containerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.containerFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contentFrame = QFrame(self.containerFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy3)
        self.contentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.contentFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_7 = SquareWidget(self.contentFrame)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_7, 1, 2, 1, 1)

        self.widget_8 = SquareWidget(self.contentFrame)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_8, 1, 3, 1, 1)

        self.widget_1 = SquareWidget(self.contentFrame)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_1, 0, 0, 1, 1)

        self.widget_5 = SquareWidget(self.contentFrame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_5, 1, 0, 1, 1)

        self.widget_4 = SquareWidget(self.contentFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_4, 0, 3, 1, 1)

        self.widget_2 = SquareWidget(self.contentFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = SquareWidget(self.contentFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget_6 = SquareWidget(self.contentFrame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_6, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.contentFrame)


        self.verticalLayout.addWidget(self.containerFrame)

        self.footerFrame = QFrame(self.mainbody)
        self.footerFrame.setObjectName(u"footerFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy4)
        self.footerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.footerFrame)


        self.horizontalLayout.addWidget(self.mainbody)

        self.toolbar = QWidget(self.centralwidget)
        self.toolbar.setObjectName(u"toolbar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy5)
        self.toolbar.setMinimumSize(QSize(50, 0))
        self.toolbar.setStyleSheet(u"")
        self.colorThemeButton = QPushButton(self.toolbar)
        self.colorThemeButton.setObjectName(u"colorThemeButton")
        self.colorThemeButton.setGeometry(QRect(10, 10, 31, 31))
        icon = QIcon()
        icon.addFile(u"assets/color_palette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorThemeButton.setIcon(icon)
        self.colorThemeButton.setIconSize(QSize(20, 20))
        self.addWidgetButton = QPushButton(self.toolbar)
        self.addWidgetButton.setObjectName(u"addWidgetButton")
        self.addWidgetButton.setGeometry(QRect(10, 50, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"assets/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addWidgetButton.setIcon(icon1)
        self.addWidgetButton.setIconSize(QSize(20, 20))
        self.reorderWidgetsButton = QPushButton(self.toolbar)
        self.reorderWidgetsButton.setObjectName(u"reorderWidgetsButton")
        self.reorderWidgetsButton.setGeometry(QRect(10, 90, 31, 31))
        icon2 = QIcon()
        icon2.addFile(u"assets/reorder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reorderWidgetsButton.setIcon(icon2)
        self.reorderWidgetsButton.setIconSize(QSize(26, 26))
        self.removeWidgetButton = QPushButton(self.toolbar)
        self.removeWidgetButton.setObjectName(u"removeWidgetButton")
        self.removeWidgetButton.setGeometry(QRect(10, 130, 31, 31))
        icon3 = QIcon()
        icon3.addFile(u"assets/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeWidgetButton.setIcon(icon3)
        self.removeWidgetButton.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.toolbar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.clockLabel.setText("")
        self.colorThemeButton.setText("")
        self.addWidgetButton.setText("")
        self.reorderWidgetsButton.setText("")
        self.removeWidgetButton.setText("")
    # retranslateUi

