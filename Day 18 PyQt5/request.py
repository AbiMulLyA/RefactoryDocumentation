from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QUrl, QByteArray
import json


class mainApp():

    def getRequest(self):
        url = QUrl("https://jsonplaceholder.typicode.com/users/1")

        self.request = QNetworkRequest(url)

        self.manager = QNetworkAccessManager()
        self.manager.get(self.request)
        self.manager.finished.connect(self.getResponse)

    def postRequest(self):
        url = QUrl("http://httpbin.org/post")

        dataDict = {}
        dataDict["fname"] = "Budi"
        dataDict["lname"] = "Anton"

        dataJson = json.dumps(dataDict)

        data = QByteArray()
        data.append(dataJson)

        self.request = QNetworkRequest(url)
        self.request.setHeader(QNetworkRequest.ContentTypeHeader,"application/json")

        self.manager = QNetworkAccessManager()
        self.manager.post(self.request, data)
        self.manager.finished.connect(self.getResponse)

    def getResponse(self, reply):
        self.result = reply.readAll()
        print(str(self.result, "utf-8"))

        QApplication.quit()

if __name__ == "__main__":
    app = QApplication([])
    win = mainApp()
    # win.getRequest()
    win.postRequest()
    app.exec_()
