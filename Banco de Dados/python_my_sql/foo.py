import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="daniel",
  passwd="59228922ddd"
)

print(mydb)