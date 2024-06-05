import random
from PySide6.QtWidgets import QDialog
from ..square_widget import SquareWidget
from .quotesGui import Ui_Form
from PySide6.QtCore import Signal, QTimer
from .quotesEditGui import Ui_Dialog

class QuotesWidget(SquareWidget):
    def __init__(self, content, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
        self.content = content
        self.autorefresh = self.content["autorefresh"]
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.set_random_quote)

        self.set_random_quote()

        self.ui.refreshButton.setText("⟳")
        self.ui.refreshButton.clicked.connect(self.set_random_quote)
        self.ui.moreButton.clicked.connect(self.open_details_window)

        if self.autorefresh:
            self.toggle_autorefresh()


    def set_random_quote(self) -> None:
        if not self.content["quotes"]:
            self.ui.quoteLabel.setText("")
        else:
            self.ui.quoteLabel.setText(random.choice(self.content["quotes"]))


    def open_details_window(self) -> None:
        self.new_window = QuotesEdit(self.content)
        self.new_window.data.connect(self.update_data)
        self.new_window.exec()
        self.set_random_quote()
    
    
    def update_data(self, content: dict) -> None:
        self.content = content
        if self.content["autorefresh"] != self.autorefresh:
            self.toggle_autorefresh()
        self.widget_update.emit(self.content)
    
    
    def toggle_autorefresh(self) -> None:
        self.autorefresh = self.content["autorefresh"]
        if self.autorefresh:
            interval = self.content["interval"] * 60 * 1000
            self.timer.start(interval)
        else:
            self.timer.stop()


    def get_type(self) -> str:
        return "quotes"
    
    widget_update = Signal(dict)


class QuotesEdit(QDialog):
    def __init__(self, content: dict):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit quotes")
        self.content = content
        
        self.initiate_quotes()
        
        self.ui.autorefreshCheckBox.stateChanged.connect(self.toggle_autorefresh)
        
    data = Signal(dict)
    
    def initiate_quotes(self) -> None:
        self.ui.quotesListEdit.setPlainText("\n".join(self.content["quotes"]))
        self.ui.autorefreshCheckBox.setChecked(self.content["autorefresh"])
        if self.content["autorefresh"]:
            self.ui.autorefreshIntervalSpinBox.setValue(self.content["interval"])
        else:
            self.ui.autorefreshIntervalSpinBox.setEnabled(False)
    
    def toggle_autorefresh(self) -> None:
        if self.ui.autorefreshCheckBox.isChecked():
            self.ui.autorefreshIntervalSpinBox.setEnabled(True)
        else:
            self.ui.autorefreshIntervalSpinBox.setEnabled(False)
    
    def update_quotes(self) -> None:
        self.content["autorefresh"] = self.ui.autorefreshCheckBox.isChecked()
        self.content["interval"] = self.ui.autorefreshIntervalSpinBox.value()
        self.content["quotes"] = self.ui.quotesListEdit.toPlainText().rstrip("\n").split("\n")
        self.data.emit(self.content)
    
    def closeEvent(self, event) -> None:
        self.update_quotes()
