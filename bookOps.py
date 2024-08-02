from db_utils import connect_database

def add_book(connection):
    try:
        cursor = connection.cursor()
        title = input("Enter the book title: ")
        author_id = int(input("Enter the author ID: "))
        genre_id = int(input("Enter the genre ID: "))
        isbn = input("Enter the book ISBN: ")
        publication_date = input("Enter the publication date (YYYY-MM-DD): ")

        query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (title, author_id, genre_id, isbn, publication_date))
        connection.commit()
        print("Book added successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def borrow_book(connection):
    try:
        cursor = connection.cursor()
        book_id = int(input("Enter the book ID to borrow: "))
        user_id = int(input("Enter the user ID borrowing the book: "))
        borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")

        # Check if the book is available
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()
        
        if result and result[0]:
            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, book_id, borrow_date))
            
            # Update book availability
            cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
            connection.commit()
            print("Book borrowed successfully.")
        else:
            print("Book is not available.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def return_book(connection):
    try:
        cursor = connection.cursor()
        book_id = int(input("Enter the book ID to return: "))
        user_id = int(input("Enter the user ID returning the book: "))
        return_date = input("Enter the return date (YYYY-MM-DD): ")

        # Check if the book is currently borrowed
        cursor.execute("SELECT id FROM borrowed_books WHERE book_id = %s AND user_id = %s AND return_date IS NULL", (book_id, user_id))
        result = cursor.fetchone()
        
        if result:
            query = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND user_id = %s AND return_date IS NULL"
            cursor.execute(query, (return_date, book_id, user_id))
            
            # Update book availability
            cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
            connection.commit()
            print("Book returned successfully.")
        else:
            print("No record of this book being borrowed by the user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def search_book(connection):
    try:
        cursor = connection.cursor()
        search_term = input("Enter title or ISBN to search: ")
        
        query = "SELECT * FROM books WHERE title LIKE %s OR isbn = %s"
        cursor.execute(query, ('%' + search_term + '%', search_term))
        books = cursor.fetchall()
        
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Genre ID: {book[3]}, ISBN: {book[4]}, Publication Date: {book[5]}, Available: {book[6]}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def display_all_books(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        books = cursor.fetchall()
        
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Genre ID: {book[3]}, ISBN: {book[4]}, Publication Date: {book[5]}, Available: {book[6]}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()