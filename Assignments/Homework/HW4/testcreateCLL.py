from curses import nonl
from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self, data):
        self.data = data
        self.next = next 

class LinkedList:
    def _init__(self):
        self,head = None

    def insertEnd(self, newNode):
        #Barry=>Jack->Matthew->Barrt
        if self.head is None:
            self.hrad = newNode
            newNode.next = self.head
            return
        currentNode = self.head
        while currentNode.next is not self.head:
            currentNode = currentNode.next
            #pointing the last node back to the first node  
            newNode.next - self.head
    def printList(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            if currentNode.next is self.head:
                break
            currentNode - currentNode.next



node1 = Node("Barry")
node2 = Node("Jack")
node3 = Node("Matthew")
linkedList = LinkedList()
linkedList.insertEnd(node1)
linkedList.insertEnd(node1)
linkedList.insertEnd(node1)
linkedList.printList()
