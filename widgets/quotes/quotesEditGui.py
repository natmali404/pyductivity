# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quotesEditGui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPlainTextEdit, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(290, 442)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 221, 21))
        self.quotesListEdit = QPlainTextEdit(Dialog)
        self.quotesListEdit.setObjectName(u"quotesListEdit")
        self.quotesListEdit.setGeometry(QRect(10, 70, 271, 361))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 141, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 201, 16))
        self.autorefreshCheckBox = QCheckBox(Dialog)
        self.autorefreshCheckBox.setObjectName(u"autorefreshCheckBox")
        self.autorefreshCheckBox.setGeometry(QRect(130, 10, 76, 20))
        self.autorefreshIntervalSpinBox = QSpinBox(Dialog)
        self.autorefreshIntervalSpinBox.setObjectName(u"autorefreshIntervalSpinBox")
        self.autorefreshIntervalSpinBox.setGeometry(QRect(230, 30, 42, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"(List quotes from newline)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Quotes autorefresh:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Quotes autorefresh interval (in mins):)", None))
        self.autorefreshCheckBox.setText("")
    # retranslateUi

