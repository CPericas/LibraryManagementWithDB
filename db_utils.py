import mysql.connector
from mysql.connector import Error

def connect_database():
    """Connect to the MySQL database and return the connection object."""
    db_name = "library_management_system_db"
    user = "root"
    password = "$E@kster1"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        if conn.is_connected():
            print("Successfully connected to the database.")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None
