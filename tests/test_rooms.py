import unittest

from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_tropical = Rooms("Tropical Room")
        self.room_magma = Rooms("Magma")

    def test_room_exists(self):
        self.assertEqual("Tropical Room", self.room_tropical.name)
        self.assertEqual(0, len(self.room_tropical.guest_list))
        self.assertEqual(0, len(self.room_tropical.song_list))

    