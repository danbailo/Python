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

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

#envia as modificacoes de inserção para o banco
# mydb.commit()

print("Dados da tabela usando fetchall:")
mycursor.execute("SELECT * FROM customers;")
myresult = mycursor.fetchall()
#print(mycursor)
for row in myresult:
    print(row)    
print()



# mycursor.execute('INSERT INTO customers VALUES("Daniel", "Itibere 808", "NULL")')
# mycursor.execute("INSERT INTO customers VALUES(%s,%s,%s)",("Daniel", "Itibere 808",None))

# mydb.commit()

# inserindo multiplos valores

# sql = "INSERT INTO customers VALUES (%s, %s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4', None),
#   ('Amy', 'Apple st 652', None),
#   ('Hannah', 'Mountain 21', None),
#   ('Michael', 'Valley 345', None),
#   ('Sandy', 'Ocean blvd 2', None),
#   ('Betty', 'Green Grass 1', None),
#   ('Richard', 'Sky st 331', None),
#   ('Susan', 'One way 98', None),
#   ('Vicky', 'Yellow Garden 2', None),
#   ('Ben', 'Park Lane 38', None),
#   ('William', 'Central st 954', None),
#   ('Chuck', 'Main Road 989', None),
#   ('Viola', 'Sideway 1633', None)
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

#inserindo um valor e retornando seu id

# sql = "INSERT INTO customers VALUES (%s, %s, %s)"
# val = ("Michelle", "Blue Village", None)
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)


#selecionando colunas
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print()

mycursor.execute("SELECT * FROM customers WHERE id = 15")
myresult = mycursor.fetchone()
print(myresult)  
print()


sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)