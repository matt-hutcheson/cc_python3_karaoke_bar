class Bar:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}
        self.rooms = []

    def add_money_to_till(self, money_to_add):
        self.till += money_to_add

    def add_drink(self, drink):
        if drink.name in self.drinks:
            self.drinks[drink.name]["stock"] += 1
        else:
            self.drinks[drink.name] = {"price":drink.price, "alcohol_units":drink.alcohol_units, "stock": 1}

    def remove_drink(self, drink):
        if drink.name in self.drinks:
            self.drinks[drink.name]["stock"] -= 1

    def stock_count(self):
        stock_count = 0
        for drink in self.drinks:
            stock_count += self.drinks[drink]["stock"]
        return stock_count