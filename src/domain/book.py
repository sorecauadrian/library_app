from src.domain.exceptions import ValidatorException

class Book:
    def __init__(self, book_id : int, title : str, author : str, times_rented : int = 0):
        self.__id = book_id
        self.__title = title
        self.__author = author
        self.__times_rented = times_rented

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.id == other.id

    def __str__(self):
        return str(self.id) + ": '" + self.title + "' by " + self.author

    def __repr__(self):
        return str(self)

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def times_rented(self):
        return self.__times_rented

    @title.setter
    def title(self, new_title : str):
        self.__title = new_title

    @author.setter
    def author(self, new_author : str):
        self.__author = new_author

    @times_rented.setter
    def times_rented(self, new_times_rented : int):
        self.__times_rented = new_times_rented

class BookValidator:
    def validate(self, book : Book):
        if not isinstance(book, Book):
            raise TypeError("can only validate book objects!")
        errors = []
        if len(book.title) < 3:
            errors.append("title must be at least 3 characters long!")
        if len(book.author) < 3:
            errors.append("author must be at least 3 characters long!")
        if len(errors) > 0:
            raise ValidatorException(errors)
        return True

