import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Lager", 5, 3)
        self.drink_2 = Drink("Wine", 8, 5)
        
        drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("The Prancing Pony", drinks, 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(5)
        self.assertEqual(105, self.pub.till)

    def test_sell_drink_to_customer(self):
        customer = Customer("Bob", 100, 21, 0)
        self.pub.sell_drink_to_customer(self.drink_1, customer)
        self.assertEqual(95, customer.wallet)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(3, customer.drunkenness)

    def test_sell_drink_to_customer_underage(self):
        customer = Customer("Alice", 100, 16, 0)
        self.pub.sell_drink_to_customer(self.drink_1, customer)
        self.assertEqual(100, customer.wallet)
        self.assertEqual(100, self.pub.till)

    def test_check_drunkenness(self):
        customer = Customer("Bob", 100, 21, 50)
        self.pub.sell_drink_to_customer(self.drink_1, customer)
        self.assertEqual(100, customer.wallet)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(50, customer.drunkenness)
        
    def test_sell_food_to_customer(self):
        customer = Customer("Bob", 100, 21, 30)
        food = Food("Chips", 5, 10)
        self.pub.sell_food_to_customer(food, customer)
        self.assertEqual(95, customer.wallet)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(20, customer.drunkenness)