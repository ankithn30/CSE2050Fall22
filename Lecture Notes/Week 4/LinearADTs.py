class Stack_Wrapper:
    """Implements Stack ADT w/ List Wrapper"""
def __init__(self):
    self._L = [] #composition :L a stack *has a* list 

    def push(self,item):
        return self._L.insert(0, item) #O(n)
        #self._L.append(item) # O(1)
    def pop(self):
        return self._L.pop() #O(1)
        #return self._L.pop() #O(n)
    def __len__(self):
        return len(self._L) #O(1)
class Queue_Wrapper:
    """Implements Queue ADT w/ List Wrapper"""

class Deque_Wrapper:
    """Implements Deque ADT w/ List Wrapper"""
