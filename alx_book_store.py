import mysql.connector
from mysql.connector import Error

try:
    mydb = connect(
        host='localhost',
        user='root',
        passwd='876287'
    )
except Error as e:
    print("An Error occur while try to connect: {e}")