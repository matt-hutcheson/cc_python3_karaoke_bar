import unittest

from src.guest import Guest
from src.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_loud_bob = Guest("Loud Bob", 23, 200.00, "Song 2", 100.00)
        self.guest_shy_bob = Guest("Shy Bob", 18, 1000.00, "Three Blind Mice", 0.00)

    def test_guest_exists(self):
        self.assertEqual("Loud Bob", self.guest_loud_bob.name)
        self.assertEqual(23, self.guest_loud_bob.age)
        self.assertEqual(200.00, self.guest_loud_bob.wallet)

    def test_guest_pays_for_room(self):
        self.guest_loud_bob.pay(15.00)
        self.assertEqual(185.00, self.guest_loud_bob.wallet)

    def test_customer_has_money_to_pay__True(self):
        entry_fee = 15.00
        self.assertEqual(True, self.guest_loud_bob.check_can_pay(entry_fee))

    def test_customer_has_money_to_pay__False(self):
        entry_fee = 201.00
        self.assertEqual(False, self.guest_loud_bob.check_can_pay(entry_fee))

    def test_guest_has_favourite_song(self):
        self.assertEqual("Song 2", self.guest_loud_bob.fav_song)

    def test_guest_can_pay_drink(self):
        test_drink = Drink("Blue Lagoon", 15.00, 4.00)
        self.guest_loud_bob.pay(test_drink.price)
        self.assertEqual(185.00, self.guest_loud_bob.wallet)