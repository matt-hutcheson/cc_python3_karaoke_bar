import unittest

from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song1 = Songs("Another One Bites The Dust", "Queen")
        self.song2 = Songs("Song 2", "Blue")
        self.song3 = Songs("Three Blind Mice", "Nat King Cole")

    def test_song_exists(self):
        self.assertEqual("Another One Bites The Dust", self.song1.title)
        self.assertEqual("Queen", self.song1.artist)

    