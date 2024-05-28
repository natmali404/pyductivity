from constants import WidgetType

from widgets.pomodoro.pomodoro_widget import PomodoroWidget
from widgets.notes.notes_widget import NotesWidget


def initialize_widget(widget_type: str):
        if widget_type == WidgetType.POMODORO.value:
            #print("detected pomodoro!")
            new_widget = PomodoroWidget()
        else:
            #print("detected notes!")
            new_widget = NotesWidget()
        return new_widget
        #elif