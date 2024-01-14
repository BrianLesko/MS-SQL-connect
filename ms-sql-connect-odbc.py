# Brian Lesko
# This app connects to a Microsoft SQL Server database from python using the pyodbc library

import pyodbc

server = '3JZDHW3\SQLEXPRESS'
username = 'lesko'
password = 'lesko'
database = 'master'

# Connect to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                        SERVER='+server+';\
                        DATABASE='+database+';\
                        UID='+username+';\
                        PWD='+ password)

cursor = conn.cursor()

integer_variable = 1
query = "SELECT * FROM table_name WHERE printer = %d"
cursor.execute(query,integer_variable)
result = cursor.fetchall()
print(result)