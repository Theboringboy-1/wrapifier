import os, sys, subprocess
from colorama import init, Fore, Back, Style
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
import shutil
from win32com.client import Dispatch
from pathlib import Path

# Importing the cmds class to inherit.
from commandline import cmds

# colorama initializer:
init()


# the <main> class for the build process.
class Builder(cmds):
    def __init__(self):
        self.default_icon = "default_icon.png"

    def create_shortcut(self):

        # Dispatching the shell:
        shell = Dispatch("WScript.Shell")

        desktop = Path.home() / "Desktop"
        shortcut_path = desktop / f"{self.title}.lnk"

        # initialize a shortcut:
        shortcut = shell.CreateShortCut(str(shortcut_path))

        exe_path = Path(f"builds/{self.title}/{self.url_input}.exe").resolve()

        shortcut.Targetpath = str(exe_path)
        shortcut.WorkingDirectory = str(exe_path.parent)

        if self.have_icon:
            shortcut.IconLocation = f"builds/{self.title}/converted.ico"
        else:
            shortcut.IconLocation = f"builds/{self.title}/long-paper-roll.ico"

        shortcut.save()

    def pyinstaller_build(self):
        check = subprocess.run(
            [sys.executable, "-m", "pip", "show", "pyinstaller"],
            capture_output=True,
            text=True,
        )

        if check.returncode != 0:
            print(Fore.RED + "[Error:] " + Fore.RESET + "PyInstaller is not installed")
            return

        build_dir = os.path.join("builds", self.title)
        script_path = os.path.join(build_dir, f"{self.url_input}.py")

        cmd = [
            sys.executable,
            "-m",
            "PyInstaller",
            "--onefile",
            "--noconsole",
            "--distpath",
            build_dir,
            "--workpath",
            os.path.join(build_dir, "temp"),
            "--specpath",
            build_dir,
        ]

        if self.have_icon:
            cmd.extend(
                ["--icon", os.path.abspath(os.path.join(build_dir, "converted.ico"))]
            )
        else:
            cmd.extend(
                [
                    "--icon",
                    os.path.abspath(os.path.join(build_dir, "long-paper-roll.ico")),
                ]
            )

        cmd.append(script_path)

        print(Fore.YELLOW + "[LOGS:] " + Fore.RESET + "Building executable...")

        result = subprocess.run(cmd)

        if result.returncode == 0:
            print(Fore.GREEN + "[SUCCESS:] " + Fore.RESET + f"EXE saved in {build_dir}")
        else:
            print(Fore.RED + "[ERROR:] Build failed" + Fore.RESET)

        self.ask_shortcut = input(
            Fore.YELLOW
            + "[QUESTION:]"
            + Fore.RESET
            + "Would you like to add a shortcut ? (y/n): "
        )
        if self.ask_shortcut == "y":
            self.create_shortcut()
        elif self.ask_shortcut == "n":
            pass

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
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
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

        os.makedirs(f"builds/{self.title}", exist_ok=True)
        shutil.move(file_name, f"builds/{self.title}/{file_name}")

        if self.have_icon:
            shutil.move("converted.ico", f"builds/{self.title}/converted.ico")
        else:
            shutil.copy(
                "long-paper-roll.ico", f"builds/{self.title}/long-paper-roll.ico"
            )

        # ask the user to build the program
        self.ask_build = input(
            Fore.RED + "Would you like to build the Program?: " + Fore.RESET
        )
        if self.ask_build == "n" or self.ask_build == "no":
            print(
                Fore.YELLOW
                + "[SAVED:] "
                + Fore.RESET
                + f"Source saved at builds/{self.title}"
            )
        elif self.ask_build == "y" or self.ask_build == "yes":
            self.pyinstaller_build()
