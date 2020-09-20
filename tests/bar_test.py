import unittest
from src.bar import Bar
from src.drink import Drink
from src.guest import Guest

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Music and Spirits", 100.00)
        self.beer = Drink("Tennents", 4.00, 2.00)
        self.cocktail = Drink("Depth Charge",8.50, 3.00)
        self.bar.drinks = [self.beer, self.cocktail]

    def test_bar_has_name(self):
        self.assertEqual("Music and Spirits", self.bar.name)

    def test_bar_has_till(self):
        self.assertEqual(100.00, self.bar.till)

    def test_bar_has_drinks(self):
        self.assertEqual(2,len(self.bar.drinks))
    
    def test_add_money_to_till(self):
        money_to_add = self.beer.price
        self.bar.add_money_to_till(money_to_add)
        self.assertEqual(104.00, self.bar.till)

    def test_add_drink(self):
        self.bar.add_drink(self.beer)
        self.assertEqual(3, len(self.bar.drinks))

    def test_remove_drink(self):
        self.bar.remove_drink(self.beer)
        self.assertEqual(1, len(self.bar.drinks))

    def test_stock_count(self):
        self.assertEqual(2, self.bar.stock_count())



