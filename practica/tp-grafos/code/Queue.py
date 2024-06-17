from Linkedlist import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def dequeue(self):
        if self.head is not None:
            current = self.head
            if current.next is None:
                element=current.data
                self.head=self.head.next
            while current.next.next:
                current=current.next
                
            element = current.next.data
            current.next = current.next.next
            return element
        return None 