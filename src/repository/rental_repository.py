from src.repository.exceptions import RepositoryException

class RentalRepository:
    def __init__(self, list_of_rentals : list = None):
        if list_of_rentals is None:
            list_of_rentals = []
        self.__rentals = list_of_rentals

    def store(self, rental):
        if self.find_by_id(rental.id) is not None:
            raise RepositoryException("rental with id " + str(rental.id) + " already in repository!")
        self.__rentals.append(rental)

    def find_by_id(self, rentalId : int):
        for rental in self.__rentals:
            if rentalId == rental.id:
                return rental
        return None

    def update(self, rental):
        updatedRental = self.find_by_id(rental.id)
        if updatedRental is None:
            raise RepositoryException("rental not found!")
        indexOfRental = self.__rentals.index(updatedRental)
        self.__rentals.remove(updatedRental)
        self.__rentals.insert(indexOfRental, rental)

    def delete(self, rentalId : int):
        rental = self.find_by_id(rentalId)
        if rental is None:
            raise RepositoryException("rental not found!")
        self.__rentals.remove(rental)
        return rental

    def get_all(self):
        return self.__rentals

    def __len__(self):
        return len(self.__rentals)

    def __str__(self):
        result = ""
        for rental in self.__rentals:
            result += str(rental)
            result += "\n"
        return result
