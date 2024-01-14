# Brian Lesko 
# 

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

