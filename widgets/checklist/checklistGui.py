# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checklistGui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setStyleSheet(u"background-color: rgb(246, 234, 255);")
        self.widgetTitleLabel = QLabel(Form)
        self.widgetTitleLabel.setObjectName(u"widgetTitleLabel")
        self.widgetTitleLabel.setGeometry(QRect(10, 10, 181, 20))
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
        self.removeButtonFrame = QFrame(Form)
        self.removeButtonFrame.setObjectName(u"removeButtonFrame")
        self.removeButtonFrame.setGeometry(QRect(170, 30, 31, 161))
        self.removeButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.removeButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(160, 30, 20, 161))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.contentFrame = QFrame(Form)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setGeometry(QRect(10, 30, 151, 161))
        self.contentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.widgetTitleLabel.setText(QCoreApplication.translate("Form", u"checklist()", None))
    # retranslateUi

