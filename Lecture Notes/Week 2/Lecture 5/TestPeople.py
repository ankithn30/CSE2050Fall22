import unittest #unittest is really useful 40
from Person import Student, Faculty 

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s1 = Student('ann20007','Ankith')

    def test_init(self,name,netId):
        s1  = Student('ann20007', 'Ankith')
        #assert s1.name('jake')
        self.assertEqual(s1.name,'Ankith')
        self.assertEqual(s1.netID,'ann20007')
    

    def test_change_name(self):
        #This is the function to change the name
        self.assertEqual(s1.name,'Ankith')
        self.s1.set._name('Andrew')
        self.assertEqual(s1.name, 'Andrew')


    def test_add_course(self):
        self.s1 = Student('ann20007','Ankith')


    class TestFaculty(unittest.TestCase):
        def setUp(self):
            self.f1 = Faculty('jake','jas14034')


        #private attribute, you can do that with "self.(_)name", the underscore makes it a private attribute 
        #wiete a test for how A USER will be using the class 