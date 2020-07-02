from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QToolBar, QAction, QPushButton, QVBoxLayout
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class mainApp(QMainWindow):
    def __init__(self):
        super(mainApp, self).__init__()
        self.resize(600, 400)
        self.mainUI()
        self.setCentralWidget(self.widget)

    def mainUI(self):
        self.pushButton = QPushButton("Camera")
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.pushButton.clicked.connect(self.showCamera)

    def showCamera(self):
        self.finder = QCameraViewfinder()
        self.finder.show()

        self.camera = QCamera()
        self.camera.setViewfinder(self.finder)
        self.camera.start()
        self.camera.stop()


if __name__ == "__main__":
    app = QApplication([])
    win = mainApp()
    win.show()
    app.exec_()
