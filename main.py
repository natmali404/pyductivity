import ctypes
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from mainWindow import Ui_MainWindow


from widgets.square_widget import SquareWidget
from toolbar.theme_picker.themePicker import ThemePicker
from toolbar.add_widget.addWidget import AddWidget
from toolbar.reorder_widgets.reorderWidgets import ReorderWidgets
from toolbar.remove_widget.removeWidget import RemoveWidget
from data_utils import AppData
from header_utils import set_username, update_app_style
from widgets.widget_utils import initialize_widget, set_style
from constants import widget_list


#admin priviledges, required for the website blocker to run

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin() -> None:
    if sys.platform == 'win32':
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


class MainWindow(QMainWindow):
    def __init__(self) -> None:

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assets/app_icon.png'))
        
        #data initialization
        self.appData = AppData()
    
        self.user_settings = self.appData.user_settings
        self.widget_settings = self.appData.widget_settings

        collected_widgets = sorted(self.ui.contentFrame.findChildren(SquareWidget), key=lambda widget: widget.objectName())
        self.appData.initiate_widget_grid(widget_list, collected_widgets)

        self.widget_grid = self.appData.widget_grid

        #app initialization
        self.initialize_header()
        self.initialize_grid()
        update_app_style(self.ui, self.user_settings)
        
        #connect the ui elements
        self.ui.colorThemeButton.clicked.connect(self.open_theme_picker_window)
        self.ui.addWidgetButton.clicked.connect(self.open_add_widget_window)
        self.ui.reorderWidgetsButton.clicked.connect(self.open_reorder_widgets_window)
        self.ui.removeWidgetButton.clicked.connect(self.open_remove_widgets_window)
        


    #####################################
    ######## INIT/UTIL FUNCTIONS ########
    #####################################
    def initialize_header(self) -> None:
        self.user_settings["username"] = set_username(self.user_settings["username"])
        self.appData.update_user_settings(self.user_settings)
    
        
    def delete_widgets(self) -> None:
        for slot in self.widget_grid:
            layout = self.widget_grid[slot].layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                
                
    def initialize_grid(self) -> None:
        self.delete_widgets()
        self.appData.reinitiate_slots()
        for slot in self.widget_grid:
            if self.appData.widget_settings[slot]["initialized"] == "yes":
                widget_type = self.appData.widget_settings[slot]["type"]
                widget_content = self.appData.get_contents_from_path(self.appData.widget_settings[slot]["content"])
                
                new_widget = initialize_widget(widget_type, widget_content)
                new_widget.setVisible(True)
                new_widget.widget_update.connect(partial(self.on_widget_update, slot=slot))
                self.widget_grid[slot].layout().addWidget(new_widget)
                
                self.ui.contentFrame.update()
                set_style(new_widget, self.appData.user_settings["main_color"])

            
    def on_widget_update(self, content: dict, slot: str) -> None:
        self.appData.update_widget_content(slot, content)

        
    #### EVENTS OVERRIDDEN ####
    def closeEvent(self, event) -> None:
        self.appData.update_user_settings(self.user_settings)
        self.appData.save_settings()
        event.accept()
        

    #####################################
    ########## TOOLBAR BUTTONS ##########
    #####################################
    
    #### COLOR THEME BUTTON ####
    def open_theme_picker_window(self) -> None:
        self.new_window = ThemePicker(self.user_settings["main_color"], self.user_settings["accent_color"])
        self.new_window.colors_changed.connect(self.on_colors_changed)
        self.new_window.exec()
        update_app_style(self.ui, self.user_settings)
        
    def on_colors_changed(self, new_main_color: str, new_accent_color: str) -> None:
        self.user_settings["main_color"] = new_main_color
        self.user_settings["accent_color"] = new_accent_color
        self.appData.update_user_settings(self.user_settings)
        self.initialize_grid()
        
        
    #### ADD WIDGET BUTTON ####
    def open_add_widget_window(self) -> None:
        if False in self.appData.widget_slots:
            self.new_window = AddWidget(self.appData)
            self.new_window.widget_added.connect(self.update_all_settings)
            self.new_window.exec()
            self.initialize_grid()


    #### REORDER WIDGETS BUTTON ####
    def open_reorder_widgets_window(self) -> None:
        if True in self.appData.widget_slots:
            self.new_window = ReorderWidgets(self.appData)
            self.new_window.widget_reordered.connect(self.update_all_settings)
            self.new_window.exec()
            self.initialize_grid()

        
    #### REMOVE WIDGET BUTTON ####
    def open_remove_widgets_window(self) -> None:
        if True in self.appData.widget_slots:
            self.new_window = RemoveWidget(self.appData)
            self.new_window.widget_removed.connect(self.update_all_settings)
            self.new_window.exec()
            self.initialize_grid()
 
    def update_all_settings(self, appData: AppData) -> None:
        self.appData.update_user_settings(appData.user_settings)
        self.appData.update_widget_settings(appData.widget_settings)
        self.appData.update_widget_grid(appData.widget_grid)
        self.appData.update_widget_slots(appData.widget_slots)

    
if __name__ == '__main__':
    run_as_admin()
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    
    window = MainWindow()
    window.setWindowTitle("pyDuctivity")
    window.show()

    sys.exit(app.exec())