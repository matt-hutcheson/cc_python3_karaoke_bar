class Guest():
    def __init__(self, name, age, wallet, fav_song, drunkeness):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fav_song = fav_song
        self.drunkeness = drunkeness

    def pay(self, entry_fee):
        self.wallet -= entry_fee

    def check_can_pay(self, price):
        if self.wallet >= price:
            return True
        else:
            return False

    