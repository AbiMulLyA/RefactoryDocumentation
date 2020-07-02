# import mysql.connector as mysql
# config = {
#   "host" : "127.0.0.1",
#   "port" : "3306",
#   "user" : "root",
#   "password" : "",
#   'database' : "mdd"
# }

# connect = mysql.connect(**config)
# cursor = connect.cursor()
# #$nampilin db

# query_database = "create database mdd"
# cursor.execute(query_database)

# query="show databases"
# cursor.execute(query)
# for db in cursor:
#   print(db)

# query = "create table user (id INT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10,2))"
# test = cursor.execute(query)

# show = "show tables"
# test2 = cursor.execute(show)
# for a in cursor:
#   print(a)
import mysql.connector as db
config ={
	'host': 'localhost',
	'port': '3306',
	'user': 'root',
	'password': '',
	'database': 'mdd_training'
}
conn = db.connect(**config)
if conn:
	print('Koneksi Berhasil')
cursor = conn.cursor()
# Show database
# cursor.execute("show databases")
# for database in cursor:
# 	print(database)
# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS mdd_training")
# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS peserta (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(100), alamat VARCHAR(255))")
# cursor.execute("ALTER TABLE peserta AUTO_INCREMENT = id")
cursor.execute("SHOW TABLES")
for table in cursor:
	print(table)
# Insert data
query = "INSERT INTO peserta (nama,alamat) VALUES (%s,%s)"
value = [
("Abi Mulya","Depok Citayam"),
("Wahyu","Tangerang Cingkareng")
]
# cursor.execute(query, value) # input tunggal
# cursor.executemany(query, value) # Input multiply
conn.commit()
print(cursor.rowcount, "Record")
print("Record ID", cursor.lastrowid)
select = cursor.execute("SELECT * FROM peserta")
get = cursor.fetchall() # get semua data
get1 = cursor.fetchone() # get 1 data
for data in get:
	print(data)
where = "SELECT * FROM peserta WHERE alamat = %s"
value = ("Depok Citayam",)
cursor.execute(where, value)
get = cursor.fetchall()
for x in get:
	print(x)