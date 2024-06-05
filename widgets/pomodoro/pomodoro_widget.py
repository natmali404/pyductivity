from PySide6.QtWidgets import QDialog
from ..square_widget import SquareWidget
from .pomodoroGui import Ui_Form
from PySide6.QtCore import Signal, QTimer
from .pomodoroEditGui import Ui_Dialog



class PomodoroWidget(SquareWidget):
    def __init__(self, content: dict, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.content = content
        
        self.mode = "work"
        self.remaining_seconds = self.content["work_time"] * 60
        
        self.update_timer_display()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.ui.runButton.clicked.connect(self.start_pause_timer)
        self.ui.editButton.clicked.connect(self.open_settings_window)
        
    
    def update_timer_display(self) -> None:
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.ui.timeLeftLabel.setText(f"{minutes:02d}:{seconds:02d}")

    def update_timer(self) -> None:
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.update_timer_display()
        else:
            self.timer.stop()
            self.change_mode()
            self.ui.runButton.setText("RUN")

    def start_pause_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            self.ui.runButton.setText("STOP")
        else:
            self.timer.stop()
            self.ui.runButton.setText("RUN")
    
    def change_mode(self):
        if self.mode == "work":
            self.mode = "rest"
            self.remaining_seconds = self.content["rest_time"] * 60
            self.update_timer_display()
            self.ui.modeLabel.setText("REST")
        else:
            self.mode = "work"
            self.remaining_seconds = self.content["work_time"] * 60
            self.update_timer_display()
            self.ui.modeLabel.setText("WORK")
    
    
    def open_settings_window(self) -> None:
        self.new_window = PomodoroEdit()
        self.new_window.time_changed.connect(self.update_settings)
        self.new_window.exec()
    
    def update_settings(self, work_time: int, rest_time: int) -> None:
        self.content["work_time"] = work_time
        self.content["rest_time"] = rest_time
        self.mode = "work"
        self.remaining_seconds = work_time * 60
        self.update_timer_display()
        self.widget_update.emit(self.content)
        
    
    def get_type(self) -> str:
        return "pomodoro"

    widget_update = Signal(dict)
    

    
class PomodoroEdit(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit pomodoro timer")
        self.ui.applyButton.clicked.connect(self.save_settings)
        
    def save_settings(self):
        work_time = self.ui.workTimeEdit.value()
        rest_time = self.ui.restTimeEdit.value()
        self.time_changed.emit(work_time, rest_time)
        self.close()
        
    time_changed = Signal(int, int)
            