
Abstract Data Types
Tells users what they can do with an object but it does not specify how it is done, sopecifices how a user should do a function.

ADT:
Stack
Queue
Deck
ordered list
Priority Queue 
Mapping 
Graphs

Data Strucutures:
Lists
Sets
Dictionaries
New:
Linked List
Double Linked List 
Shos how the data is strucured on the computer 

Stack ADT:
Push (item):
adds item to the top of a stack
pop():
returns the top item

s = start()
s.push('apple')
s.push([1,2,3])
s.push(1)

s.pop() --> loses the top item  --> Becomes 
                                    [1,2,3]
                                    apple

Stack --> Last one in, first one out (LIFO)

1 (on top now)
[1,2,3]
"apple"

#example: 
If you type hello and then bold h,

the first undo, would take away the bold, and then the word itself, so each action


#Queue

Has the FIFO (first In, First Out)

    enqueue --> adds item to my queue 
    dequeue --> eremoves and returns the first item in my queue

Q = Queue()s
q.enqueue(1)
q.enqueue('apple')
q.enqueue([1,2,3])
q,dequeue() --> take out the first one (1)


to make a dequeue quicker:
self._L.insert(0,item)

self._L.pop()


Linked Lists:
#store a series of nodes and each node conrains whatever item it needs and a pointer to the next item
Attributes:
keeep track of the head
keep track of length (number of nodes)

Node:
item and a pointer to the next item

add_first()
add_last()
remove_first() coded in
remove_last() coded in