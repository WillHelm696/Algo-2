# Definir la clase Node
class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.next = None

# Definir la clase LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.parent=current

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        pos = 0
        current = self.head
        while current:
            pos += 1 
            if current.data == data:
                return pos
            current = current.next
        return None

    def delete(self, data):
        pos = 0
        current = self.head
        if current is None:
            return None
        if current.data == data:
            self.head = current.next
            return pos
        while current.next:
            pos =+ 1
            if current.next.data == data:
                current.next = current.next.next
                return pos
            current = current.next

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
