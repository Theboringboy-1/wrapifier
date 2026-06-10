import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView


class WhatsAppApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WhatsApp Desktop (PyQt6)")
        self.resize(1200, 800)

        # Browser
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Load WhatsApp Web
        self.browser.setUrl(QUrl("https://abdullmanan.xyz/"))

def main():
    app = QApplication(sys.argv)

    window = WhatsAppApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()