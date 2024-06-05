from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QSizePolicy, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout
from ..square_widget import SquareWidget
from .checklistGui import Ui_Form
from PySide6.QtCore import Signal, QSize
from PySide6.QtCore import Qt


class ChecklistWidget(SquareWidget):
    def __init__(self, content: dict, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.layout_setup()

        self.content = content
        self.reinitiate_checklist()

        
    def layout_setup(self) -> None:
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ui.contentFrame.setLayout(main_layout)
        
        remove_button_layout = QVBoxLayout()
        remove_button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ui.removeButtonFrame.setLayout(remove_button_layout)
        
        
    
    def reinitiate_checklist(self) -> None:
        main_layout = self.ui.contentFrame.layout()
        self.clear_layout(main_layout)
        self.clear_layout(self.ui.removeButtonFrame.layout())

        for item_id, item_data in self.content.items():
            new_layout, remove_button = self.new_checklist_item_layout(item_id, item_data)
            self.ui.contentFrame.layout().addLayout(new_layout) # type: ignore
            self.ui.removeButtonFrame.layout().addWidget(remove_button)

        add_button = self.new_add_button()
        main_layout.addWidget(add_button)
        
        self.ui.contentFrame.setLayout(main_layout)

            
    def clear_layout(self, layout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                sublayout = item.layout()
                if sublayout:
                    self.clear_layout(sublayout)
        
    def new_add_button(self) -> QPushButton:
        add_button = QPushButton()
        add_button.clicked.connect(self.add_item)
        add_button.setText("+")
        add_button.setFixedSize(QSize(20, 20))
        add_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return add_button
            
    def add_item(self) -> None:
        add_button = self.sender()
        add_button.deleteLater()
        if self.content == {}:
            last_id = -1
        else:
            last_id = max(map(int, self.content.keys()))  
        print(last_id)
        self.content[last_id + 1] = {"status": "unchecked", "text": ""}
        new_layout, remove_button = self.new_checklist_item_layout(last_id + 1, {"status": "unchecked", "text": ""})
        self.ui.contentFrame.layout().addLayout(new_layout) # type: ignore
        self.ui.removeButtonFrame.layout().addWidget(remove_button)
        if last_id < 4:
            add_button = self.new_add_button()
            self.ui.contentFrame.layout().addWidget(add_button)
        print(self.content)
    
    
    def new_checklist_item_layout(self, item_id: int, item_data: dict) -> tuple:
            item_layout = QHBoxLayout()
            item_layout.setProperty("id", item_id)

            checkbox = QCheckBox()
            checkbox.setChecked(item_data["status"] == "checked")
            checkbox.setProperty("id", item_id)
            checkbox.checkStateChanged.connect(self.update_content)
            checkbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            item_layout.addWidget(checkbox)

            plaintext_edit = QLineEdit()
            plaintext_edit.setText(item_data["text"])
            plaintext_edit.setFixedHeight(18)
            plaintext_edit.setProperty("id", item_id)
            plaintext_edit.textChanged.connect(self.update_content)
            plaintext_edit.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            item_layout.addWidget(plaintext_edit)


            remove_button = QPushButton()
            remove_button.setProperty("id", item_id)
            remove_button.clicked.connect(self.remove_item)
            remove_button.setText("X")
            remove_button.setFixedSize(QSize(18, 18))
            remove_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            
            return item_layout, remove_button
        
    
    widget_update = Signal(object)
    
    def update_content(self) -> None:
        sender = self.sender()
        key = sender.property("id")
        if isinstance(sender, QCheckBox):
            self.content[key]["status"] = "checked" if sender.isChecked() else "unchecked"
        elif isinstance(sender, QLineEdit):
            self.content[key]["text"] = sender.text()
            
        self.widget_update.emit(self.content)
    

    def remove_item(self) -> None:
        key_to_remove = self.sender().property("id")
        del self.content[key_to_remove]
        
        new_content = {}
        idx = 0
        for elem in self.content:
            new_content[idx] = self.content[elem]
            idx += 1
            
        self.content = new_content
        
        self.reinitiate_checklist()


    def get_type(self) -> str:
        return "checklist"
    
    