import json
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QListWidgetItem, QDialog, QGraphicsDropShadowEffect, QSizePolicy, QSpacerItem, QBoxLayout
from PySide6.QtCore import Qt, QDate, QTime, QDateTime, Signal, Slot
from PySide6.QtGui import QColor, QIcon
from mainWindow import Ui_MainWindow


#user imports
from widgets.square_widget import SquareWidget
from toolbar.theme_picker.themePicker import ThemePicker
from toolbar.add_widget.addWidget import AddWidget
from data_utils import AppData
from header_utils import set_username
from widgets.widget_utils import initialize_widget
from constants import widget_slots, widget_list



class MainWindow(QMainWindow):
    def __init__(self) -> None:

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assets/app_icon.png'))
        
        self.appData = AppData()
        
        self.user_settings = self.appData.get_settings()
        self.basic_config = self.appData.get_settings()["basic_config"]

        collected_widgets = sorted(self.ui.contentFrame.findChildren(SquareWidget), key=lambda widget: widget.objectName())
        self.appData.initiate_widget_grid(widget_list, collected_widgets)
        
        self.widget_grid = self.appData.widget_grid


        self.initialize_header()
        
        self.update_app_style()
        
        self.initialize_grid()
        
        #connect the elements
        self.ui.colorThemeButton.clicked.connect(self.open_theme_picker_window)
        self.ui.addWidgetButton.clicked.connect(self.open_add_widget_window)
    

        

    #####################################
    ######## INIT/UTIL FUNCTIONS ########
    #####################################
    def initialize_header(self) -> None:
        self.basic_config["username"] = set_username(self.basic_config["username"])
    
    #### UPDATE APP STYLE AND COLORS ####
    def update_app_style(self) -> None:
        self.ui.toolbar.setStyleSheet(f"background-color: {self.basic_config['accent_color']};")
        self.ui.nameLabel.setText(f"Welcome, <b>{self.basic_config['username']}</b>!")
        
        
    def delete_widgets(self) -> None:
        for slot in self.widget_grid:
            layout = self.widget_grid[slot].layout()
            #print(layout)
            #print(self.widget_grid[slot].layout().children())
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    #print("found a child!")
                    child.widget().deleteLater()
                
    def initialize_grid(self) -> None:
        print("initializing grid...")
        self.delete_widgets()
        slot_idx = 0
        print()
        for slot in self.widget_grid: #moze cos z i in range idk
            if self.appData.get_settings()[slot]["initialized"] == "yes":
                #print(f"found a widget in slot {slot}!")
                widget_slots[slot_idx] = True
                #print(self.appData.get_settings()[slot]["type"])
                new_widget = initialize_widget(self.appData.get_settings()[slot]["type"])
                new_widget.setVisible(True)
                self.widget_grid[slot].layout().addWidget(new_widget)
                self.ui.contentFrame.update()
                # print(f"Layout contents for slot {slot}:")
                # layout = self.widget_grid[slot].layout()
                # for i in range(layout.count()):
                #     item = layout.itemAt(i)
                #     if item.widget():
                #         print(f"- Widget {i}: {item.widget()}")
                #         print(f"{item.geometry()}")
                
                #shadow

                new_widget.setStyleSheet(new_widget.styleSheet() + "border-radius: 20px;")
                shadow = QGraphicsDropShadowEffect(new_widget)
                shadow.setBlurRadius(10)
                shadow.setXOffset(3)
                shadow.setYOffset(3)
                shadow.setColor("#636363")
                new_widget.setGraphicsEffect(shadow)
                new_widget.update()
                # self.widget_grid[slot].update()
                # self.widget_grid[slot].layout().update()
                #print("updated")
            slot_idx += 1
        #self.ui.contentFrame.update()
        for slot in self.widget_grid:
            if self.widget_grid[slot].layout().itemAt(0):
                print(f"{self.widget_grid[slot]} => {self.widget_grid[slot].layout().itemAt(0).widget()}")
            
    
        

    #### EVENTS OVERRIDDEN ####
    def closeEvent(self, event) -> None:
        self.appData.update_settings(self.user_settings)
        self.appData.save_settings()
        event.accept()
        

        
    #####################################
    ########## TOOLBAR BUTTONS ##########
    #####################################
    
    #### COLOR THEME BUTTON ####


    
    def open_theme_picker_window(self) -> None:
        self.new_window = ThemePicker(self.basic_config["main_color"], self.basic_config["accent_color"])
        self.new_window.colors_changed.connect(self.on_colors_changed)
        self.new_window.exec()
        self.update_app_style()
        
    def on_colors_changed(self, new_main_color: str, new_accent_color: str) -> None:
        self.basic_config["main_color"] = new_main_color
        self.basic_config["accent_color"] = new_accent_color
        self.appData.update_settings(self.user_settings)
        
    def open_add_widget_window(self) -> None:
        self.new_window = AddWidget(self.appData)
        self.new_window.widget_added.connect(self.on_widget_added)
        self.new_window.exec()
        self.initialize_grid()
        self.ui.contentFrame.update()
        for widget in self.widget_grid:
            self.widget_grid[widget].update()
        
    def on_widget_added(self, settings: dict) -> None:
        print("signal caught!!")
        self.appData.update_settings(settings)
        self.appData.update_widget_grid(self.widget_grid)
        



    


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    
    window = MainWindow()
    window.setWindowTitle("pyDuctivity")
    window.show()

    sys.exit(app.exec())