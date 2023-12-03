from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from datetime import date, timedelta

class UI:
    def __init__(self, bookService : BookService = None, clientService : ClientService = None, rentalService : RentalService = None):
        if bookService is None:
            bookService = BookService()
        if clientService is None:
            clientService = ClientService()
        if rentalService is None:
            rentalService = RentalService()
        self.__book_service = bookService
        self.__client_service = clientService
        self.__rental_service = rentalService

    def ui_add_book(self):
        try:
            id = int(input("input the id of the book: "))
            title = input("input the title of the book: ")
            author = input("input the author of the book: ")
            self.__book_service.store(id, title, author)
            print("book successfully added!")
        except Exception as e:
            print(e)

    def ui_add_client(self):
        try:
            id = int(input("input the id of the client: "))
            name = input("input the name of the client: ")
            self.__client_service.store(id, name)
            print("client successfully added!")
        except Exception as e:
            print(e)

    def ui_remove_book(self):
        try:
            id = input("input the id of the book: ")
            self.__book_service.delete(id)
            print("book successfully deleted")
        except Exception as e:
            print(e)

    def ui_remove_client(self):
        try:
            id = input("input the id of the client: ")
            self.__client_service.delete(id)
            print("client successfully deleted")
        except Exception as e:
            print(e)

    def ui_update_book(self):
        try:
            id = int(input("input the id of the book: "))
            title = input("input the new title of the book: ")
            author = input("input the new author of the book: ")
            self.__book_service.update(id, title, author)
            print("book successfully updated!")
        except Exception as e:
            print(e)

    def ui_update_client(self):
        try:
            id = int(input("input the id of the client: "))
            name = input("input the new name of the client: ")
            self.__client_service.update(id, name)
            print("client successfully updated!")
        except Exception as e:
            print(e)

    def ui_list_books(self):
        if self.__book_service.get_all() is []:
            print("there are no books yet!")
        for book in self.__book_service.get_all():
            print(book)

    def ui_list_clients(self):
        if self.__client_service.get_all() is []:
            print("there are no clients yet!")
        for client in self.__client_service.get_all():
            print(client)

    def ui_rent_a_book(self):
        try:
            id = int(input("input the id of the rent: "))
            bookId = int(input("input the id of the book: "))
            clientId = int(input("input the id of the client: "))
            if self.__rental_service.book_is_available(self.__book_service.find_by_id(bookId), date.today(), date.today() - timedelta(days=1)) is True:
                self.__rental_service.create(id, bookId, clientId, date.today(), date.today() - timedelta(days=1))
            print("book successfully rented!")
        except Exception as e:
            print(e)

    def ui_return_a_book(self):
        try:
            bookId = int(input("input the id of the book: "))
            clientId = int(input("input the id of the client: "))
            self.__rental_service.return_a_book(bookId, clientId)
            print("book successfully returned!")
        except Exception as e:
            print(e)

    def ui_find_book_by_id(self):
        id = int(input("input the id of the book: "))
        print(self.__book_service.find_by_id(id))

    def ui_find_books_by_title(self):
        title = input("input the title of the book: ")
        for book in self.__book_service.find_by_title(title):
            print(book)

    def ui_find_book_by_author(self):
        author = input("input the author of the book: ")
        for book in self.__book_service.find_by_author(author):
            print(book)

    def ui_find_client_by_id(self):
        id = int(input("input the id of the client: "))
        print(self.__client_service.find_by_id(id))

    def ui_find_clients_by_name(self):
        name = input("input the name of the client: ")
        for client in self.__client_service.find_by_name(name):
            print(client)

    def ui_most_rented_books(self):
        for book in self.__book_service.get_all():
            book.times_rented = 0

        for rental in self.__rental_service.get_all():
            book = self.__book_service.find_by_id(rental.book_id)
            book.times_rented += 1

        books = []
        for book in self.__book_service.get_all():
            if book.times_rented > 0:
                books.append(book)

        books.sort(key = lambda book_object: book_object.times_rented, reverse=True)

        for book in books:
            print(book)

    def ui_most_active_clients(self):
        for client in self.__client_service.get_all():
            client.days_of_rental = 0

        for rental in self.__rental_service.get_all():
            client = self.__client_service.find_by_id(rental.client_id)
            client.days_of_rental += (rental.returned_date - rental.rented_date).days

        clients = []
        for client in self.__client_service.get_all():
            if client.days_of_rental > 0:
                clients.append(client)

        clients.sort(key=lambda client_object: client_object.days_of_rental, reverse=True)

        for client in clients:
            print(client)

    def ui_most_rented_author(self):
        for book in self.__book_service.get_all():
            book.times_rented = 0

        for rental in self.__rental_service.get_all():
            book = self.__book_service.find_by_id(rental.book_id)
            book.times_rented += 1

        authors = []
        for book in self.__book_service.get_all():
            if book.times_rented > 0:
                if book.author not in authors:
                    authors.append(book.author)

        for author in authors:
            print(author)

    def ui_manage_clients_and_books(self):
        self.submenu1()
        choice = input("> ")
        if choice == "1":
            self.ui_add_book()
        elif choice == "2":
            self.ui_add_client()
        elif choice == "3":
            self.ui_remove_book()
        elif choice == "4":
            self.ui_remove_client()
        elif choice == "5":
            self.ui_update_book()
        elif choice == "6":
            self.ui_update_client()
        elif choice == "7":
            self.ui_list_books()
        elif choice == "8":
            self.ui_list_clients()
        elif choice == "0":
            pass
        else:
            print("invalid choice!")

    def ui_rent_or_return(self):
        self.submenu2()
        choice = input("> ")
        if choice == "1":
            self.ui_rent_a_book()
        elif choice == "2":
            self.ui_return_a_book()
        elif choice == "0":
            pass
        else:
            print("invalid choice!")

    def ui_search(self):
        self.submenu3()
        choice = input("> ")
        if choice == "1":
            self.ui_find_book_by_id()
        elif choice == "2":
            self.ui_find_books_by_title()
        elif choice == "3":
            self.ui_find_book_by_author()
        elif choice == "4":
            self.ui_find_client_by_id()
        elif choice == "5":
            self.ui_find_clients_by_name()
        elif choice == "0":
            pass
        else:
            print("invalid choice!")

    def ui_statistics(self):
        self.submenu4()
        choice = input("> ")
        if choice == "1":
            self.ui_most_rented_books()
        elif choice == "2":
            self.ui_most_active_clients()
        elif choice == "3":
            self.ui_most_rented_author()
        elif choice == "0":
            pass
        else:
            print("invalid choice!")

    @staticmethod
    def submenu1():
        print("\nmanage clients and books")
        print("1. add a book")
        print("2. add a client")
        print("3. remove a book")
        print("4. remove a client")
        print("5. update a book")
        print("6. update a client")
        print("7. list the books")
        print("8. list the clients")
        print("0. abandon")

    @staticmethod
    def submenu2():
        print("\nrent or return a book")
        print("1. rent a book")
        print("2. return a book")
        print("0. abandon")

    @staticmethod
    def submenu3():
        print("\nsearch for clients or books")
        print("1. search for a book with a specific id")
        print("2. search for books using the title")
        print("3. search for books using the author")
        print("4. search for a client with a specific id")
        print("5. search for clients using the name")
        print("0. abandon")

    @staticmethod
    def submenu4():
        print("\nstatistics")
        print("1. most rented books")
        print("2. most active clients")
        print("3. most rented author")
        print("0. abandon")

    @staticmethod
    def menu():
        print("\nmenu")
        print("1. manage clients and books")
        print("2. rent or return a book")
        print("3. search for clients or books")
        print("4. statistics")
        print("0. exit")

    def start(self):
        while True:
            self.menu()
            choice = input("> ")
            if choice == "1":
                self.ui_manage_clients_and_books()
            elif choice == "2":
                self.ui_rent_or_return()
            elif choice == "3":
                self.ui_search()
            elif choice == "4":
                self.ui_statistics()
            elif choice == "0":
                print("thank you for using my program!")
                break
            else:
                print("invalid choice!")
