# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'websiteBlockerGui.ui'
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
        Form.resize(197, 208)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setStyleSheet(u"background-color: rgb(246, 234, 255);")
        self.widgetTitleLabel = QLabel(Form)
        self.widgetTitleLabel.setObjectName(u"widgetTitleLabel")
        self.widgetTitleLabel.setGeometry(QRect(12, 10, 181, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widgetTitleLabel.sizePolicy().hasHeightForWidth())
        self.widgetTitleLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(11)
        font.setBold(True)
        self.widgetTitleLabel.setFont(font)
        self.widgetTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(55, 60, 61, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.statusLabel = QLabel(Form)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(118, 60, 49, 16))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.statusLabel.setFont(font2)
        self.blockButton = QPushButton(Form)
        self.blockButton.setObjectName(u"blockButton")
        self.blockButton.setGeometry(QRect(43, 90, 121, 51))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(16)
        self.blockButton.setFont(font3)
        icon = QIcon()
        icon.addFile(u"../../assets/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.blockButton.setIcon(icon)
        self.blockButton.setIconSize(QSize(32, 32))
        self.editButton = QPushButton(Form)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(55, 180, 91, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.widgetTitleLabel.setText(QCoreApplication.translate("Form", u"website_blocker()", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Blocker:", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"OFF", None))
        self.blockButton.setText(QCoreApplication.translate("Form", u"BLOCK", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit websites...", None))
    # retranslateUi

