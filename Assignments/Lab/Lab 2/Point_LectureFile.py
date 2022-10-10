#test-driven devlopment
#able to naturally debug the code
#3Phases
#1. Red 2. Green 3. Refractor (Blue Phase)

#def sum(num1, num2)
    # return num1 + num2

#Write a test that fails 
    #make sure it FAILS 


#Use test-driven devlopment for EVRYTHING, HW AND LABS 

#Write a failed test BEFORE writing the function, to check.
#Write function
##^Follow these steps above 

#Think what line will fail & WHAT ERROR IT WOULD GIVE YOU, you would want to figure out the expected reason for failure 
#Red Phase: Wirte a test that you know will fail 
#Green Phase: (?)
#Refactor: Rewrite code with simplicity, would want to do this, if you are repeating things over and over again
    #Make that code into a function
    #Helps with the efficency of writing code 


#object oriented programming
    #OOP
    #Programming where we are orient our brain
    # x=[]
    # #x is an instance of a list class
        #make an instance of the class 
    #List attributes:
        #Variable, Method, .append(),.pop(),.remove(), .len()  (Capsualtion, where you can put everything somewhere to see what you can do with it)
            #What this variable is and WHAT I can do with it 
    #Example for a car isntance, provide all information about the car, important thngs about it, make, model, speed, engine
    #c1 = car(max.speed = 50mph, make "Toyota", ... )
    #c2 = car(max_speed = 60mph, make = "dodge"...)

    #Two ways to write it 
    #my.set{1,2,3}
    #my_set = set(1,2,3)


#self, will be always used, can technically use any variable 


import math
class Vector():
    def __init__(self, p1,p2):
        self.x = p1
        self.y = p2

    def magnitude(self.p1**2 + self.p2**2) ** (1/2)

    def angle(self):
        return math.atan (self.y/self.x)
#Vector.__init__(v1,3,4)
#print(v1)

v1 = Vector(3,4) #calls vector.__init__ w/v1
v2 = Vector(4,5)


assert v1.x == 3
assert v1.y == 4


print(Vector.magnitude(v1))
assert v1.magnitude() == 5 #dot notation, the it would be the first thing that is plugged in

#Line 5 (50) Fails above
#--init__, a variable that is held onto by python


#TEST-CASES IMPORTANT 
p1 = PolarVector(2,2)
assert p1.angle() == 45

#when you get an error think "Awesome!, another error!"



#Inheritance 
#makeing a way to make a class a sub class 
#Object
    #Children (ie int, float, string & VECTOR 
    #Polar Vector goes WITHIN the vector "child"
    #you can consolidate it, look at picture 


#run test and make sure it fails