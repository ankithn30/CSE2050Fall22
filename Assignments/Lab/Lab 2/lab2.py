#example use Class Run(self, distance, time)

# class Point:
#     def __init__(self, x, y):
#         pass

# if __name__ == '__main__':
#     p1 = Point(3, 4)
#     assert p1.x == 3
#     assert p1.y == 4

#the code above fails, which is good and it shows that our first step of TDD is complete


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_from_origin(self):
        d = ((self.x**2)+(self.y**2))**(1/2)
        return d 

    def __eq__(self,other):
        return self.dist_from_origin() == other.dist_from_origin()

    
    def __lt__(self,other):
        return self.dist_from_origin() < other.dist_from_origin()
        
    def __gt__(self,other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __str__(self):
        return "Point({}, {})".format(self.x,self.y)


if __name__ == '__main__':
    p1 = Point(3, 4)
    s1 = str(p1)
    p2 = Point(2,2)
    s2 = str(p2)
    p3 = Point(3,4)
    s3 = str(p3)
    p4 = Point(5,6)
    s4 = str(p4)
    # assert p1.x == 3
    # assert p1.y == 4
    # assert p1.x == 3
    # assert p2.x ==2

    # assert p1.y == 4 
    # assert p2.y == 2

    assert not (p1 == p2) #expected False, with "not" is true 
    assert p1 == p3 #True

    assert not (p2 == p3) #expected False, with "not" is true 
    assert not (p2 > p1) #false 

    assert not(p3>p1) #true (original expected false )
    assert p3<p4 #true 

    assert p4 > p2 #true 
    assert not (p4==p2)

    assert str(s1) == "Point(3, 4)"
    assert str(s2) != "Point(2, 1)"

    assert p1.dist_from_origin()
    assert p4.dist_from_origin()
    #Auto Graded Test 


    #Manually Graded Tests(75)