class Person:
    def __init__(self,netID,name):
        self._name = name
        self._netID = netID 
         
    @property          #property allows for the calling of methods like variables 
    def name(self):
        return self._name
        #changes email
        #prompts for new password 

class Student(Person):
    def __init__(self,netID,name):
        self._name = name #now a private atrribute 
        #self._netID = netID
        # Dont need it anymore, just used fo testing, now goign immediatelly through Person Class
        # #now a priivate attribute , so people cannot change the name whenever 

   
    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self._name  #now you are letting name be able to change with this 

    def _add_course(self,course): #can make tjuis method provate by adding a leading underscore 
        pass


class Faculty(Person): #using the person class, when using "Faculty" in the other file
    pass
    
    
    # def __init__(self,name,netID):
    #     self._name = name
    #     self._netID = netID 

    # @property
    # def name(self):
    #     return self._name()


#comment the code out and then jut use the general "Person" class cause its the same across 
