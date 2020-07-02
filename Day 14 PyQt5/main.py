from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QDialog, QInputDialog, QDialogButtonBox, QSlider, QProgressBar
from PyQt5.QtCore import Qt


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.data = ["makan","minum","sekolah"]
        self.mainUI()
        self.setLayout()
        self.setCentralWidget(self.setWidget)

    def mainUI(self):
        self.list = QListWidget()
        self.list.addItems(self.data)

        self.buttonAdd = QPushButton("Add")
        self.buttonRemove = QPushButton("Remove")
        self.buttonDialog = QPushButton("Open Dialog Box")
        self.buttonInputDialog = QPushButton("Open Input Dialog")
        self.buttonDialog.clicked.connect(self.setDialog)
        self.buttonInputDialog.clicked.connect(self.setInputDialog)

    def setLayout(self):
        self.layoutList = QVBoxLayout()
        self.layoutList.addWidget(self.list)
        self.layoutList.addWidget(self.buttonAdd)
        self.layoutList.addWidget(self.buttonRemove)
        self.layoutList.addWidget(self.buttonDialog)
        self.layoutList.addWidget(self.buttonInputDialog)

        self.setWidget = QWidget()
        self.setWidget.setLayout(self.layoutList)

    def setDialog(self):
        self.dialog = QDialog()
        self.dialog.setFixedSize(300,200)
        self.dialog.setWindowTitle("Custom Dialog Box")

        self.labelDialog = QLabel("custom label")
        self.button = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(self.button)
        self.buttonBox.accepted.connect(self.dialog.accept)
        
        self.layoutDialog = QVBoxLayout()
        self.layoutDialog.addWidget(self.labelDialog)
        self.layoutDialog.addWidget(self.buttonBox)

        self.dialog.setLayout(self.layoutDialog)
        self.dialog.exec_()

    def setInputDialog(self):
        self.inputDialog, ok = QInputDialog.getText(self, "Input Dialog 1", "add list item")
        print(f"cek input dialog : {self.inputDialog}")
        print(ok)        
    
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.mainUI()
        self.setLayout()
        self.setCentralWidget(self.widget)
        self.setWindowTitle("example slider")
        self.setFixedSize(400,300)

    def mainUI(self):
        self.slider = QSlider()
        self.progressBar = QProgressBar()
        self.progressBar.setValue(30)

    def setLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.progressBar)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()