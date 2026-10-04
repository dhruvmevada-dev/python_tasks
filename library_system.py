class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        if any(b.isbn == isbn for b in self.books):
            print(f"A book with ISBN {isbn} already exists.")
            return
        self.books.append(Book(title, author, isbn))
        print(f"Added: {title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book.title}")
                return
        print("Book not found.")

    def search_by_title(self, query):
        """Case-insensitive partial match on title."""
        return [b for b in self.books if query.lower() in b.title.lower()]

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        for b in self.books:
            print(b)


if __name__ == "__main__":
    lib = Library()
    lib.add_book("Clean Code", "Robert C. Martin", "111")
    lib.add_book("The Pragmatic Programmer", "Andrew Hunt", "222")
    lib.add_book("Python Crash Course", "Eric Matthes", "333")

    print("\nAll books:")
    lib.list_books()

    print("\nSearch 'python':")
    for b in lib.search_by_title("python"):
        print(b)

    print("\nRemoving ISBN 222:")
    lib.remove_book("222")

    print("\nAfter removal:")
    lib.list_books()
