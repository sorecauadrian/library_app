from src.repository.exceptions import RepositoryException

class BookRepository:
    def __init__(self, list_of_books : list = None):
        if list_of_books is None:
            list_of_books = []
        self.__books = list_of_books

    def store(self, book):
        if self.find_by_id(book.id) is not None:
            raise RepositoryException("book with id " + str(book.id) + " already in repository!")
        self.__books.append(book)

    def find_by_id(self, bookId : int):
        for book in self.__books:
            if bookId == book.id:
                return book
        return None

    def find_by_title(self, title : str):
        books = []
        for book in self.__books:
            if title in book.title:
                books.append(book)
        return books

    def find_by_author(self, author : str):
        books = []
        for book in self.__books:
            if author in book.author:
                books.append(book)
        return books

    def update(self, book):
        updatedBook = self.find_by_id(book.id)
        if updatedBook is None:
            raise RepositoryException("book not found!")
        indexOfBook = self.__books.index(updatedBook)
        self.__books.remove(updatedBook)
        self.__books.insert(indexOfBook, book)

    def delete(self, bookId : str):
        if bookId.isdigit is False:
            raise TypeError("the id is not an integer!")
        bookId = int(bookId)
        book = self.find_by_id(bookId)
        if book is None:
            raise RepositoryException("book not found!")
        self.__books.remove(book)
        return book

    def get_all(self):
        return self.__books

    def __len__(self):
        return len(self.__books)

    def __str__(self):
        result = ""
        for book in self.__books:
            result += str(book)
            result += "\n"
        return result
