import os, sys, pathlib, requests
import requests
from pathlib import Path
from colorama import init, Fore, Back, Style
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
# colorama initializer:

init()

# the <main> class for all the features.
class cmds:
    def __init__(self):
        self._valid = None
        self.app = QApplication(sys.argv)
        self.default_icon = "default_icon.png"

    def pre_greeter(self):
        print(Fore.RED + "-" * 35)
        print(Fore.YELLOW + " - Welcome to Wrapifier! ")
        print(Fore.RED + "-" * 35 + Fore.RESET)
        self.greeter()
        

    def check_valid(self):
        while True:
            _protocol = input("Enter (https:1)" + Fore.RED + " [recommended for most cases]" +Fore.RESET + " (http:2) : ")
            if _protocol == "1":
                _protocol = "https://"
                break
            elif _protocol == "2":
                _protocol = "http://"
                break
            
        try:
            print(Fore.YELLOW + "[Logs:] " + Fore.RESET + "Validating URL ...")
            url_request = requests.get(_protocol+self.url_input, timeout=10)
            url_response = url_request.status_code
            if url_response >= 200 and url_response <300:
                self._valid = True
            elif url_response >= 300 and url_response <400:
                redirect_permission = input(f"The site is redirected to {url_request.url} continue (y/n) : ")
                if redirect_permission == "y":
                    self._valid = True
                else:
                    self._valid = False

        except requests.exceptions.RequestException:
            self._valid = False        
    
    def greeter(self):
        while True:
            self.url_input = input("Enter your URL : ")
            self.check_valid()
            if self._valid == True:
                break
            print(Fore.RED + "[Error:] " + Fore.RESET + f"The url {self.url_input} is INVALID")

        from builder import Builder

        Builder().build(self.url_input)

    def icon_retry(self,_url):
        _url = Path(_url)
        if _url.is_dir():
            return("dir")
        elif not _url.exists():
            return("non_existent")
        else:
            return("valid")
    
    def build_input(self):
        self.title = input("Enter the title of your app : ")
        self.icon_choice = input("Would you like to add an icon? (y/n) :")
        if self.icon_choice == "y":
            self.icon = input("Enter the path to ur icon : ")
            while True:
                if self.icon_retry(self.icon) == "dir":
                    self.icon = input(Fore.RED + "[Error:] " + Fore.RESET + "path leads to a directory/folder, include file name : ")
                    if len(self.icon) == 0:
                        self.icon = self.default_icon
                        break
                
                elif self.icon_retry(self.icon) == "non_existent":
                    self.icon = input(Fore.RED + "[Error:] " + Fore.RESET + "path is invalid, Enter again : ")
                    if len(self.icon) == 0:
                        self.icon = self.default_icon    
                        break

                elif self.icon_retry(self.icon) == "valid":
                    print("Building the app")
                    break
        else:
            self.icon = self.default_icon


if __name__ == "__main__":
    startup = cmds()
    startup.pre_greeter()
