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

    def test_sell_drink(self):
        test_guest = Guest("Drunken Bob", 53, 200.00, "Song 2",20.00)
        test_drink = self.beer
        self.bar.sell_drink(self.beer, test_guest)
        self.assertEqual(104.00, self.bar.till)
        self.assertEqual(196, test_guest.wallet)
        self.assertEqual(1, self.bar.stock_count())

    def test_add_drink(self):
        self.bar.add_drink(self.beer)
        self.assertEqual(3, len(self.bar.drinks))

    def test_remove_drink(self):
        self.bar.remove_drink(self.beer)
        self.assertEqual(1, len(self.bar.drinks))

    def test_stock_count(self):
        self.assertEqual(2, self.bar.stock_count())

    def test_age_check(self):
        test_guest = Guest("Young Bob", 13, 1.50, "Three Blind Mice",0.00)
        self.assertEqual("Beat it scamp!", self.bar.sell_drink(self.beer, test_guest))

    def test_refuse_drunk(self):
        test_guest = Guest("Really Drunken Bob", 50, 23.00, "Another One Bites The Dust",25.00)
        self.assertEqual("Beat it drunken scamp!", self.bar.sell_drink(self.cocktail, test_guest))