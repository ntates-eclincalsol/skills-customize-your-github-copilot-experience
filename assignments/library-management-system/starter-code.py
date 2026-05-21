class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __repr__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"


class Patron:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __repr__(self):
        return f"Patron(name={self.name}, id={self.member_id})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, isbn: str, patron: Patron):
        book = self.find_book(isbn)
        if not book:
            raise ValueError("Book not found")
        if not book.available:
            raise ValueError("Book is currently unavailable")

        book.available = False
        patron.borrow_book(book)
        return book

    def return_book(self, isbn: str, patron: Patron):
        book = self.find_book(isbn)
        if not book:
            raise ValueError("Book not found")
        if book not in patron.borrowed_books:
            raise ValueError("This patron did not borrow this book")

        book.available = True
        patron.return_book(book)
        return book

    def list_books(self):
        return self.books


if __name__ == "__main__":
    library = Library()

    book1 = Book("The Wind in the Willows", "Kenneth Grahame", "978-0141321130")
    book2 = Book("A Wrinkle in Time", "Madeleine L'Engle", "978-0312367541")

    library.add_book(book1)
    library.add_book(book2)

    patron1 = Patron("Avery", 101)
    patron2 = Patron("Jordan", 102)

    print("Library inventory:")
    print(library.list_books())

    print("\nBorrowing a book:")
    library.borrow_book("978-0141321130", patron1)
    print(book1)
    print(patron1.borrowed_books)

    print("\nReturning a book:")
    library.return_book("978-0141321130", patron1)
    print(book1)
    print(patron1.borrowed_books)
