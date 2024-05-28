# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'themePickerGui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(345, 228)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 71, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 30, 71, 16))
        self.mainColorDisplayWidget = QWidget(Dialog)
        self.mainColorDisplayWidget.setObjectName(u"mainColorDisplayWidget")
        self.mainColorDisplayWidget.setGeometry(QRect(60, 50, 61, 41))
        self.accentColorDisplayWidget = QWidget(Dialog)
        self.accentColorDisplayWidget.setObjectName(u"accentColorDisplayWidget")
        self.accentColorDisplayWidget.setGeometry(QRect(220, 50, 61, 41))
        self.changeMainColorButton = QPushButton(Dialog)
        self.changeMainColorButton.setObjectName(u"changeMainColorButton")
        self.changeMainColorButton.setGeometry(QRect(50, 100, 81, 24))
        self.changeAccentColorButton = QPushButton(Dialog)
        self.changeAccentColorButton.setObjectName(u"changeAccentColorButton")
        self.changeAccentColorButton.setGeometry(QRect(210, 100, 81, 24))
        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(250, 190, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Main color:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Accent color:", None))
        self.changeMainColorButton.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.changeAccentColorButton.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

