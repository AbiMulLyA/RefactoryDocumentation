from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QToolBar, QAction
from PyQt5.QtGui import QIcon
import sys


class myApp(QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.mainUI()
        self.mainLayout()
        self.setCentralWidget(self.mainWidget)
        self.menuBars()
        self.setMenuBar(self.menu)
        self.toolBars()
        self.addToolBar(self.toolBar)

    def mainUI(self):
        self.firstTab = firstTab()
        self.secondTab = secondTab()
        self.tabs = QTabWidget()
        self.tabs.addTab(self.firstTab, "firstTab")
        self.tabs.addTab(self.secondTab, "secondTab")

    def toolBars(self):
        self.toolBar = QToolBar()
        button_toolBar = QAction(QIcon("icon/boy.png"),"test",self)
        self.toolBar.addAction(button_toolBar)
        button_toolBar.triggered.connect(self.toolPrint)

    def toolPrint(self):
        print("clicked!")
        
    def menuBars(self):
        self.menu = self.menuBar()
        test = self.menu.addMenu("About")
        test.addAction("help")
        test.setToolTip("this is help")

    def mainLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabs)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)

class firstTab(QWidget):
    def __init__(self):
        super(firstTab, self).__init__()
        self.mainUI()
        self.setLayout(self.layout)

    def mainUI(self):
        self.pButton = QPushButton("first tab button")
        self.pButton2 = QPushButton("first tab button")
        self.pButton3 = QPushButton("first tab button")
        self.pButton4 = QPushButton("first tab button")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pButton)
        self.layout.addWidget(self.pButton2)
        self.layout.addWidget(self.pButton3)
        self.layout.addWidget(self.pButton4)

class secondTab(QWidget):
    def __init__(self):
        super(secondTab, self).__init__()

if __name__ == "__main__":
    app = QApplication([])
    window = myApp()
    window.show()
    sys.exit(app.exec_())