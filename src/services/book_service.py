from src.domain.book import Book, BookValidator
from src.repository.book_repository import BookRepository
from src.services.rental_service import RentalService


class BookService:
    def __init__(self, validator = None, repository = None, rental_service = None):
        if validator is None:
            validator = BookValidator()
        if repository is None:
            repository = BookRepository(self.list_of_books())
        if rental_service is None:
            rental_service = RentalService()
        self.__validator = validator
        self.__repository = repository
        self.__rental_service = rental_service

    def store(self, bookId : int, title : str, author : str):
        book = Book(bookId, title, author)
        self.__validator.validate(book)
        self.__repository.store(book)
        return book

    def delete(self, bookId : str):
        self.__repository.delete(bookId)

    def update(self, bookId : int, title : str, author : str):
        book = Book(bookId, title, author)
        self.__validator.validate(book)
        self.__repository.update(book)
        return book

    def get_all(self):
        return self.__repository.get_all()

    def find_by_id(self, bookId : int):
        return self.__repository.find_by_id(bookId)

    def find_by_title(self, title: str):
        return self.__repository.find_by_title(title)

    def find_by_author(self, author: str):
        return self.__repository.find_by_author(author)

    @staticmethod
    def list_of_books():
        return [Book(1, "el hombre", "huxley"),
                Book(2, "the eternal husband", "dostoevski"),
                Book(3, "great new world", "huxley"),
                Book(4, "karamazov brothers", "dostoevski"),
                Book(5, "the idiot", "dostoevski"),
                Book(6, "island", "huxley"),
                Book(7, "1984", "orwell"),
                Book(8, "animal farm", "orwell"),
                Book(9, "the invisible man", "wells"),
                Book(10, "time machine", "wells")]

