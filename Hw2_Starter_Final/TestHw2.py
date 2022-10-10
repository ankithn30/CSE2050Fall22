# Start here. Once you have good test, move on to hw2.py
from ast import Return
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

        c2 = Card(3, "red","solid","oval")

        self.assertEqual(c2.number, 3)
        self.assertEqual(c2.color, "red")
        self.assertEqual(c2.shading, "solid")
        self.assertEqual(c2.shape, "oval")

        c3 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c3.number, 2)
        self.assertEqual(c3.color, "green")
        self.assertEqual(c3.shading, "striped")
        self.assertEqual(c3.shape, "diamond")
    def test_str(self):
        """test that we can get a good string representation of GroupCard instances"""
        #if ALL attributes of the card are equal then it will return 
        c1 = Card(2, "green", "striped", "diamond") 
        assert str(c1) == "Card(2, green, striped, diamond)"
    def test_eq(self):
        """Tests that two cards are equal if and only if all attributes (number, color, shading, shape) are equal"""
        c1 = Card(2, "green", "striped", "diamond")
        c3 = Card(2, "green", "striped", "diamond")
        assert c1 == c3
       

# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self): 
        """Would test how this works in that specifc situation"""
        mydec = Deck()
        self.assertEqual(len(mydec),81)



    def test_draw_top(self): 
        mydec = Deck()
        mycard = mydec.draw_top()
        self.assertEqual(mycard, Card(3,'purple','solid','oval'))
            
    '''Tests if the top card is drawn'''

    def test_shuffle(self): 
        L = ['abcde']
    
# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):

    def test_is_group(self): 
       pass
unittest.main() # runs all unittests above

