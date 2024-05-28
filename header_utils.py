from PySide6.QtWidgets import QLabel, QDialog
from PySide6.QtCore import QTimer, QTime
from name_prompt import NamePrompt

class ClockLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QTime.currentTime()
        hours_minutes = current_time.toString('hh:mm')
        seconds = current_time.toString('ss')
        self.setText(f"<html><head/><body><p><span style=' font-size:60pt;'>{hours_minutes}</span><span style=' font-size:30pt;'>:{seconds}</span></p></body></html>")
        

def set_username(username: str) -> str:
    if username == "":
        name_prompt = NamePrompt()  # Replace 'self' with the appropriate parent object.
        if name_prompt.exec() == QDialog.DialogCode.Accepted:
            username = name_prompt.get_name()
    return username
