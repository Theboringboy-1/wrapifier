import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon
from PIL import Image
import ctypes


# doc: giving the application their identity ,
## mainly for fixing the icon bug in windows.
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    "wrapifier.app.1"
)


# First argument <url> after main.py
url_to_build = sys.argv[1] if len(sys.argv) > 1 else "about:blank"

if not url_to_build.startswith(("http://", "https://")):
    url_to_build = "https://" + url_to_build
# Second argument <title> after <url>
title_window = sys.argv[2] if len(sys.argv) > 2 else "App"
# Third argument <icon> after <title>
icon_window = sys.argv[3] if len(sys.argv) > 3 else ""


# doc: Class initialized
class app_creator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(title_window)
        self.resize(1200, 800)
        
        img = Image.open(icon_window)

        # Converting to (.ico) for more stability.
        ico_path = "converted.ico"
        img.save(ico_path, format="ICO", sizes=[(256, 256)])

        icon = QIcon(ico_path)
        self.setWindowIcon(icon)

        # Browser
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.browser.setUrl(QUrl(url_to_build))

# doc: window manager
def main():
    app = QApplication(sys.argv)

    window = app_creator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
