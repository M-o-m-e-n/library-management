import csv

BOOKS_FILE = "books.csv"
BORROWED_FILE = "borrowed.csv"


class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:

    def __init__(self):
        self.books = []
        self.borrowed_books = []
        self.loadBooks()
        self.loadBorrowedBooks()

    def addBook(self, book):
        self.books.append(book)
        self.saveBooks()
        print(f"📚 Book '{book.title}' added successfully!")

    def displayBooks(self):
        available_books = [b for b in self.books if b.isbn not in self.borrowed_books]

        if not available_books:
            print("No available books.")
            return

        print("\n📖 Available Books:")
        for book in available_books:
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")

    def borrowBook(self, isbn, user):
        for book in self.books:
            if book.isbn == isbn and isbn not in self.borrowed_books:
                self.borrowed_books.append(isbn)
                self.saveBorrowedBooks(user, isbn)
                print(f"✅ '{book.title}' has been borrowed by {user}.")
                return
        
        print("❌ Book not available or already borrowed.")

    def returnBook(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            self.saveBorrowedBooks()
            print(f"🔄 Book with ISBN {isbn} has been returned.")
        else:
            print("❌ Book not found in borrowed records.")

    def displayBorrowedBooks(self):
        if not self.borrowed_books:
            print("No books are currently borrowed.")
            return

        print("\n📕 Borrowed Books:")
        with open(BORROWED_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                print(f"- {row[1]} (ISBN: {row[2]}) borrowed by {row[0]}")

    def saveBooks(self):
        try:
            with open(BOOKS_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "ISBN"])
                for book in self.books:
                    writer.writerow([book.title, book.author, book.isbn])
        except Exception as e:
            print(f"Error saving books: {e}")

    def saveBorrowedBooks(self, user=None, isbn=None):
        try:
            with open(BORROWED_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["User", "Book Title", "ISBN"])
                for borrowed_isbn in self.borrowed_books:
                    for book in self.books:
                        if book.isbn == borrowed_isbn:
                            writer.writerow([user, book.title, book.isbn])
        except Exception as e:
            print(f"Error saving borrowed books: {e}")

    def loadBooks(self):
        try:
            with open(BOOKS_FILE, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 3:
                        self.books.append(Book(row[0], row[1], row[2]))
        except FileNotFoundError:
            print("No existing book records found.")
        except Exception as e:
            print(f"Error loading books: {e}")

    def loadBorrowedBooks(self):
        try:
            with open(BORROWED_FILE, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 3:
                        self.borrowed_books.append(row[2])  # Store ISBN
        except FileNotFoundError:
            print("No borrowed records found.")
        except Exception as e:
            print(f"Error loading borrowed books: {e}")
