#!/usr/bin/env python3

import mysql.connector
import sys

# Check if a database name argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <database_name>")
    sys.exit(1)

database_name = sys.argv[1]

# Connect to MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='87628762',
)

if mydb.is_connected():
    print('Connected to MySQL server...')
    mycursor = mydb.cursor()

    # Create the database if it does not exist
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")

    # Use the specified database
    mycursor.execute(f"USE {database_name};")

    # Define table creation queries
    create_books_table_query = """
        CREATE TABLE IF NOT EXISTS Books (
            book_id INT PRIMARY KEY,
            title VARCHAR(130),
            author_id INT,
            price DOUBLE,
            publication_date DATE,
            FOREIGN KEY (author_id) REFERENCES Authors(author_id)
        );
    """

    create_authors_table_query = """
        CREATE TABLE IF NOT EXISTS Authors (
            author_id INT PRIMARY KEY,
            author_name VARCHAR(215)
        );
    """

    create_customers_table_query = """
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(215),
            email VARCHAR(215),
            address TEXT
        );
    """

    create_orders_table_query = """
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INT PRIMARY KEY,
            customer_id INT,
            order_date DATE,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        );
    """

    create_order_details_table_query = """
        CREATE TABLE IF NOT EXISTS Order_Details (
            order_details_id INT PRIMARY KEY,
            order_id INT,
            book_id INT,
            quantity DOUBLE,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id),
            FOREIGN KEY (book_id) REFERENCES Books(book_id)
        );
    """

    # Execute table creation queries
    mycursor.execute(create_authors_table_query)
    mycursor.execute(create_customers_table_query)
    mycursor.execute(create_orders_table_query)
    mycursor.execute(create_books_table_query)
    mycursor.execute(create_order_details_table_query)

    # Show tables to verify creation
    mycursor.execute("SHOW TABLES;")
    
    for table in mycursor:
        print(table)

    print("Done>>>")

# Close the cursor and connection
mycursor.close()
mydb.close()
