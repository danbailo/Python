import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="daniel",
  passwd="123456789",
  database="MY_PYTHON_DB"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE MY_PYTHON_DB;")

print("Databases:")
mycursor.execute("SHOW DATABASES;")
for db in mycursor:
    print(db)
print()

#tabela ja criada
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")    

print("Tables:")
mycursor.execute("SHOW TABLES;")
for db in mycursor:
    print(db)
print()

print("Desc:")
mycursor.execute("DESC customers;")
#print(mycursor)
for db in mycursor:
    print(db)    
print()

#error, ja existe essa tabela
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")  

#adicionando uma primary key
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)