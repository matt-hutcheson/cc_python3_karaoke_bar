class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.capacity = capacity
        self.cash_take = 0.00
        self.entry_fee = 15.00

    def check_in_guest(self, guest_to_add):
        check = self.capacity_check()
        if check:
            self.guest_list.append(guest_to_add)
            return self.guest_reacts_to_favourite_song(guest_to_add)

    def check_out_guest(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)

    def add_song(self, song_to_add):
        self.song_list.append(song_to_add)
        for guest in self.guest_list:
            return self.guest_reacts_to_favourite_song(guest)

    def reset_room(self, bar):
        bar.till += self.cash_take
        self.cash_take = 0
        self.song_list.clear()
        self.guest_list.clear()

    def capacity_check(self):
        if len(self.guest_list) < self.capacity:
            return True
        else:
            return False
        
    def pay_entry_fee(self, guest_to_pay):
        if guest_to_pay.check_can_pay(self.entry_fee):
            guest_to_pay.pay(self.entry_fee)
            self.cash_take += self.entry_fee

    def guest_reacts_to_favourite_song(self, guest):
        for song in self.song_list:
            if song.title == guest.fav_song:
                return f"{song.title} is {guest.name}'s tune!!!"

    def sell_drink(self, drink, guest, bar):
        if guest.age > 18:
            if guest.drunkeness < 25.00:
                self.cash_take += drink.price
                guest.pay(drink.price)
                bar.remove_drink(drink)
            else:
                return "Beat it drunken scamp!"
        else:
            return "Beat it young scamp!"