# STOP! You should write tests in TestHw2.py before modifying this file.

class Card:
    def __init__(self,number,color,shading,shape): 
        self._color = color 
        self._shape = shape
        self._number = number
        self._shading = shading 
    def __str__(self): pass

    # repr() is called instead of str() by some of pytho's built-ins. We'll always
    # want the same value returned in this course, so we can piggyback off of str
    def __repr__(self): return str(self)

    def __eq__(self, other): 
        return self._color == other._color


# Valid values for default game of GROUP! included here to avoid spelling
# issues. Feel free to copy/paste:
# [1, 2, 3]
# ['diamond', 'squiggle', 'oval']
# ['green', 'blue', 'purple']
# ['empty', 'striped', 'solid']
class Deck:
    def __init__(self): pass    
        
    # should remove and return top card
    def draw_top(self): pass

    # should randomly shuffle cards. Does not need a return.
    def shuffle(self): pass

    # should return number of items in deck
    def __len__(self): pass



# Oonce Card and Deck are both finished, write tests for this algorithm, then
# write the algorithm

# True if, for all attributes, each card has the same or different values;
# e.g. {1, 1, 1} or {1, 2, 3}, but not {1, 1, 3}
def is_group(): pass
