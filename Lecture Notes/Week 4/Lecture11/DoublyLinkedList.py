class Node:
    def __init__(self, _item, _next=None, _prev=None):
        self._item = _item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        p = self._prev._item if self._prev else None
        n = self._next._item if self._next else None
        return f"Node({self._item}, prv={p}, nxt={n})"


class DoublyLinkedList:
    def __init__(self):
        """Initializes empty DLL"""
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self, item):
        """Adds item to beginning of DLL"""
        new_node = Node(item, _next =self.head)
        if len(self) == 0:
            new_node = Node(item)
            self._head = new_node
            self._tail =  new_node
            self._len +=1
            return
        else:
           # create a new code w/ next -> old head 
           #update old hea'd prev pointer
           #update DLL._head
            self._head._prev = new_node  #updat eold heads previous pointer 
            self._head = new_node # update DLL head 

        self._len += 1 
        #to leanr implement doubly linked lsit from scratch 
    def add_last(self, item):
        """Adds item to end of DLL"""
       
    def remove_first(self):
        """Removes and returns first item in DLL"""
        #same as remove las and then just switch out tail and headb 
        #practice the code and start things from scratch
    def remove_last(self):
        """Removes and returns last item in DLL"""
# EDGE CASE
#EMPTY DLL
        if len(self) ==0: raise RuntimeError("Cannot remove_last from empty DLL")

        #edge case - 1 item in DLL
        if len(self) == 1:
            data = self._tail_item
            self._head = None
            self._tail = None
            self._len -= 1
            return data 
        #general case
        else:
            data = data._tail._item
            penultimate - self._tail._prev
            penultimate._next = None

            
            self._tail._prev._next = None #Update Penultimatre._next to none
            self._head._prev._nect = None 
    def __len__(self):
        """Returns the number of nodes in the DLL"""
        return self._len


