class Bar:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_money_to_till(self, money_to_add):
        self.till += money_to_add

    def sell_drink(self, drink, guest):
        if guest.age > 18:
            if guest.drunkeness < 25.00:
                self.add_money_to_till(drink.price)
                guest.pay(drink.price)
                self.remove_drink(drink)
            else:
                return "Beat it drunken scamp!"
        else:
            return "Beat it scamp!"

    def add_drink(self, drink):
        self.drinks.append(drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def stock_count(self):
        return len(self.drinks)