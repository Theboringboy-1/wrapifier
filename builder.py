import os, sys, subprocess
from colorama import init, Fore, Back, Style
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile

# Importing the cmds class to inherit.
from commandline import cmds

# colorama initializer:
init()

# the <main> class for the build process.
class Builder(cmds):
    def __init__(self):
        self.default_icon = "default_icon.png"

    # doc: <build> method: 
    def build(self, url):
        print(Fore.YELLOW + "[LOGS:] " + Fore.RESET + "Attempting Build ...")
        self.url_input = url
        self.build_input()
        
        # attempting build run.
        subprocess.run(["python", "main.py", self.url_input, self.title, self.icon])

    