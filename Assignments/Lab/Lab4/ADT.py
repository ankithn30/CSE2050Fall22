from ast import Assert
from LinkedList import LinkedList
#these are the clkasses for each of the different types of Lists and Linked List for a Stack and  Queue
#this is for stack:
class Stack_L:
    def __init__(self):
        self._L = []     # Composition: the Stack_L class has a List
    def push(self, item):
        self._L.append(item)
    def pop(self):
        return self._L.pop()
    def peek(self):
        return self._L[-1]
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self._L) == 0 
        #this is for stack LL
class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List
        self.len = 0
    def push(self,item):
        self._LL.add_first(item)
        self.len += 1
    def pop(self):
        self.len -= 1
        return self._LL.remove_first()
    def peek(self):
        return self._LL[-1]
    def __len__(self):
        return self.len
    def isempty(self):
        return len(self) == 0
class Queue_L:
    def __init__(self): 
        self._L = []
    def enqueue(self,item): #adds the item to a queue
        self._L.append(item)
    def dequeue(self):#take away the item
        return self._L.pop(0)
    def peek(self):
        return self._L[0]
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self._L) == 0
#Queue Linked List 
class Queue_LL:                 
    def __init__(self): 
        self._LL = LinkedList()
        self.len = 0
    def enqueue(self,item):
        self._LL.add_last(item)
        self.len += 1
    def dequeue(self):
        return self._LL.remove_first()
        self.len -= 1
    def peek(self):
        if self._LL._head is not None:
            return self._LL._head.data
        else:
            return None
    def __len__(self):
        return self.len
    def isempty(self):
        return len(self) ==0

if __name__ == '__main__':
    ##########Test Stack_L##########
    stack1 = Stack_L()
    for i in range(10):
        stack1.push(i)
    for i in range(9,-1,-1):
        assert stack1.pop() == i
    ##########Test Stack_LL#########
    stack_2 = Stack_LL()
    for i in range(10):
        stack_2.push(i)
    for i in range(9,-1,-1):
        assert stack_2.pop() == i
        

    ##########Test Queue_L##########
    queue1 = Queue_L()
    for i in range(10):
        queue1.enqueue(i)
    for i in range(10):
        assert queue1.dequeue() == i
         

    ##########Test Queue_LL#########
    queue2 = Queue_L()
    for i in range(10):
        queue2.enqueue(i)
    for i in range(10):
        assert queue2.dequeue() == i



      