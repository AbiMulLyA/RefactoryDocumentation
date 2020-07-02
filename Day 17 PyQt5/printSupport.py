import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QLabel, QVBoxLayout, QWidget, QPushButton, QDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QAbstractPrintDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.textArea = QTextEdit()
        self.button = QPushButton("print")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textArea)
        self.layout.addWidget(self.button)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.button.clicked.connect(self.print)

    def print(self):
        self.printer = QPrinter()
        self.dialog = QPrintDialog(self.printer)
        # self.dialog.exec_()
        if self.dialog.exec_() == QDialog.Accepted:
            self.textArea.document().print_(self.printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
