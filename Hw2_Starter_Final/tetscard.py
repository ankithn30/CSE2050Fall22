 
from hw2 import Card
  
def __eq__(self, other): 
    if(self.number == other.number and self.color == other.color and self.shading == other.shading and self.shape == other.shape):
        return True
    return False
 
def test_eq(self):
    """Tests that two cards are equal if and only if all attributes (number, color, shading, shape) are equal"""
    c1 = Card(2, "green", "striped", "diamond")
    c3 = Card(2, "green", "striped", "dkjiamond")
    assert c1 == c3
    
c1 = Card(2, "green", "striped", "diamond")
c3 = Card(2, "green", "striped", "diamond")
assert c1 == c3

