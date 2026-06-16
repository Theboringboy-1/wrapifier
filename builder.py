import os, sys, subprocess
from colorama import init, Fore, Back, Style
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
import shutil

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
        subprocess.run(
            [
                sys.executable,
                "main.py",
                str(self.url_input),
                str(self.title),
                str(self.icon),
            ]
        )

        # making a copy of <main.py>
        shutil.copy("main.py", f"{self.url_input}.py")
        # initializing file name
        file_name = f"{self.url_input}.py"

        # opening the file:
        with open(file_name, "r") as f:
            lines = f.readlines()

        # deleting the lines 16 to 25
        del lines[17:25]

        # making self variables as local variables.
        lines.insert(15, f'icon_window = "{self.icon}"\n')
        lines.insert(16, f'title_window = "{self.title}"\n')
        lines.insert(17, f'url_to_build = "{self.url_input}"\n')

        # adding link validation ( required to work proper. )
        lines.insert(21, 'if not url_to_build.startswith(("http://", "https://")):\n')
        lines.insert(22, '    url_to_build = "https://" + url_to_build\n')

        # writing back the files.
        with open(file_name, "w") as f:
            f.writelines(lines)

        shutil.move(file_name, f"builds/{file_name}")

        if self.have_icon:
            shutil.move("converted.ico", "builds/converted.ico")
        else:
            shutil.copy("long-paper-roll.png", "builds/long-paper-roll.png")
