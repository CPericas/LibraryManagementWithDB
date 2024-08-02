from db_utils import connect_database

def add_author(connection):
    """Add a new author to the database."""
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")

    try:
        cursor = connection.cursor()
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        cursor.execute(query, (name, biography))
        connection.commit()
        print("Author added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view_author_details(connection):
    """View details of a specific author."""
    author_id = input("Enter author ID: ")
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM authors WHERE id = %s"
        cursor.execute(query, (author_id,))
        result = cursor.fetchone()
        if result:
            print("Author Details:", result)
        else:
            print("No author found with the provided ID.")
    except Exception as e:
        print(f"Error: {e}")

def display_all_authors(connection):
    """Display all authors."""
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM authors"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            print("Authors List:")
            for row in results:
                print(row)
        else:
            print("No authors found.")
    except Exception as e:
        print(f"Error: {e}")
