# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notesGui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(205, 208)
        Form.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.widgetTitleLabel = QLabel(Form)
        self.widgetTitleLabel.setObjectName(u"widgetTitleLabel")
        self.widgetTitleLabel.setGeometry(QRect(10, 10, 181, 20))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(12)
        font.setBold(True)
        self.widgetTitleLabel.setFont(font)
        self.widgetTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleEdit = QLineEdit(Form)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(30, 35, 141, 22))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(2, 60, 201, 121))
        self.showFullNoteButton = QPushButton(Form)
        self.showFullNoteButton.setObjectName(u"showFullNoteButton")
        self.showFullNoteButton.setGeometry(QRect(50, 182, 101, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.widgetTitleLabel.setText(QCoreApplication.translate("Form", u"notes()", None))
        self.showFullNoteButton.setText(QCoreApplication.translate("Form", u"Show full note...", None))
    # retranslateUi

