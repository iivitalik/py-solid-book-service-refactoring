from models import Book


class BookRepository:
    def __init__(self):
        self.books = []

    def add(self, book: Book) -> None:
        self.books.append(book)

    def get_all(self) -> list[Book]:
        return self.books