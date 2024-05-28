from PySide6.QtWidgets import QLabel
from ..square_widget import SquareWidget
from .notesGui import Ui_Form

class NotesWidget(SquareWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #print(f"NotesWidget initialized!")
        #self.label = QLabel("PomodoroWidget", self)
        #self.update()
        
    def get_type(self):
        return "notes"