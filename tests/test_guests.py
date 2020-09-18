import unittest

from src.guests import Guests

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest_loud_bob = Guests("Loud Bob", 23, 200.00)
        self.guest_shy_bob = Guests("Shy Bob", 18, 1000.00)

    def test_guest_exists(self):
        self.assertEqual("Loud Bob", self.guest_loud_bob.name)
        self.assertEqual(23, self.guest_loud_bob.age)
        self.assertEqual(200.00, self.guest_loud_bob.wallet)

    