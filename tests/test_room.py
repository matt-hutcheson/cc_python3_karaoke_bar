import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_tropical = Room("Tropical Room", 5)
        self.room_magma = Room("Magma", 4)
        self.test_guest = Guest("Party Bob", 38, 2000.00)
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
        test_guest2 = Guest("Musical Bob", 54, 700.00)
        test_guest3 = Guest("Tone Deaf Bob", 76, 500.00)
        self.room_tropical.guest_list = [self.test_guest, test_guest2, test_guest3]
        self.room_tropical.check_out_guest(test_guest2)
        self.assertEqual("Party Bob", self.room_tropical.guest_list[0].name)
        self.assertEqual("Tone Deaf Bob", self.room_tropical.guest_list[1].name)
        self.assertEqual(2, len(self.room_tropical.guest_list))

    def test_add_song_to_room(self):
        self.room_tropical.add_song(self.test_song)
        self.assertEqual(1, len(self.room_tropical.song_list))

    def test_reset_room(self):
        self.room_tropical.reset_room()
        self.assertEqual(0, len(self.room_tropical.guest_list))
        self.assertEqual(0, len(self.room_tropical.song_list))

    def test_room_capacity_allowed(self):
        self.room_magma.guest_list = [self.test_guest, self.test_guest, self.test_guest]
        self.assertEqual(True, self.room_magma.capacity_check())

    def test_room_capacity_exceeded(self):
        self.room_magma.guest_list = [self.test_guest, self.test_guest, self.test_guest, self.test_guest]
        self.assertEqual(False, self.room_magma.capacity_check())

    def test_pay_entry_fee(self):
        self.room_tropical.pay_entry_fee(guest_to_pay)
        self.assertEqual(15.00, self.room_tropical.cash_take)