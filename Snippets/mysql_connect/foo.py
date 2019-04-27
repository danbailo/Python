import mysql.connector
from xlwt import Workbook
from mysql.connector import Error

try:
    MySQLconnect = mysql.connector.connect(
        host='localhost',
        user='daniel', password='123456789',
        database='TRABALHO_BD1'
        )
    if MySQLconnect.is_connected():
        print("\nCONNECTED SUCCESSFULLY TO MySQL DATABASE")
        
        MySQLcursor = MySQLconnect.cursor()
        MySQLcursor.execute("SELECT * FROM VENDEDOR;")

        columnName = MySQLcursor.column_names
        tableValues = MySQLcursor.fetchall()

        print("\nDATA RETRIEVED SUCCESSFULLY FROM MySQL DATABASE")

        workBook = Workbook()
        workSheet = workBook.add_sheet("Sheet No 1")

        for i in range(len(columnName)):
            workSheet.write(0, i, columnName[i])

        for r, row in enumerate(tableValues):
            for c, col in enumerate(row):
                workSheet.write(r+1, c, col)

        workBook.save("./MySQL.xls")

        print("\nDATA WRITTEN SUCCESSFULLY TO EXCEL FILE")

except Error as e:
    print("\nERROR", e)
    
finally:
    if (MySQLconnect.is_connected()):
        MySQLcursor.close()
        MySQLconnect.close()
        print("\nMySQL CONNECTION CLOSED")  
    