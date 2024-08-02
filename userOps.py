import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='library_management_system_db'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def add_user(connection):
    try:
        cursor = connection.cursor()
        name = input("Enter the user's name: ")
        library_id = input("Enter the user's library ID: ")
        
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (name, library_id))
        connection.commit()
        print("User added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def view_user_details(connection):
    try:
        cursor = connection.cursor()
        user_id = int(input("Enter the user's ID to view details: "))
        
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        
        if user:
            print(f"ID: {user[0]}")
            print(f"Name: {user[1]}")
            print(f"Library ID: {user[2]}")
        else:
            print("User not found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def display_all_users(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        
        if users:
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")
        else:
            print("No users found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
