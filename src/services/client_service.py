from src.domain.client import Client, ClientValidator
from src.repository.client_repository import ClientRepository
from src.services.rental_service import RentalService


class ClientService:
    def __init__(self, validator = None, repository = None, rental_service = None):
        if validator is None:
            validator = ClientValidator()
        if repository is None:
            repository = ClientRepository(self.list_of_clients())
        if rental_service is None:
            rental_service = RentalService()
        self.__validator = validator
        self.__repository = repository
        self.__rental_service = rental_service

    def store(self, clientId : int, name : str):
        client = Client(clientId, name)
        self.__validator.validate(client)
        self.__repository.store(client)
        return client

    def delete(self, clientId : str):
        self.__repository.delete(clientId)

    def update(self, clientId : int, name : str):
        client = Client(clientId, name)
        self.__validator.validate(client)
        self.__repository.update(client)
        return client

    def get_all(self):
        return self.__repository.get_all()

    def find_by_id(self, clientId : int):
        return self.__repository.find_by_id(clientId)

    def find_by_name(self, name: str):
        return self.__repository.find_by_name(name)

    @staticmethod
    def list_of_clients():
        return [Client(1, "florin"),
                Client(2, "luci"),
                Client(3, "raul"),
                Client(4, "deni"),
                Client(5, "ilie"),
                Client(6, "cosmin"),
                Client(7, "rares"),
                Client(8, "darius"),
                Client(9, "beti"),
                Client(10, "rafa")]