import json


class AppData():
    def __init__(self):
        self.user_settings = self.load_settings()
        self.widget_grid = {}
        #self.widget_grid = self.initialize_grid()
        
    # def initialize_grid(self):
    #     collected_widgets = sorted(self.ui.contentFrame.findChildren(SquareWidget), key=lambda widget: widget.objectName())
    #     widget_grid = {key: value for key, value in zip(widget_list, collected_widgets)}
    #     print(widget_grid)
    #     return widget_grid


    
    ## settings 
    
    def load_settings(self) -> dict:
        try:   
            with open('userdata/settings.json', 'r') as f:
                user_settings = json.load(f)
                #print(f'Data loaded successfully: {user_settings}')
                
        except FileNotFoundError:
            with open('userdata/init_settings.json', 'r') as f: #try catch na brak init settings?
                user_settings = json.load(f)
            print(f'Error loading data! Initial data loaded: {user_settings}')
        
        return user_settings


    def save_settings(self) -> None:    
        with open('userdata/settings.json', 'w') as f:
            json.dump(self.user_settings, f, indent=4)
            #print(f'Data saved successfully: {self.user_settings}')
            
    
        
    def update_settings(self, user_settings: dict):
        self.user_settings = user_settings
        
    
    def get_settings(self) -> dict:
        return self.user_settings
    
    
    ## widget grid
    
    def initiate_widget_grid(self, widget_name_list: list, widget_list: list):
        self.widget_grid = {key: value for key, value in zip(widget_name_list, widget_list)}
    
    def update_widget_grid(self, widget_grid: dict):
        self.widget_grid = widget_grid
        
    def get_widget_grid(self) -> dict:
        return self.widget_grid

    def update_widget_data(self, widget_key: str, widget_property: str, value: str) -> None:
        self.user_settings[widget_key][widget_property] = value
        
        
