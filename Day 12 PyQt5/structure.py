# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        self.label = Labels()
        self.mainWidget()
        self.setLayout()
        self.setWidget()

    def mainWidget(self):
        # object combobox
        self.comboBox = QComboBox()
        self.comboBox.addItem("satu")    
        self.comboBox.addItem("dua")    
        self.comboBox.addItem("tiga")    
        self.comboBox.addItem("empat")

        # object checkbox
        self.checkBox = QCheckBox("Memasak")
        self.checkBox.setChecked(False)
        self.checkBox2 = QCheckBox("Menari")
        self.checkBox2.setChecked(False)

        # object RadioButton
        self.radioButton = QRadioButton("female")
        self.radioButton = QRadioButton("male")

    def setLayout(self):
        # object layout 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label.addLabel("test"))
        self.layout.addWidget(self.label.addLabel("fmlkgl"))
        self.layout.addWidget(self.label.addLabel("ngierng"))
        self.layout.addWidget(self.label.addLabel("ejinge"))
        self.layout.addWidget(checkBoxs("test class").addCheckBox)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.checkBox)
        self.layout.addWidget(self.checkBox2)
        self.layout.addWidget(self.radioButton)

    def setWidget(self):
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        # set "object widget" to centralWidget of mainWindow()
        # centralWidget() hanya menerima satu widget
        self.setCentralWidget(self.widget)


class checkBoxs():
    def __init__(self, text):
        self.addCheckBox = QCheckBox(text)

class Labels():
    def addLabel(self, text):
        self.label = QLabel(text)
        return self.label

if __name__ == "__main__":
    app = QApplication([])
    window = WindowApp()
    window.show()
    app.exec_()