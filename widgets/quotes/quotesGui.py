# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quotesGui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

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
        self.moreButton = QPushButton(Form)
        self.moreButton.setObjectName(u"moreButton")
        self.moreButton.setGeometry(QRect(70, 180, 71, 24))
        self.quoteLabel = QLabel(Form)
        self.quoteLabel.setObjectName(u"quoteLabel")
        self.quoteLabel.setGeometry(QRect(20, 40, 161, 131))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(True)
        self.quoteLabel.setFont(font1)
        self.quoteLabel.setWordWrap(True)
        self.refreshButton = QPushButton(Form)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(25, 175, 24, 24))
        icon = QIcon()
        icon.addFile(u"../../assets/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.widgetTitleLabel.setText(QCoreApplication.translate("Form", u"quotes()", None))
        self.moreButton.setText(QCoreApplication.translate("Form", u"More...", None))
        self.quoteLabel.setText(QCoreApplication.translate("Form", u"\"It takes courage to grow up and become who you really are.\" ", None))
        self.refreshButton.setText("")
    # retranslateUi

