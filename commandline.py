import os, sys
from colorama import init, Fore, Back, Style
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
# colorama initializer:

init()


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

    def logic_checker(self, ok):
        self._valid = ok
        if ok:
            print("")  # gaps.
            print(Fore.YELLOW + "[LOGS:] " + Fore.RESET + "Website Found ...")
        else:
            print(Fore.RED + "[Error:] " + Fore.RESET + "Not a Valid Website")

        self.app.quit()

    # example check_valid:
    def check_valid(self):
        view = QWebEnginePage()
        view.loadFinished.connect(self.logic_checker)
        view.setUrl(QUrl(self.url_input))
        self.app.exec()

    def greeter(self):
        while True:
            self.url_input = input("Enter your URL : ")
            self.check_valid()
            if self._valid == True:
                break
            print(f"The URL {self.url_input} is invalid.")

        from builder import Builder

        Builder().build(self.url_input)

    def build_input(self):
        self.title = input("Enter the title of your app : ")
        self.icon_choice = input("Would you like to add an icon? (y/n) :")
        if self.icon_choice == "y":
            self.icon = input("Enter the path to ur icon : ")
        else:
            self.icon = self.default_icon


if __name__ == "__main__":
    startup = cmds()
    startup.pre_greeter()
