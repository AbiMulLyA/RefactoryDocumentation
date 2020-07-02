from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('chinook.sqlite')
db.open()

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setTable()
        self.setLayout()
        self.setCentralWidget(self.widget)
        self.resize(600,400)
    
    def setTable(self):
        self.search = QLineEdit()
        self.search.textChanged.connect(self.setFilter)
        self.table = QTableView()
        self.model = QSqlRelationalTableModel(db=db)
        self.model.setTable('album')
        self.table.setModel(self.model)
        index = self.model.fieldIndex("Title")
        self.model.setSort(index, Qt.DescendingOrder)

        self.model.setRelation(2, QSqlRelation("artist", "ArtistId","Name"))
        
        self.model.select()

    def setLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.table)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)

    def setFilter(self, word):
        filterLastName = f'Name LIKE "%{word}%"'
        self.model.setFilter(filterLastName)
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()