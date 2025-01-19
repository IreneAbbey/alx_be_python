class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"The book '{title}' is not available.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        print(f"The book '{title}' does not belong to this library.")
        return False

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
