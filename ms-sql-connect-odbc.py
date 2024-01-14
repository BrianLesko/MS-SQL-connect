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

query = "SELECT * FROM MSreplication_option"
conn.close
#cursor.execute(query)