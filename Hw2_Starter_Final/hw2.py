# STOP! You should write tests in TestHw2.py before modifying this file.
import random
class Card:
    def __init__(self,number,color,shading,shape): 
        self.color = color 
        self.shape = shape
        self.number = number
        self.shading = shading 
    def __str__(self):
          return "Card({}, {}, {}, {})".format(self.number, self.color,self.shading,self.shape)


    # repr() is called instead of str() by some of pytho's built-ins. We'll always
    # want the same value returned in this course, so we can piggyback off of str
    def __repr__(self): 
        return self.str

    def __eq__(self, other): 
        if(self.number == other.number and self.color == other.color and self.shading == other.shading and self.shape == other.shape):
            return True
        return False


# Valid values for default game of GROUP! included here to avoid spelling
# issues. Feel free to copy/paste:
# [1, 2, 3]
# ['diamond', 'squiggle', 'oval']
# ['green', 'blue', 'purple']
# ['empty', 'striped', 'solid']
class Deck:
    def __init__(self,number = [1,2,3], color = ['green', 'blue', 'purple'], shading = ['empty', 'striped', 'solid'], shape =["diamond","squiggle","oval"] ): 

        self.cards = []

        for s in shape:
            for z in color:
                for x in shading:
                    for y in number:
                        self.cards.append(Card(y,z,x,s))

    # should remove and return top card
    def draw_top(self): 
        return self.cards.pop()

    # should randomly shuffle cards. Does not need a return.
    def shuffle(self): 
        random.shuffle(self.cards)

    # should return number of items in deck
    def __len__(self): 
        return len(self.cards)

# Once Card and Deck are both finished, write tests for this algorithm, then
# write the algorithm

# True if, for all attributes, each card has the same or different values;
# e.g. {1, 1, 1} or {1, 2, 3}, but not {1, 1, 3}
def is_group(c1,c2,c3): 
    return (\
            (((c1.number == c2.number) and (c2.number == c3.number)) or ((c1.number != c2.number) and (c1.number != c3.number) and (c2.number != c3.number))) and \
            (((c1.color == c2.color) and (c2.color == c3.color)) or ((c1.color != c2.color) and (c1.color != c3.color) and (c2.color != c3.color))) and \
            (((c1.shades == c2.shades) and (c2.shades == c3.shades)) or ((c1.shades != c2.shades) and (c1.shades != c3.shades) and (c2.shades != c3.shades))) and\
            (((c1.shapes == c2.shapes) and (c2.shapes == c3.shapes)) or ((c1.shapes != c2.shapes) and (c1.shapes != c3.shapes) and (c2.shapesa != c3.shapes)))
             )
