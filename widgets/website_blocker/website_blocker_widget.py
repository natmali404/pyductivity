import os
from PySide6.QtWidgets import QDialog
from ..square_widget import SquareWidget
from .websiteBlockerGui import Ui_Form
from PySide6.QtCore import Signal

from .websiteBlockerEditGui import Ui_Dialog


class WebsiteBlockerWidget(SquareWidget):
    def __init__(self, content: dict, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.content = content
        self.blocking_enabled = False if self.content["status"] == "off" else True
        
        self.update_ui()
        
        self.ui.blockButton.clicked.connect(self.toggle_blocking)
        self.ui.editButton.clicked.connect(self.open_settings_window)

    def open_settings_window(self):
        dialog = WebsiteBlockerEdit(self.content["blocked_websites"])
        dialog.data_changed.connect(self.update_content)
        dialog.exec_()

    def update_content(self, data):
        self.content["blocked_websites"] = data
        self.widget_update.emit(self.content)
        
    def toggle_blocking(self):
        self.blocking_enabled = not self.blocking_enabled
        if self.blocking_enabled:
            self.content["status"] = "on"
        else:
            self.content["status"] = "off"
        self.widget_update.emit(self.content)
        self.block_websites()
        self.update_ui()

    def update_ui(self):
        if self.blocking_enabled:
            self.ui.statusLabel.setText("ON")
            self.ui.blockButton.setText("UNBLOCK")
        else:
            self.ui.statusLabel.setText("OFF")
            self.ui.blockButton.setText("BLOCK")

    def block_websites(self):
        hosts_path = self.get_hosts_path()
        redirect_ip = "127.0.0.1"
        try:
            with open(hosts_path, "r+") as file:
                lines = file.readlines()
                file.seek(0)
                #remove previously blocked websites
                lines = [line for line in lines if not any(website.strip("https://").strip("http://").strip("www.") in line for website in self.content["blocked_websites"])]
                if self.blocking_enabled:
                    for website in self.content["blocked_websites"]:
                        website = website.replace("https://", "").replace("http://", "").strip("/")
                        lines.append(f"{redirect_ip} {website}\n")
                        if "www." not in website:
                            lines.append(f"{redirect_ip} www.{website}\n")
                        else:
                            lines.append(f"{redirect_ip} {website.replace('www.', '')}\n")
                        
                file.writelines(lines)
                file.truncate()
        except PermissionError:
            print("Permission denied. Please run the program as an administrator.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_hosts_path(self):
        if os.name == 'nt':  #windows
            return r"C:\Windows\System32\drivers\etc\hosts"
        else:
            return "/etc/hosts"
    

    def get_type(self) -> str:
        return "website_blocker"
    
    
    def closeEvent(self, event) -> None:
        self.blocking_enabled = False
        self.block_websites()
        event.accept()

    widget_update = Signal(dict)
    

    
class WebsiteBlockerEdit(QDialog):
    def __init__(self, content):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit blocked websites")
        self.content = content
        if self.content == []:
            self.ui.websiteListEdit.setPlainText("")
        else:
            self.ui.websiteListEdit.setPlainText("\n".join(self.content))
        self.ui.websiteListEdit.textChanged.connect(self.update_data)
              
    
    def update_data(self):
        data = self.ui.websiteListEdit.toPlainText().rstrip('\n').split("\n")
        self.data_changed.emit(data)

        
    data_changed = Signal(list)
            