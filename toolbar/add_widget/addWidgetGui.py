# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addWidgetGui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 256)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widgetTypeList = QComboBox(Dialog)
        self.widgetTypeList.setObjectName(u"widgetTypeList")
        self.widgetTypeList.setGeometry(QRect(160, 40, 121, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 40, 81, 16))
        self.widgetPlacementFrame = QFrame(Dialog)
        self.widgetPlacementFrame.setObjectName(u"widgetPlacementFrame")
        self.widgetPlacementFrame.setGeometry(QRect(180, 100, 90, 52))
        self.widgetPlacementFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.widgetPlacementFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.widgetPlacementFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widgetRadioButton_1 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_1.setObjectName(u"widgetRadioButton_1")

        self.gridLayout.addWidget(self.widgetRadioButton_1, 0, 0, 1, 1)

        self.widgetRadioButton_2 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_2.setObjectName(u"widgetRadioButton_2")

        self.gridLayout.addWidget(self.widgetRadioButton_2, 0, 1, 1, 1)

        self.widgetRadioButton_3 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_3.setObjectName(u"widgetRadioButton_3")

        self.gridLayout.addWidget(self.widgetRadioButton_3, 0, 2, 1, 1)

        self.widgetRadioButton_4 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_4.setObjectName(u"widgetRadioButton_4")

        self.gridLayout.addWidget(self.widgetRadioButton_4, 0, 3, 1, 1)

        self.widgetRadioButton_5 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_5.setObjectName(u"widgetRadioButton_5")

        self.gridLayout.addWidget(self.widgetRadioButton_5, 1, 0, 1, 1)

        self.widgetRadioButton_7 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_7.setObjectName(u"widgetRadioButton_7")

        self.gridLayout.addWidget(self.widgetRadioButton_7, 1, 1, 1, 1)

        self.widgetRadioButton_6 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_6.setObjectName(u"widgetRadioButton_6")

        self.gridLayout.addWidget(self.widgetRadioButton_6, 1, 2, 1, 1)

        self.widgetRadioButton_8 = QRadioButton(self.widgetPlacementFrame)
        self.widgetRadioButton_8.setObjectName(u"widgetRadioButton_8")

        self.gridLayout.addWidget(self.widgetRadioButton_8, 1, 3, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 101, 16))
        self.addWidgetButton = QPushButton(Dialog)
        self.addWidgetButton.setObjectName(u"addWidgetButton")
        self.addWidgetButton.setGeometry(QRect(300, 210, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Widget type", None))
        self.widgetRadioButton_1.setText("")
        self.widgetRadioButton_2.setText("")
        self.widgetRadioButton_3.setText("")
        self.widgetRadioButton_4.setText("")
        self.widgetRadioButton_5.setText("")
        self.widgetRadioButton_7.setText("")
        self.widgetRadioButton_6.setText("")
        self.widgetRadioButton_8.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Widget placement", None))
        self.addWidgetButton.setText(QCoreApplication.translate("Dialog", u"Add Widget", None))
    # retranslateUi

