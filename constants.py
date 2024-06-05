from enum import Enum

class WidgetType(Enum):
    POMODORO = 'pomodoro'
    NOTES = 'notes'
    CHECKLIST = 'checklist'
    WEBSITE_BLOCKER = 'website_blocker'
    QUOTES = 'quotes'
    

default_basic_settings = {
    "username": "",
    "main_color": "#b0b0b0",
    "accent_color": "#84688f"
}


widget_slots = [False, False, False, False, False, False, False, False]

widget_list = ["widget_1", "widget_2", "widget_3", "widget_4", "widget_5", "widget_6", "widget_7", "widget_8"]

default_widget_settings = {
    "initialized": "no",
    "type": "",
    "content": "" # pathtofile.txt
}

pomodoro_default_data = {
    "work_time": 25,
    "rest_time": 5
}

notes_default_data = {
    "title": "",
    "text": """:)"""
}

checklist_default_data = {
    0: {
        "status": "checked",
        "text": "grocery shopping"
    },
    1: {
        "status": "unchecked",
        "text": "clean the house"
    }
}

website_blocker_default_data = {
    "status": "off",
    "blocked_websites": []
}

quotes_default_data = {
    "autorefresh": False,
    "interval": 5,
    "quotes": []
}

