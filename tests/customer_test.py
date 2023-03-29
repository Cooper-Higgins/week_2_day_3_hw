import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Bob", 100.00)

    def test_buy_drink(self, drink, wallet):
        