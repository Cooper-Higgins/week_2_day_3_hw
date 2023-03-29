class Customer:
    
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def buy_drink(self, price, alcohol_level):
        self.wallet -= price
        self.drunkenness += alcohol_level

    def buy_food(self, price, rejuvenation_level):
        self.wallet -= price
        self.drunkenness -= rejuvenation_level