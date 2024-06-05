import json
from constants import widget_list, default_widget_settings, default_basic_settings, widget_slots, pomodoro_default_data, checklist_default_data, notes_default_data, website_blocker_default_data, quotes_default_data
from datetime import datetime


class AppData():
    def __init__(self):
        self.user_settings, self.widget_settings = self.load_settings()
        #print(f"Loaded user settings: {self.user_settings}")
        #print(f"Loaded widget settings: {self.widget_settings}")
        self.widget_grid = {}
        self.widget_slots = widget_slots
        self.reinitiate_slots()


    def load_settings(self) -> tuple:
        try:   
            with open('userdata/user_settings.json', 'r') as f:
                user_settings = json.load(f)
                #print(f'User data loaded successfully: {user_settings}')      
        except FileNotFoundError:
            user_settings = self.generate_new_user_settings()
            #print(f'Error loading data! New date file created: {user_settings}')

        try:
            with open('userdata/widget_settings.json', 'r') as f:
                widget_settings = json.load(f)
                #print(f'Widget data loaded successfully: {widget_settings}') 
        except FileNotFoundError:
            widget_settings = self.generate_new_widget_settings()
            #print(f'Error loading data! New date file created: {widget_settings}')
        
        return user_settings, widget_settings


    def save_settings(self) -> None:    
        with open('userdata/user_settings.json', 'w') as f:
            json.dump(self.user_settings, f, indent=4)
        with open('userdata/widget_settings.json', 'w') as f:
            json.dump(self.widget_settings, f, indent=4)
            
        #print(f'Data saved successfully:\n->{self.user_settings}\n->{self.widget_settings}')
            
       
        
    def update_user_settings(self, user_settings: dict) -> None:
        self.user_settings = user_settings
        self.save_settings()
        
    def update_widget_settings(self, widget_settings: dict) -> None:
        self.widget_settings = widget_settings
        self.save_settings()
        
    
    
    ## widget grid
    
    def initiate_widget_grid(self, widget_name_list: list, widget_list: list) -> None:
        self.widget_grid = {key: value for key, value in zip(widget_name_list, widget_list)}
        self.reinitiate_slots()
    
    def reinitiate_slots(self) -> None:
        self.widget_slots = [False for _ in range(8)]
        slot_idx = 0
        for slot in self.widget_grid:
            if self.widget_settings[slot]["initialized"] == "yes":
                self.widget_slots[slot_idx] = True
            slot_idx += 1

    
    def update_widget_grid(self, widget_grid: dict) -> None:
        self.widget_grid = widget_grid
        
    
    def update_widget_slots(self, widget_slots: list) -> None:
        self.widget_slots = widget_slots

    def update_widget_content(self, widget_key: str, content: dict) -> None:
        filename = self.widget_settings[widget_key]["content"]
        with open(f'userdata/widget_data/{filename}', 'w') as file:
                json.dump(content, file, indent=4)
    
    def get_single_widget_data(self, widget_key: str) -> dict:
        return self.widget_settings[widget_key]
    
    def set_single_widget_data(self, widget_key: str, widget_data: dict) -> None:
        self.widget_settings[widget_key] = widget_data
    
    
    
     
    def create_widget_data(self, widget_slot: str, widget_type: str) -> None:
        self.widget_settings[widget_slot]["initialized"] = "yes"
        self.widget_settings[widget_slot]["type"] = widget_type
        now = datetime.now()
        filename_number = now.strftime("%Y%m%d%H%M%S")
        content_filename = f'{widget_type}_{filename_number}.json'
        self.widget_settings[widget_slot]["content"] = content_filename
        self.create_default_widget_content(widget_type, content_filename)
    
    
    def create_default_widget_content(self, type: str, filename: str) -> None:
        if(type == "pomodoro"):
            data_to_insert = pomodoro_default_data
        elif(type == "notes"):
            data_to_insert = notes_default_data
        elif(type == "checklist"):
            data_to_insert = checklist_default_data
        elif(type == "website_blocker"):
            data_to_insert = website_blocker_default_data
        elif(type == "quotes"):
            data_to_insert = quotes_default_data
        else:
            data_to_insert = {}
        with open(f'userdata/widget_data/{filename}', 'w') as file:
            json.dump(data_to_insert, file, indent=4)
        
        
    def get_contents_from_path(self, filename: str) -> dict:
        with open(f'userdata/widget_data/{filename}', 'r') as file:
            return json.load(file)
        
        
        
    #generative
    def generate_new_user_settings(self) -> dict:
        with open('userdata/user_settings.json', 'w') as file:
            json.dump(default_basic_settings, file, indent=4)
        #print("user_settings.json file has been created with the default structure.")
        return default_basic_settings
    
    def generate_new_widget_settings(self) -> dict:
        widgets_data = {widget_name: default_widget_settings.copy() for widget_name in widget_list}
        with open('userdata/widget_settings.json', 'w') as file:
            json.dump(widgets_data, file, indent=4)
        #print("widget_settings.json file has been created with the default structure.")
        return widgets_data