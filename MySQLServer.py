import mysql.connector
import Error

try:
    mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='87628762'
)

    if mydb.is_connected():
        mycursor = mydb.cursor()
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
        mycursor.execute(query)
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()