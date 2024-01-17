# Brian Lesko
# This script connects to a Microsoft SQL Server database from python using the pyodbc library

import mysql.connector # ! pip install mysql-connector-python

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'lesko',
    password = 'lesko',
    database = 'test_db'
) 

cursor = mydb.cursor()

table_name = 'coffee_table'
cursor.execute("SELECT * FROM {table_name}")

results = cursor.fetchall()

for result in results:
    print(result)

