# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class WindowApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowApp, self).__init__(*args, **kwargs)
        # show label 1
        self.label = QLabel()
        self.label.setText("Set Text Text")
        self.label.setAlignment(Qt.AlignCenter)
        
        # show label 2
        self.label2 = QLabel("Test")
        self.label2.setAlignment(Qt.AlignRight)

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
        # self.radioButton = QRadioButton("female")
        # self.radioButton = QRadioButton("male")
        
        # object layout 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.checkBox)
        self.layout.addWidget(self.checkBox2)
        self.layout.addWidget(self.radioButton)
        
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.radioButton = QRadioButton("female")
        self.radioButton = QRadioButton("male")
        
        # set "object widget" to centralWidget of mainWindow()
        # centralWidget() hanya menerima satu widget
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication([])
    window = WindowApp()
    window.show()
    app.exec_()