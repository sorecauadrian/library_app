import unittest
import datetime

from src.domain.book import Book
from src.domain.client import Client
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService


class Test(unittest.TestCase):
    def test_add_book(self):
        service = BookService()
        service.store(11, "adi", "adi")
        self.assertEqual(len(service.get_all()), 11)
        self.assertEqual(service.get_all()[10].id, 11)
        self.assertEqual(service.get_all()[10].title, "adi")
        self.assertEqual(service.get_all()[10].author, "adi")

    def test_add_client(self):
        service = ClientService()
        service.store(11, "adi")
        self.assertEqual(len(service.get_all()), 11)
        self.assertEqual(service.get_all()[10].id, 11)
        self.assertEqual(service.get_all()[10].name, "adi")

    def test_remove_book(self):
        service = BookService()
        service.store(11, "adi", "adi")
        service.store(12, "luci", "luci")
        self.assertEqual(len(service.get_all()), 12)
        service.delete("12")
        self.assertEqual(len(service.get_all()), 11)

    def test_remove_client(self):
        service = ClientService()
        service.store(11, "adi")
        service.store(12, "luci")
        self.assertEqual(len(service.get_all()), 12)
        service.delete("12")
        self.assertEqual(len(service.get_all()), 11)

    def test_update_book(self):
        service = BookService()
        service.store(11, "adi", "adrian")
        service.update(11, "luci", "lucian")
        self.assertEqual(len(service.get_all()), 11)
        self.assertEqual(service.get_all()[10].id, 11)
        self.assertEqual(service.get_all()[10].title, "luci")
        self.assertEqual(service.get_all()[10].author, "lucian")

    def test_update_client(self):
        service = ClientService()
        service.store(11, "adi")
        service.update(11, "luci")
        self.assertEqual(len(service.get_all()), 11)
        self.assertEqual(service.get_all()[10].id, 11)
        self.assertEqual(service.get_all()[10].name, "luci")

    def test_find_book(self):
        service = BookService()
        service.store(11, "adi", "adrian")
        service.store(12, "luci", "lucian")
        self.assertEqual(service.find_by_id(11), Book(11, "adi", "adrian"))
        self.assertEqual(service.find_by_id(0), None)
        self.assertEqual(service.find_by_title("adi"), [Book(11, "adi", "adrian")])
        self.assertEqual(service.find_by_title("adrian"), [])
        self.assertEqual(service.find_by_author("adrian"), [Book(11, "adi", "adrian")])
        self.assertEqual(service.find_by_author("adi"), [])

    def test_find_client(self):
        service = ClientService()
        service.store(11, "adi")
        service.store(12, "luci")
        self.assertEqual(service.find_by_id(11), Client(11, "adi"))
        self.assertEqual(service.find_by_id(0), None)
        self.assertEqual(service.find_by_name("adi"), [Client(11, "adi")])
        self.assertEqual(service.find_by_name("adrian"), [])

    def test_add_rental(self):
        rentalService = RentalService()

        rentalService.create(1, 1, 1, datetime.date.today() - datetime.timedelta(days=3), datetime.date.today())
        self.assertEqual(len(rentalService.get_all()), 1)
        self.assertEqual(rentalService.get_all()[0].id, 1)
        self.assertEqual(rentalService.get_all()[0].book_id, 1)
        self.assertEqual(rentalService.get_all()[0].client_id, 1)
        self.assertEqual(rentalService.get_all()[0].rented_date, datetime.date.today() - datetime.timedelta(days=3))
        self.assertEqual(rentalService.get_all()[0].returned_date, datetime.date.today())

    def test_delete_rental(self):
        rentalService = RentalService()

        rentalService.create(1, 1, 1, datetime.date.today() - datetime.timedelta(days=3), datetime.date.today())
        rentalService.delete_rental(1)
        self.assertEqual(len(rentalService.get_all()), 0)


