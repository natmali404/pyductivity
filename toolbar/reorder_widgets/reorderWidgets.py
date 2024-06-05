from PySide6.QtWidgets import QDialog, QRadioButton
from PySide6.QtCore import Signal
from .reorderWidgetsGui import Ui_Dialog
from constants import widget_list, default_widget_settings
from data_utils import AppData

class ReorderWidgets(QDialog):
    def __init__(self, appData: AppData):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Reorder widgets")
        self.appData = appData
        
        self.ui.applyButton.setEnabled(False)
        self.current_selected_position = -1
        self.new_selected_position = -1
        
        self.current_position_radio_buttons = self.ui.currentWidgetPositionFrame.findChildren(QRadioButton)
        self.new_position_radio_buttons = self.ui.newWidgetPositionFrame.findChildren(QRadioButton)
        
        self.fill_combobox()
        self.selected_widget = self.ui.widgetsComboBox.currentText()
        self.new_widget_selected()
        
        self.ui.widgetsComboBox.currentTextChanged.connect(self.new_widget_selected)
        self.ui.applyButton.clicked.connect(self.reorder_widget)
        self.ui.applyButton.clicked.connect(self.close)

        for radio_button in self.new_position_radio_buttons:
            radio_button.clicked.connect(self.new_position_selected)
        
    
    widget_reordered = Signal(AppData)
        
    
    def fill_combobox(self) -> None:
        for slot in self.appData.widget_grid:
            if self.appData.widget_grid[slot].layout().itemAt(0):
                self.ui.widgetsComboBox.addItem(f'{self.appData.widget_grid[slot].objectName()} ({self.appData.widget_grid[slot].layout().itemAt(0).widget().get_type()})')
    
    
    def new_widget_selected(self) -> None:
        self.selected_widget = self.ui.widgetsComboBox.currentText().split()[0]
        self.current_selected_position = widget_list.index(self.selected_widget)
        
        
        index = widget_list.index(self.selected_widget)
        for radio_button in self.current_position_radio_buttons:
            radio_button.setEnabled(False)
        self.current_position_radio_buttons[index].setChecked(True)
        
        for radio_button in self.new_position_radio_buttons:
            radio_button.setEnabled(True)
        self.new_position_radio_buttons[index].setChecked(False)
        self.new_position_radio_buttons[index].setEnabled(False)
        
        
    def new_position_selected(self) -> None:
        self.ui.applyButton.setEnabled(True)
        self.new_selected_position = self.new_position_radio_buttons.index(self.sender())
        print(self.new_selected_position)
    
    
    def reorder_widget(self) -> None:
        if self.current_selected_position == self.new_selected_position:
            self.close()
        elif self.appData.widget_slots[self.new_selected_position] == True:
            print("ding ding")
            replaced_widget_name = widget_list[self.new_selected_position]
            replaced_widget_data = self.appData.get_single_widget_data(replaced_widget_name)
            replacing_widget_name = widget_list[self.current_selected_position]
            replacing_widget_data = self.appData.get_single_widget_data(replacing_widget_name)
            
            self.appData.widget_settings[replaced_widget_name] = replacing_widget_data
            self.appData.widget_settings[replacing_widget_name] = replaced_widget_data
        else:
            self.appData.widget_settings[widget_list[self.new_selected_position]] = self.appData.get_single_widget_data(widget_list[self.current_selected_position])
            self.appData.widget_settings[widget_list[self.current_selected_position]] = default_widget_settings

        self.widget_reordered.emit(self.appData)
        