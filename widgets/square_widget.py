from PySide6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import QSize

class SquareWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))
        #print(f"SquareWidget initialized!")
        #self.label = QLabel("Test", self)
        self.setMinimumSize(200,200)
        self.update()

    def resizeEvent(self, event):
        size = min(self.width(), self.height())
        self.resize(QSize(size, size))
        super().resizeEvent(event)

    def sizeHint(self):
        return QSize(100, 100)  # Default size of 100x100, but it will be square regardless of size

    def minimumSizeHint(self):
        return QSize(100, 100)  # Minimum size of 20x20 to prevent it from becoming too small
