# Brian Lesko
# This app connects to a Microsoft SQL Server database 

import pyodbc
import pandas as pd

# Connect to the database
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};Server=localhost\SQLEXPRESS;Database=master;User=sa;'
conn = pyodbc.connect(connectionString)