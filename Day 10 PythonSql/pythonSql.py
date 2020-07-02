import mysql.connector as mysql
import click
class pythonSql():
  def __init__ (self):
    config = {
      "host" : "localhost",
      "port" : "3306",
      "user" : "root",
      "password" : "",
      "database" : "python_sql"
      }
    self.connect = mysql.connect(**config)
    self.cursor = self.connect.cursor()
    # cursor.execute("show databases")
    # # for databases in cursor:
    # #   print(databases)
  def create_db(self):
    self.cursor.execute("CREATE DATABASE IF NOT EXISTS python_sql")
    self.cursor.execute("CREATE TABLE IF NOT EXISTS todo_list(id INT PRIMARY KEY, activity VARCHAR(100), status INT)")
    query = "INSERT INTO todo_list(id, activity, status) VALUES(%s,%s,%s)"
    value = [
      ("4","Jogging jam 5:00 WIB","1"),
      ("5","Makan di Warteg Bu Ita","0"),
      ("15","Nge-gym di Celfit", "1"),
      ("19","Pergi ambil kue di Cizz Cake","0")
    ]
    # self.cursor.executemany(query, value)
    self.connect.commit()
    # self.cursor.execute("SHOW TABLES")
    # for data in self.cursor:
    #   print(data)
  @click.group()    
  def pythonSqlGroup():
    """Welcome to the App"""
  @pythonSqlGroup.command("list")
  def show_db(self):
    select_cursor = self.cursor.execute("SELECT * FROM todo_list")
    for data in self.cursor:
      if data[2] == 1:
        status = "(DONE)"
      else:
        status = ""
    print(data[0],".",data[1],status)
# test = pythonSql()
# test.create_db()
if __name__ == "__main__":
    test = pythonSql()
    test.pythonSqlGroup()