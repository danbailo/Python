import mysql.connector
from mysql.connector import errorcode

def connect(user=None, password=None, host=None, database=None):
    
    if {user, password, host, database}&{None}: return False

    try:
        cnx = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
        )
    except mysql.connector.Error as err:
        print(err)

def close(connector):
    connector.close() 

print(not connect())