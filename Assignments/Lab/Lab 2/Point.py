#Setting up the Class "Point"
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
 
    assert p1 == p2 #False
    assert p1 == p3 #True

    assert p2 == p3 #False
    assert  p1 > p2 #True  

    assert p3<p1 #True
    assert p3>p4 #False

    assert p4<p2 #False
    assert p4!=p2 #True

    assert str(s1) == "Point(3, 4)" #expected true
    assert str(s2) == "Point(2, 1)" #expected false

    assert p1.dist_from_origin() #provides the distance from origin
    assert p4.dist_from_origin() #provides distance from origin
    
 