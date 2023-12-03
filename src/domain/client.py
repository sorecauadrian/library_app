from src.domain.exceptions import ValidatorException

class Client:
    def __init__(self, client_id : int, name : str, days_of_rental : int = 0):
        self.__id = client_id
        self.__name = name
        self.__days_of_rental = days_of_rental

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.id == other.id

    def __str__(self):
        return str(self.id) + ": " + self.name

    def __repr__(self):
        return str(self)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name : str):
        self.__name = new_name

    @property
    def days_of_rental(self):
        return self.__days_of_rental

    @days_of_rental.setter
    def days_of_rental(self, new_days_of_rental : int):
        self.__days_of_rental = new_days_of_rental


class ClientValidator:
    def validate(self, client : Client):
        if not isinstance(client, Client):
            raise TypeError("can only validate client objects!")
        errors = []
        if len(client.name) < 3:
            errors.append("name must be at least 3 characters long!")
        if len(errors) > 0:
            raise ValidatorException(errors)
        return True
