import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon

# First argument <url> after main.py
url_to_build = sys.argv[1] if len(sys.argv) > 1 else "about:blank"
# Second argument <title> after <url>
title_window = sys.argv[2] if len(sys.argv) > 2 else "App"
# Third argument <icon> after <title>
icon_window = sys.argv[3] if len(sys.argv) > 3 else ""


class app_creator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(title_window)
        self.resize(1200, 800)
        self.setWindowIcon(QIcon(icon_window))

        # Browser
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.browser.setUrl(QUrl(url_to_build))


def main():
    app = QApplication(sys.argv)

    window = app_creator()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
