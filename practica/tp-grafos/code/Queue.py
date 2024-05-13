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
            while current.next :
                current
            current.next = current.next.next
        return None
