from src.repository.exceptions import RepositoryException

class ClientRepository:
    def __init__(self, list_of_clients : list = None):
        if list_of_clients is None:
            list_of_clients = []
        self.__clients = list_of_clients

    def store(self, client):
        if self.find_by_id(client.id) is not None:
            raise RepositoryException("client with id " + str(client.id) + " already in repository!")
        self.__clients.append(client)

    def find_by_id(self, clientId: int):
        for client in self.__clients:
            if clientId == client.id:
                return client
        return None

    def find_by_name(self, name: str):
        books = []
        for client in self.__clients:
            if name in client.name:
                books.append(client)
        return books

    def update(self, client):
        updatedClient = self.find_by_id(client.id)
        if updatedClient is None:
            raise RepositoryException("client not found!")
        indexOfClient = self.__clients.index(updatedClient)
        self.__clients.remove(updatedClient)
        self.__clients.insert(indexOfClient, client)

    def delete(self, clientId : str):
        if clientId.isdigit is False:
            raise TypeError("the id is not an integer!")
        clientId = int(clientId)
        client = self.find_by_id(clientId)
        if client is None:
            raise RepositoryException("client not found!")
        self.__clients.remove(client)
        return client

    def get_all(self):
        return self.__clients

    def __len__(self):
        return len(self.__clients)

    def __str__(self):
        result = ""
        for client in self.__clients:
            result += str(client)
            result += "\n"
        return result
