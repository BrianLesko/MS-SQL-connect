# Brian Lesko
# This app connects to a Microsoft SQL Server database from python using the pyodbc library

#https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver16&tabs=linux
import pyodbc

server = '3JZDHW3\SQLEXPRESS'
username = 'lesko'
password = 'lesko'
database = 'master'

# Connect to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};\
                        SERVER='+server+';\
                        DATABASE='+database+';\
                        UID='+username+';\
                        PWD='+ password)

cursor = conn.cursor()

integer_variable = 1
# = "SELECT * FROM table_name WHERE printer = %d"
#cursor.execute(query,integer_variable)
#result = cursor.fetchall()
#print(result)