from PySide6.QtWidgets import QDialog, QRadioButton
from PySide6.QtCore import Signal
from .removeWidgetGui import Ui_Dialog
from constants import widget_list, default_widget_settings
from data_utils import AppData

class RemoveWidget(QDialog):
    def __init__(self, appData: AppData):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Remove a widget")
        
        self.appData = appData
        self.current_selected_position = -1
        
        self.current_position_radio_buttons = self.ui.widgetPositionframe.findChildren(QRadioButton)
        
        self.fill_combobox()
        self.selected_widget = self.ui.widgetComboBox.currentText()
        self.new_widget_selected()
        
        self.ui.widgetComboBox.currentTextChanged.connect(self.new_widget_selected)
        self.ui.applyButton.clicked.connect(self.remove_widget)
        self.ui.applyButton.clicked.connect(self.close)

    
    widget_removed = Signal(AppData)
        
    
    def fill_combobox(self) -> None:
        for slot in self.appData.widget_grid:
            if self.appData.widget_grid[slot].layout().itemAt(0):
                self.ui.widgetComboBox.addItem(f'{self.appData.widget_grid[slot].objectName()} ({self.appData.widget_grid[slot].layout().itemAt(0).widget().get_type()})')
    
    
    def new_widget_selected(self) -> None:
        self.selected_widget = self.ui.widgetComboBox.currentText().split()[0]
        self.current_selected_position = widget_list.index(self.selected_widget)
        
        index = widget_list.index(self.selected_widget)
        for radio_button in self.current_position_radio_buttons:
            radio_button.setEnabled(False)
        self.current_position_radio_buttons[index].setChecked(True)
        
        
    def remove_widget(self) -> None:

        self.appData.widget_settings[self.selected_widget] = default_widget_settings.copy()
        self.appData.widget_slots[widget_list.index(self.selected_widget)] = False
        print(self.appData.widget_settings)
        print(self.appData.widget_slots)
        
        self.widget_removed.emit(self.appData)
        
