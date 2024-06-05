from constants import WidgetType

from widgets.pomodoro.pomodoro_widget import PomodoroWidget
from widgets.notes.notes_widget import NotesWidget
from widgets.checklist.checklist_widget import ChecklistWidget
from widgets.website_blocker.website_blocker_widget import WebsiteBlockerWidget
from widgets.quotes.quotes_widget import QuotesWidget
from PySide6.QtWidgets import QGraphicsDropShadowEffect


def initialize_widget(widget_type: str, widget_content: dict):
        if widget_type == WidgetType.POMODORO.value:
            new_widget = PomodoroWidget(widget_content)
        elif widget_type == WidgetType.NOTES.value:
            new_widget = NotesWidget(widget_content)
        elif widget_type == WidgetType.CHECKLIST.value:
            new_widget = ChecklistWidget(widget_content)
        elif widget_type == WidgetType.QUOTES.value:
            new_widget = QuotesWidget(widget_content)
        else:
            new_widget = WebsiteBlockerWidget(widget_content)
        return new_widget
        
        
def set_style(new_widget, accent_color: str) -> None:
        new_widget.setObjectName("fullWidget")
        new_widget.setStyleSheet(f"""
                #fullWidget {{
                    border-radius: 20px;
                    background-color: {accent_color};
                    
                }}   
                #widgetTitleLabel {{
                    background-color: none;
                }}
        """)
        if new_widget.get_type() == WidgetType.POMODORO.value:
            new_widget.setStyleSheet(new_widget.styleSheet() + f"""
                QLabel {{
                    background-color: none;
                }}
                QPushButton#runButton {{
                    border-radius: 5px; /* Ensure buttons are not affected by parent styles */
                    background-color: #000000;
                    color: white;
                }}
                QPushButton#editButton {{
                    border: 0px solid black;
                    text-decoration: underline;
                    background-color: none;
                }}
            """)
        elif new_widget.get_type() == WidgetType.CHECKLIST.value:
            new_widget.setStyleSheet(new_widget.styleSheet() + f"""
                QFrame {{
                    background-color: {accent_color};
                }}
                QLineEdit {{
                    background-color: {accent_color};
                    border: 0px solid black;
                }}
                QPushButton {{
                    border-radius: 5px; /* Ensure buttons are not affected by parent styles */
                    font-size: 15px;
                    font-weight: bold;
                }}
            """)
        elif new_widget.get_type() == WidgetType.NOTES.value:
            new_widget.setStyleSheet(new_widget.styleSheet() + f"""
                QLineEdit::placeholderText {{
                color: grey;
                text-style: italic;
                }}
                QLineEdit {{
                    background-color: {accent_color};
                    border: none;
                    border-bottom: 2px solid black;
                    font-weight: bold;
                    font-size: 16px;
                }}
                QTextEdit {{
                    background-color: {accent_color};
                    border: 0px solid black;
                }}
                #showFullNoteButton {{
                    border: 0px solid black;
                    text-decoration: underline;
                    background-color: none;
                }}
            """)
        elif new_widget.get_type() == WidgetType.WEBSITE_BLOCKER.value:
            new_widget.setStyleSheet(new_widget.styleSheet() + f"""
                QPushButton#blockButton {{
                    border-radius: 5px; /* Ensure buttons are not affected by parent styles */
                    background-color: #000000;
                    color: white;
                }}
                QLabel {{
                    background-color: none;
                }}
                #editButton {{
                    border: 0px solid black;
                    text-decoration: underline;
                    background-color: none;
                
                }}
            """)
        elif new_widget.get_type() == WidgetType.QUOTES.value:
            new_widget.setStyleSheet(new_widget.styleSheet() + f"""
                #refreshButton {{
                    border: 0px solid black;
                    background-color: {accent_color};
                    font-size: 30px;
                    font-weight: bold;
                }}
                #moreButton {{
                    border: 0px solid black;
                    text-decoration: underline;
                    background-color: none;
                }}
                QLabel {{
                    background-color: {accent_color};
                }}
                    """)
            
        shadow = QGraphicsDropShadowEffect(new_widget)
        shadow.setBlurRadius(10)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor("#636363")
        new_widget.setGraphicsEffect(shadow)
        new_widget.update()