from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QToolBar, QAction
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl


class mainApp(QMainWindow):
    def __init__(self):
        super(mainApp, self).__init__()
        self.resize(600, 400)
        self.mainUI()
        self.setCentralWidget(self.video)

    def mainUI(self):
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.openTool = QAction("open", self)
        self.toolbar.addAction(self.openTool)
        self.openTool.triggered.connect(self.openDialog)

        self.player = QMediaPlayer()
        self.video = QVideoWidget()
        self.player.setVideoOutput(self.video)

    def openDialog(self):
        self.dialog = QFileDialog.getOpenFileName(
            self, "Open Video", 'c:\\', 'files(*.mp4)')
        if self.dialog[0] != '':
            self.player.setMedia(QMediaContent(QUrl(self.dialog[0])))
            self.player.play()
            self.player.setVolume(0)
            self.player.setPosition(60000)


if __name__ == "__main__":
    app = QApplication([])
    win = mainApp()
    win.show()
    app.exec_()
