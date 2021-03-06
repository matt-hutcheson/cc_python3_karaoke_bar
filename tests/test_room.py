import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar
from src.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_tropical = Room("Tropical Room", 5)
        self.room_magma = Room("Magma", 4)
        self.test_guest = Guest("Party Bob", 38, 2000.00, "Song 2", 100.00)
        self.test_song = Song("Song 2", "Blur")

    def test_room_exists(self):
        self.assertEqual("Tropical Room", self.room_tropical.name)
        self.assertEqual(0, len(self.room_tropical.guest_list))
        self.assertEqual(0, len(self.room_tropical.song_list))

    def test_check_in_guest_to_room(self):
        self.room_tropical.check_in_guest(self.test_guest)
        self.assertEqual(1, len(self.room_tropical.guest_list))

    def test_check_out_guest_from_room(self):
        self.room_tropical.guest_list = [self.test_guest]
        self.room_tropical.check_out_guest(self.test_guest)
        self.assertEqual(0, len(self.room_tropical.guest_list))

    def test_check_out_guest_from_room_multiple_guests(self):
        test_guest2 = Guest("Musical Bob", 54, 700.00, "Another One Bites The Dust", 5.00)
        test_guest3 = Guest("Tone Deaf Bob", 76, 500.00, "Three Blind Mice", 50.00)
        self.room_tropical.guest_list = [self.test_guest, test_guest2, test_guest3]
        self.room_tropical.check_out_guest(test_guest2)
        self.assertEqual("Party Bob", self.room_tropical.guest_list[0].name)
        self.assertEqual("Tone Deaf Bob", self.room_tropical.guest_list[1].name)
        self.assertEqual(2, len(self.room_tropical.guest_list))

    def test_add_song_to_room(self):
        self.room_tropical.add_song(self.test_song)
        self.assertEqual(1, len(self.room_tropical.song_list))

    def test_reset_room(self):
        test_bar = Bar("Music and Spirits", 100.00)
        self.room_tropical.cash_take = 100.00
        self.room_tropical.add_song(self.test_song)
        self.room_tropical.check_in_guest(self.test_guest)
        self.room_tropical.reset_room(test_bar)
        self.assertEqual(0, len(self.room_tropical.guest_list))
        self.assertEqual(0, len(self.room_tropical.song_list))
        self.assertEqual(200.00, test_bar.till)

    def test_room_capacity_allowed(self):
        self.room_magma.guest_list = [self.test_guest, self.test_guest, self.test_guest]
        self.assertEqual(True, self.room_magma.capacity_check())

    def test_room_capacity_exceeded(self):
        self.room_magma.guest_list = [self.test_guest, self.test_guest, self.test_guest, self.test_guest]
        self.assertEqual(False, self.room_magma.capacity_check())

    def test_pay_entry_fee(self):
        self.room_tropical.pay_entry_fee(self.test_guest)
        self.assertEqual(15.00, self.room_tropical.cash_take)

    def test_entry_fee_low_funds(self):
        poor_guest = Guest("Poor Bob", 13, 10.00, "Money for Nothing", 2.00)
        self.room_tropical.pay_entry_fee(poor_guest)
        self.assertEqual(0, self.room_tropical.cash_take)

    def test_guest_reacts_to_favourite_song(self):
        self.room_tropical.add_song(self.test_song)
        self.assertEqual("Song 2 is Party Bob's tune!!!", self.room_tropical.guest_reacts_to_favourite_song(self.test_guest))

    def test_guest_reacts_to_fav_song_new_song_added(self):
        self.room_tropical.check_in_guest(self.test_guest)
        self.assertEqual("Song 2 is Party Bob's tune!!!",         self.room_tropical.add_song(self.test_song))

    def test_guest_reacts_to_fav_song_new_guest_added(self):
        self.room_tropical.add_song(self.test_song)
        self.assertEqual("Song 2 is Party Bob's tune!!!", self.room_tropical.check_in_guest(self.test_guest))

    def test_sell_drink(self):
        test_guest = Guest("Drunken Bob", 53, 200.00, "Song 2",20.00)
        test_beer = Drink("Tennents", 4.00, 2.00)
        test_bar = Bar("Music and Spirits", 100.00)
        test_bar.add_drink(test_beer)
        self.room_tropical.sell_drink(test_beer, test_guest, test_bar)
        self.assertEqual(4.00, self.room_tropical.cash_take)
        self.assertEqual(196, test_guest.wallet)
        self.assertEqual(0, test_bar.stock_count())

    def test_refuse_drunk(self):
        test_guest = Guest("Really Drunken Bob", 50, 23.00, "Another One Bites The Dust",25.00)
        test_cocktail = Drink("Depth Charge",8.50, 3.00)
        test_bar = Bar("Music and Spirits", 100.00)
        test_bar.add_drink(test_cocktail)
        self.assertEqual("Beat it drunken scamp!", self.room_tropical.sell_drink(test_cocktail, test_guest, test_bar))

    def test_age_check(self):
        test_guest = Guest("Young Bob", 13, 1.50, "Three Blind Mice",0.00)
        test_cocktail = Drink("Depth Charge",8.50, 3.00)
        test_bar = Bar("Music and Spirits", 100.00)
        test_bar.add_drink(test_cocktail)
        self.assertEqual("Beat it young scamp!", self.room_tropical.sell_drink(test_cocktail, test_guest, test_bar))