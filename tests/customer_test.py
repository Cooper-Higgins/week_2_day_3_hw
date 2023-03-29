import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Bob", 100, 21, 0)
        self.customer_2 = Customer("Alice", 100, 16, 0)

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.customer_1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer_1.wallet)