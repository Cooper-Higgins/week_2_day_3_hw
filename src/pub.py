class Pub:
    
    def __init__(self, name, drinks, till):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink

    def sell_drink_to_customer(self, drink, customer):
        if customer.age >= 18 and customer.drunkenness < 20:
            self.drinks.remove(drink)
            customer.buy_drink(drink.price, drink.alcohol_level)
            self.increase_till(drink.price)
        else:
            print("Get out of ma pub")

    def sell_food_to_customer(self, food, customer):
        customer.buy_food(food.price, food.rejuvenation)
        self.increase_till(food.price)