# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reorderWidgetsGui.ui'
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
        Dialog.resize(365, 300)
        self.widgetsComboBox = QComboBox(Dialog)
        self.widgetsComboBox.setObjectName(u"widgetsComboBox")
        self.widgetsComboBox.setGeometry(QRect(150, 30, 161, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 91, 16))
        self.currentWidgetPositionFrame = QFrame(Dialog)
        self.currentWidgetPositionFrame.setObjectName(u"currentWidgetPositionFrame")
        self.currentWidgetPositionFrame.setGeometry(QRect(130, 100, 90, 52))
        self.currentWidgetPositionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.currentWidgetPositionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.currentWidgetPositionFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 0, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout.addWidget(self.radioButton_4, 0, 2, 1, 1)

        self.radioButton_8 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout.addWidget(self.radioButton_8, 0, 3, 1, 1)

        self.radioButton_5 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout.addWidget(self.radioButton_5, 1, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout.addWidget(self.radioButton_6, 1, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 2, 1, 1)

        self.radioButton_7 = QRadioButton(self.currentWidgetPositionFrame)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout.addWidget(self.radioButton_7, 1, 3, 1, 1)

        self.newWidgetPositionFrame = QFrame(Dialog)
        self.newWidgetPositionFrame.setObjectName(u"newWidgetPositionFrame")
        self.newWidgetPositionFrame.setGeometry(QRect(130, 180, 90, 52))
        self.newWidgetPositionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.newWidgetPositionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.newWidgetPositionFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_9 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_2.addWidget(self.radioButton_9, 0, 0, 1, 1)

        self.radioButton_10 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout_2.addWidget(self.radioButton_10, 0, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout_2.addWidget(self.radioButton_11, 0, 2, 1, 1)

        self.radioButton_12 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout_2.addWidget(self.radioButton_12, 0, 3, 1, 1)

        self.radioButton_13 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout_2.addWidget(self.radioButton_13, 1, 0, 1, 1)

        self.radioButton_14 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.gridLayout_2.addWidget(self.radioButton_14, 1, 1, 1, 1)

        self.radioButton_15 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout_2.addWidget(self.radioButton_15, 1, 2, 1, 1)

        self.radioButton_16 = QRadioButton(self.newWidgetPositionFrame)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout_2.addWidget(self.radioButton_16, 1, 3, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 80, 131, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 160, 111, 16))
        self.applyButton = QPushButton(Dialog)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(270, 260, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Selected widget:", None))
        self.radioButton.setText("")
        self.radioButton_3.setText("")
        self.radioButton_4.setText("")
        self.radioButton_8.setText("")
        self.radioButton_5.setText("")
        self.radioButton_6.setText("")
        self.radioButton_2.setText("")
        self.radioButton_7.setText("")
        self.radioButton_9.setText("")
        self.radioButton_10.setText("")
        self.radioButton_11.setText("")
        self.radioButton_12.setText("")
        self.radioButton_13.setText("")
        self.radioButton_14.setText("")
        self.radioButton_15.setText("")
        self.radioButton_16.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Current widget position:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"New widget position:", None))
        self.applyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

