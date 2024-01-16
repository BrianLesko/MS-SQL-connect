import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'lesko',
    password = 'lesko',
    database = 'test_db'
) 

cursor = mydb.cursor()

cursor.execute("SELECT * FROM coffee_table")

results = cursor.fetchall()

for result in results:
    print(result)