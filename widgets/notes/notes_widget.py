from PySide6.QtWidgets import QDialog
from ..square_widget import SquareWidget
from .notesGui import Ui_Form
from PySide6.QtCore import Signal
from .notesDetailsGui import Ui_Form as Ui_FormDetails

class NotesWidget(SquareWidget):
    def __init__(self, content, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.content = content
        self.ui.titleEdit.setPlaceholderText("Note title...")
        
        self.ui.titleEdit.setText(self.content["title"])
        self.ui.textEdit.setPlainText(self.content["text"])

        self.ui.textEdit.textChanged.connect(self.update_note)
        self.ui.titleEdit.textChanged.connect(self.update_note)

        self.ui.showFullNoteButton.clicked.connect(self.open_details_window)
        

    def open_details_window(self) -> None:
        self.new_window = NotesDetails(self.content)
        self.new_window.note_data.connect(self.update_note_from_details)
        self.new_window.exec()  
    
    
    def update_note_from_details(self, content: dict) -> None:
        self.content = content
        self.ui.titleEdit.setText(self.content["title"])
        self.ui.textEdit.setPlainText(self.content["text"])
        self.widget_update.emit(self.content)
    
    
    def update_note(self) -> None:
        self.content["title"] = self.ui.titleEdit.text()
        self.content["text"] = self.ui.textEdit.toPlainText()
        self.widget_update.emit(self.content)
        
        
    def get_type(self):
        return "notes"
    
    widget_update = Signal(dict)
    

class NotesDetails(QDialog):
    def __init__(self, content: dict):
        QDialog.__init__(self)
        self.ui = Ui_FormDetails()
        self.ui.setupUi(self)
        self.setWindowTitle("Note details")
        self.content = content
        self.ui.titleEdit.setText(self.content["title"])
        self.ui.textEdit.setPlainText(self.content["text"])
        
        self.ui.textEdit.textChanged.connect(self.update_note)
        self.ui.titleEdit.textChanged.connect(self.update_note)
        
    note_data = Signal(dict)
    
    def update_note(self) -> None:
        self.content["title"] = self.ui.titleEdit.text()
        self.content["text"] = self.ui.textEdit.toPlainText()
        self.note_data.emit(self.content)
    
    def closeEvent(self, event) -> None:
        self.update_note()