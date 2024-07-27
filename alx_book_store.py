import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='87628762'
)

if mydb.is_connected():
    print('Connected...')
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")
    for row in mycursor:
        print(row)

mydb.close()