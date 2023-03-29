import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Lager", 5, 3)

    def test_drink_has_name(self):
        self.assertEqual("Lager", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)