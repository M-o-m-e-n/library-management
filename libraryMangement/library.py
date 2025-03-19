import csv

# Constant for the file name
BOOKS_FILE = "books.csv"


class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:

    def __init__(self):
        self.books = []
        self.loadBooks()

    def addBook(self, book):
        self.books.append(book)
        self.saveBooks()
        print(f"Book '{book.title}' added successfully!")

    def displayBooks(self):
        if not self.books:
            print("No books available.")
            return
        
        print("\n📚 Library Books:")
        for book in self.books:
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")

    def saveBooks(self):
        try:
            with open(BOOKS_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "ISBN"])  # Header
                for book in self.books:
                    writer.writerow([book.title, book.author, book.isbn])
        except Exception as e:
            print(f"Error saving books: {e}")

    def loadBooks(self):
        try:
            with open(BOOKS_FILE, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) == 3:
                        self.books.append(Book(row[0], row[1], row[2]))
        except FileNotFoundError:
            print("No existing book records found.")
        except Exception as e:
            print(f"Error loading books: {e}")
