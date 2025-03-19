from library import Library, Book

def main():
    library = Library()

    while True:
        print("\n📖 Library Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Borrowed Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")

            book = Book(title, author, isbn)
            library.addBook(book)

        elif choice == "2":
            library.displayBooks()

        elif choice == "3":
            user = input("Enter your name: ")
            isbn = input("Enter ISBN of book to borrow: ")
            library.borrowBook(isbn, user)

        elif choice == "4":
            isbn = input("Enter ISBN of book to return: ")
            library.returnBook(isbn)

        elif choice == "5":
            library.displayBorrowedBooks()

        elif choice == "6":
            print("Exiting... 📚")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
