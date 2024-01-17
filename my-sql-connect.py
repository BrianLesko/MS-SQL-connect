import mysql.connector

mydb = mysql.connector.connect(
    host = '192.168.129.60', # to make the server accessible from more than just 'localhost' you must change the bind address in the config file
    user = 'lesko',
    password = 'lesko',
    database = 'test_db'
) 

cursor = mydb.cursor()

cursor.execute("SELECT * FROM coffee_table")

results = cursor.fetchall()

for result in results:
    print(result)