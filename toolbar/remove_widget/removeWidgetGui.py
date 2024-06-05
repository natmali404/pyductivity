# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removeWidgetGui.ui'
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
        Dialog.resize(400, 248)
        self.widgetComboBox = QComboBox(Dialog)
        self.widgetComboBox.setObjectName(u"widgetComboBox")
        self.widgetComboBox.setGeometry(QRect(190, 30, 141, 21))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 101, 16))
        self.widgetPositionframe = QFrame(Dialog)
        self.widgetPositionframe.setObjectName(u"widgetPositionframe")
        self.widgetPositionframe.setGeometry(QRect(150, 110, 90, 52))
        self.widgetPositionframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.widgetPositionframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.widgetPositionframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton = QRadioButton(self.widgetPositionframe)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.widgetPositionframe)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.widgetPositionframe)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 0, 2, 1, 1)

        self.radioButton_4 = QRadioButton(self.widgetPositionframe)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout.addWidget(self.radioButton_4, 0, 3, 1, 1)

        self.radioButton_5 = QRadioButton(self.widgetPositionframe)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout.addWidget(self.radioButton_5, 1, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.widgetPositionframe)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout.addWidget(self.radioButton_6, 1, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.widgetPositionframe)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout.addWidget(self.radioButton_7, 1, 2, 1, 1)

        self.radioButton_8 = QRadioButton(self.widgetPositionframe)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout.addWidget(self.radioButton_8, 1, 3, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 90, 101, 16))
        self.applyButton = QPushButton(Dialog)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(300, 200, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Widget to remove:", None))
        self.radioButton.setText("")
        self.radioButton_2.setText("")
        self.radioButton_3.setText("")
        self.radioButton_4.setText("")
        self.radioButton_5.setText("")
        self.radioButton_6.setText("")
        self.radioButton_7.setText("")
        self.radioButton_8.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Widget's position:", None))
        self.applyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

