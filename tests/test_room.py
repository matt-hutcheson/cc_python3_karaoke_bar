import unittest

from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_tropical = Room("Tropical Room")
        self.room_magma = Room("Magma")

    def test_room_exists(self):
        self.assertEqual("Tropical Room", self.room_tropical.name)
        self.assertEqual(0, len(self.room_tropical.guest_list))
        self.assertEqual(0, len(self.room_tropical.song_list))

    def test_check_in_guest_to_room(self):
        test_guest = Guest("Party Bob", 38, 2000.00)
        self.room_tropical.check_in_guest(test_guest)
        self.assertEqual(1, len(self.room_tropical.guest_list))