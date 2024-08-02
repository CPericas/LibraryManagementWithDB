from db_utils import connect_database

def add_genre(connection):
    """Add a new genre to the database."""
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")

    try:
        cursor = connection.cursor()
        query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, description, category))
        connection.commit()
        print("Genre added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view_genre_details(connection):
    """View details of a specific genre."""
    genre_id = input("Enter genre ID: ")
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM genres WHERE id = %s"
        cursor.execute(query, (genre_id,))
        result = cursor.fetchone()
        if result:
            print("Genre Details:", result)
        else:
            print("No genre found with the provided ID.")
    except Exception as e:
        print(f"Error: {e}")

def display_all_genres(connection):
    """Display all genres."""
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM genres"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            print("Genres List:")
            for row in results:
                print(row)
        else:
            print("No genres found.")
    except Exception as e:
        print(f"Error: {e}")

