import sys
from PyQt5.QtCore import *              #pip install PyQt5
from PyQt5.QtWidgets import *      
from PyQt5.QtWebEngineWidgets import *  #pip install PyQtWebEngine
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://localhost:5000'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        l1 = QLabel()
        l1.setText("http://localhost:5000")
        l1.setAlignment(Qt.AlignCenter)
        navbar.addWidget(l1)
      

proc=subprocess.Popen(["python","app.py"])
app = QApplication(sys.argv)
QApplication.setApplicationName('CHATBOT APPLICATION')
window = MainWindow()
app.exec_()