from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class NamePrompt(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.resize(350, 100)
        
        self.setWindowTitle("Welcome to pyDuctivity! Please enter your name:")
        self.mainLayout = QVBoxLayout(self)
        self.nameInput = QLineEdit(self)
        self.okButton = QPushButton("Go!", self)

        self.mainLayout.addWidget(self.nameInput)
        self.mainLayout.addWidget(self.okButton)

        self.okButton.clicked.connect(self.accept)

    def accept(self) -> None:
        self.name = self.nameInput.text()
        super().accept()

    def get_name(self) -> str:
        return self.name