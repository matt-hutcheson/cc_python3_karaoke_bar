import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Old Fashioned", 10.00, 4.00)
    
    def test_drink_has_name(self):
        self.assertEqual("Old Fashioned", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(10.00, self.drink.price)

    def test_drink_alcohol_units(self):
        self.assertEqual(4, self.drink.alcohol_units)