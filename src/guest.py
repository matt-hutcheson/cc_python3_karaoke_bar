class Guest():
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def pay(self, entry_fee):
        self.wallet -= entry_fee

    def check_can_pay(self, price):
        if self.wallet >= price:
            return True
        else:
            return False

    