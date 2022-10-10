# Start here. Once you have good test, move on to hw2.py

import unittest
from hw2 import Card, Deck, is_group
class TestCard(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize cards w/ number/color/shading/shaper"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")

    def test_str(self):
        """test that we can get a good string representation of GroupCard instances"""

    def test_eq(self):
        """Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal"""
        

# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self): pass

    def test_draw_top(self): pass

    def test_shuffle(self): pass

# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):
    def test_is_group(self): pass


unittest.main() # runs all unittests above