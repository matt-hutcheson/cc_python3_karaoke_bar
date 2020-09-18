import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Another One Bites The Dust", "Queen")
        self.song2 = Song("Song 2", "Blue")
        self.song3 = Song("Three Blind Mice", "Nat King Cole")

    def test_song_exists(self):
        self.assertEqual("Another One Bites The Dust", self.song1.title)
        self.assertEqual("Queen", self.song1.artist)

    