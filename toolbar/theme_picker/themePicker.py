from PySide6.QtWidgets import QDialog, QColorDialog
from PySide6.QtCore import Signal
from .themePickerGui import Ui_Dialog

class ThemePicker(QDialog):
    def __init__(self, main_color, accent_color):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main_color = main_color
        self.accent_color = accent_color
        
        self.ui.mainColorDisplayWidget.setStyleSheet(f"background-color: {self.main_color};")
        self.ui.accentColorDisplayWidget.setStyleSheet(f"background-color: {self.accent_color};")
        
        self.ui.changeMainColorButton.clicked.connect(self.open_main_color_picker)
        self.ui.changeAccentColorButton.clicked.connect(self.open_accent_color_picker)
        self.ui.saveButton.clicked.connect(self.save_colors)
        self.ui.saveButton.clicked.connect(self.close)

    colors_changed = Signal(str, str)
    
    def open_main_color_picker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.main_color = color.name()
            self.ui.mainColorDisplayWidget.setStyleSheet(f"background-color: {self.main_color};")


    def open_accent_color_picker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.accent_color = color.name()
            self.ui.accentColorDisplayWidget.setStyleSheet(f"background-color: {self.accent_color};")

        
    def save_colors(self):
        self.colors_changed.emit(self.main_color, self.accent_color)

        
