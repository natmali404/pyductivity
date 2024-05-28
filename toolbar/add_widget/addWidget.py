from PySide6.QtWidgets import QDialog, QColorDialog, QRadioButton
from PySide6.QtCore import Signal
from .addWidgetGui import Ui_Dialog
from constants import WidgetType, widget_slots
from widgets.widget_utils import initialize_widget
from data_utils import AppData

class AddWidget(QDialog):
    def __init__(self, appData: AppData):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.radio_buttons = self.ui.widgetPlacementFrame.findChildren(QRadioButton)
        self.selected_slot_idx = -1
        
        self.appData = appData
        
        self.widget_grid = self.appData.get_widget_grid()
        
        self.fill_combobox()
        self.setup_radio_buttons()
        self.ui.addWidgetButton.clicked.connect(self.add_widget)
        self.ui.addWidgetButton.clicked.connect(self.close)
    
    widget_added = Signal(dict)
        
    
    def fill_combobox(self):
        for elem in WidgetType:
            self.ui.widgetTypeList.addItem(elem.value)
    
    
    def setup_radio_buttons(self):
        for i in range(8):
            if widget_slots[i]:
                self.radio_buttons[i].setEnabled(False)
            self.radio_buttons[i].clicked.connect(lambda checked, i=i: self.set_selected_slot_idx(i))

    def set_selected_slot_idx(self, idx):
        self.selected_slot_idx = idx
        
    def add_widget(self):
        selected_type = self.ui.widgetTypeList.currentText()
        new_widget = initialize_widget(selected_type)
        selected_key = list(self.widget_grid.keys())[self.selected_slot_idx]
        #self.widget_grid[selected_key] = self.widget_grid[selected_key].addWidget(new_widget)
        self.appData.update_widget_data(list(self.widget_grid.keys())[self.selected_slot_idx], "initialized", "yes")
        print(new_widget.get_type())
        self.appData.update_widget_data(list(self.widget_grid.keys())[self.selected_slot_idx], "type", new_widget.get_type())
        self.widget_added.emit(self.appData.get_settings())
        
        




#dodanie widzetu:
#wybranie z listy typu
#wybranie miejsce -> szare radio buttony tam gdzie jest zajete

#utworzenie obiektu zaleznie do wybranego typu w odpowiednim slocie na buttonie
