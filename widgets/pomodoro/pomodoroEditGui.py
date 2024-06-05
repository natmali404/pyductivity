# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pomodoroEditGui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(315, 199)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 171, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(47, 90, 161, 16))
        self.label_2.setFont(font)
        self.applyButton = QPushButton(Dialog)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(200, 160, 75, 24))
        self.workTimeEdit = QSpinBox(Dialog)
        self.workTimeEdit.setObjectName(u"workTimeEdit")
        self.workTimeEdit.setGeometry(QRect(210, 48, 42, 22))
        self.restTimeEdit = QSpinBox(Dialog)
        self.restTimeEdit.setObjectName(u"restTimeEdit")
        self.restTimeEdit.setGeometry(QRect(210, 88, 42, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Work time (in minutes):", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Rest time (in minutes):", None))
        self.applyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

