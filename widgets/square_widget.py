from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import QSize

class SquareWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))
        self.setMinimumSize(200,200)
        self.update()

    def resizeEvent(self, event) -> None:
        size = min(self.width(), self.height())
        self.resize(QSize(size, size))
        super().resizeEvent(event)

    def sizeHint(self) -> QSize:
        return QSize(100, 100)

    def minimumSizeHint(self) -> QSize:
        return QSize(100, 100)
