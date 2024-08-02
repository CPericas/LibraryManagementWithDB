from db_utils import connect_database
import authorsOps
import genreOps
import userOps
import bookOps

def genre_operations(connection):
    """Display genre management options and call the appropriate functions."""
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            genreOps.add_genre(connection)
        elif choice == '2':
            genreOps.view_genre_details(connection)
        elif choice == '3':
            genreOps.display_all_genres(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def author_operations(connection):
    """Display author management options and call the appropriate functions."""
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            authorsOps.add_author(connection)
        elif choice == '2':
            authorsOps.view_author_details(connection)
        elif choice == '3':
            authorsOps.display_all_authors(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def user_operations(connection):
    while True:
        print("\nUser Operations")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            userOps.add_user(connection)
        elif choice == '2':
            userOps.view_user_details(connection)
        elif choice == '3':
            userOps.display_all_users(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations(connection):
    while True:
        print("\nBook Operations")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            bookOps.add_book(connection)
        elif choice == '2':
            bookOps.borrow_book(connection)
        elif choice == '3':
            bookOps.return_book(connection)
        elif choice == '4':
            bookOps.search_book(connection)
        elif choice == '5':
            bookOps.display_all_books(connection)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """Display the main menu and handle user choices."""
    connection = connect_database()
    if connection is None:
        return

    while True:
        print("\nLibrary Management System")
        print("1. Genre Operations")
        print("2. Author Operations")
        print("3. User Operations")
        print("4. Book Operations")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            genre_operations(connection)
        elif choice == '2':
            author_operations(connection)
        elif choice == '3':
            user_operations(connection)
        elif choice == '4':
            book_operations(connection)
        elif choice == '5':
            connection.close()
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()



