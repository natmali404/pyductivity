from PySide6.QtWidgets import QDialog, QRadioButton
from PySide6.QtCore import Signal
from .addWidgetGui import Ui_Dialog
from constants import WidgetType, widget_list
from data_utils import AppData

class AddWidget(QDialog):
    def __init__(self, appData: AppData):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add a widget")
        self.radio_buttons = self.ui.widgetPlacementFrame.findChildren(QRadioButton)
        self.selected_slot_idx = -1
        
        self.appData = appData
        
        self.widget_grid = self.appData.widget_grid
        
        self.fill_combobox()
        self.setup_radio_buttons()
        self.ui.addWidgetButton.clicked.connect(self.add_widget_data)
    
    widget_added = Signal(AppData)
        
    
    def fill_combobox(self) -> None:
        for elem in WidgetType:
            self.ui.widgetTypeList.addItem(elem.value)
    
    
    def setup_radio_buttons(self) -> None:
        for i in range(8):
            if self.appData.widget_slots[i]:
                self.radio_buttons[i].setEnabled(False)
            self.radio_buttons[i].clicked.connect(lambda checked, i=i: self.set_selected_slot_idx(i))

    def set_selected_slot_idx(self, idx) -> None:
        self.selected_slot_idx = idx
        
    def add_widget_data(self) -> None:
        if self.selected_slot_idx != -1:
            selected_type = self.ui.widgetTypeList.currentText()
            self.appData.create_widget_data(widget_list[self.selected_slot_idx], selected_type)
            self.appData.widget_slots[self.selected_slot_idx] = True
            self.widget_added.emit(self.appData)
            self.close()    
        
        

