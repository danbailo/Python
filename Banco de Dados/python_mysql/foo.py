import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="daniel",
  passwd="123456789"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE MY_PYTHON_DB;")
mycursor.execute("SHOW DATABASES;")

for db in mycursor:
    print(db)