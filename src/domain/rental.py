from src.domain.exceptions import ValidatorException

class Rental:
    def __init__(self, rental_id : int, book_id : int, client_id : int, rented_date, returned_date):
        self.__id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def id(self):
        return self.__id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def returned_date(self):
        return self.__returned_date

    def __len__(self):
        return (self.returned_date - self.rented_date).days + 1

    def __str__(self):
        return "rental: " + str(self.id) + "\n book: " +  str(self.book_id) + "\n client: " + str(self.client_id) + "\n period: " + self.rented_date.strftime("%d.%m.%y") + " to " + self.returned_date.strftime("%d.%m.%y")

class RentalValidator:
    def validate(self, rental : Rental):
        if not isinstance(rental, Rental):
            raise TypeError("can only validate rental objects!")
        errors = []
        if len(rental) < 1 and len(rental) != 0:
            errors.append("rental must be at least 1 day!")
        if len(errors) > 0:
            raise ValidatorException(errors)
        return True