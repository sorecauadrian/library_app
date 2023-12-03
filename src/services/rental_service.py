from src.domain.rental import Rental, RentalValidator
from datetime import date, timedelta

from src.repository.rental_repository import RentalRepository


class RentalService:
    def __init__(self, validator = None, repository = None):
        if validator is None:
            validator = RentalValidator()
        if repository is None:
            repository = RentalRepository(self.list_of_rentals())
        self.__validator = validator
        self.__repository = repository

    def create(self, rentalId : int, bookId : int, clientId : int, rented_date, returned_date):
        rental = Rental(rentalId, bookId, clientId, rented_date, returned_date)
        self.__validator.validate(rental)
        self.__repository.store(rental)
        return rental

    def book_is_available(self, book, rented_date, returned_date):
        rentals = self.filter_rentals(book, None)
        for rental in rentals:
            if rental.returned_date < rented_date or rental.rented_date > returned_date:
                continue
            return False
        return True

    def filter_rentals(self, bookId, clientId):
        result = []
        for rental in self.__repository.get_all():
            if bookId is not None and bookId != rental.book_id:
                continue
            if clientId is not None and clientId != rental.client_id:
                continue
            result.append(rental)
        return result

    def return_a_book(self, bookId, clientId):
        rental = self.filter_rentals(bookId, clientId)
        self.delete_rental(rental[0].id)
        self.create(rental[0].id, rental[0].book_id, rental[0].client_id, rental[0].rented_date, date.today())

    def delete_rental(self, rentalId: int):
        rental = self.__repository.delete(rentalId)
        return rental

    def get_all(self):
        return self.__repository.get_all()

    @staticmethod
    def list_of_rentals():
        return [Rental(1, 1, 1, date.today() - timedelta(days=5), date.today() - timedelta(days=3)),
                Rental(2, 1, 2, date.today() - timedelta(days=3), date.today() - timedelta(days=1)),
                Rental(3, 2, 2, date.today() - timedelta(days=8), date.today() - timedelta(days=4)),
                Rental(4, 3, 2, date.today() - timedelta(days=10), date.today() - timedelta(days=9)),
                Rental(5, 3, 1, date.today() - timedelta(days=8), date.today() - timedelta(days=5))]

