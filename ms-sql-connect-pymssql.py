# Brian Lesko
# This script does not successfully connect to the MS SQL database when tested on my machine.

import pymssql

server = '3JZDHW3\SQLEXPRESS'
user = 'lesko'
password = 'lesko'
database = 'master'


# Connect to the database
try: 
    conn = pymssql.connect(server,user,password,database)
except Exception as e: 
    print(e)

