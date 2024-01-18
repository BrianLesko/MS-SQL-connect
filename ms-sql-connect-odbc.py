# Brian Lesko
# This app connects to a Microsoft SQL Server database from python using the pyodbc library

#https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver16&tabs=linux
import pyodbc

server = '192.168.129.2\SQLEXPRESS' # 192.168.129.2
username = 'lesko'
password = 'lesko'
database = 'PlatformDatabase'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;'
conn = pyodbc.connect(connectionString)

# Connect to the database
'''
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                        SERVER='+server+';\
                        DATABASE='+database+';\
                        UID='+username+';\
                        PWD='+ password)'''

cursor = conn.cursor()

integer_variable = 1
query = "SELECT * FROM Printers"
cursor.execute(query)
results = cursor.fetchall()
for result in results:
    print(result)