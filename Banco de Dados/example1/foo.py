#data for example
#https://github.com/datacharmer/test_db

import mysql.connector
from mysql.connector import errorcode

def connect(user=None, password=None, host=None, database=None):
    if user is None or password is None: return False
    if host and database: config = {'user': user,'password': password,'host': host,'database': database}
    elif host: config = {'user': user, 'password': password, 'host': host}
    else: config = {'user': user, 'password': password}
    # print(config)
    # print(len(config))
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        print(err)

def connect_database(cursor, database_name):
    try:
        cursor.execute("USE {}".format(database_name))
    except mysql.connector.Error as err:
        print(err)
        exit(1)        

def create_database(cursor, database_name):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def drop_database(cursor, database_name):
    try:
        cursor.execute("DROP DATABASE {}".format(database_name))
    except mysql.connector.Error as err:
        print("Failed delete database: {}".format(err))
        exit(1)

def close(connector,cursor):
    cursor.close()
    connector.close()

connector = connect('daniel','59228922ddd')
if connector: cursor = connector.cursor()
# print(cursor)
# print(connector)

# create_database(cursor,'python_test')
# drop_database(cursor,'python_test')
connect_database(cursor, 'TRABALHO_BD1')


close(connector, cursor)