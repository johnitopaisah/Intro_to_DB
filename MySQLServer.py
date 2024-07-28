import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='87628762',
    database='johnitopa'
)

if mydb.is_connected():
    print('Connected...')
    mycursor = mydb.cursor()

    create_books_table_query = """
        CREATE TABLE IF NOT EXISTS Books (
            book_id INT PRIMARY KEY,
            title VARCHAR(130),
            author_id,
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
            customer_id,
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
        )
    """


    mycursor.execute(query)
    mycursor.execute("SHOW TABLES")

    for table in mycursor:
        print(table)

    print("Done>>>>")

mycursor.close()
mydb.close()