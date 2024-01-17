# Brian Lesko
# This script connects to a Microsoft SQL Server database from python using the pyodbc library

import mysql.connector # ! pip install mysql-connector-python

mydb = mysql.connector.connect(
    host = '192.168.129.60', # to make the server accessible from more than just 'localhost' you must change the bind address in the config file
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

