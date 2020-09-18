import unittest

from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_tropical = Room("Tropical Room")
        self.room_magma = Room("Magma")
        self.test_guest = Guest("Party Bob", 38, 2000.00)

    def test_room_exists(self):
        self.assertEqual("Tropical Room", self.room_tropical.name)
        self.assertEqual(0, len(self.room_tropical.guest_list))
        self.assertEqual(0, len(self.room_tropical.song_list))

    def test_check_in_guest_to_room(self):
        self.room_tropical.check_in_guest(self.test_guest)
        self.assertEqual(1, len(self.room_tropical.guest_list))

    def test_check_out_guest_from_room(self):
        self.room_tropical.check_in_guest(self.test_guest)
        self.room_tropical.check_out_guest(self.test_guest)
        self.assertEqual(0, len(self.room_tropical.guest_list))

    def test_check_out_guest_from_room_multiple_guests(self):
        test_guest2 = Guest("Musical Bob", 54, 700.00)
        test_guest3 = Guest("Tone Deaf Bob", 76, 500.00)
        self.room_tropical.check_in_guest(self.test_guest)
        self.room_tropical.check_in_guest(test_guest2)
        self.room_tropical.check_in_guest(test_guest3)
        self.room_tropical.check_out_guest(test_guest2)
        self.assertEqual("Party Bob", self.room_tropical.guest_list[0].name)
        self.assertEqual("Tone Deaf Bob", self.room_tropical.guest_list[1].name)
        self.assertEqual(2, len(self.room_tropical.guest_list))