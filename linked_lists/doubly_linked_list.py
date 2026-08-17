class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def is_empty(self):
        return self.head is None
    def display_forward(self):
        if self.is_empty():
            print("The given list is empty!")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end = " <---> " if current_node.next else "\n")
                current_node = current_node.next
    def display_backward(self):
        if self.is_empty():
            print("The given list is empty!")
        else:
            current_node = self.tail
            while current_node:
                print(current_node.data, end = " <---> " if current_node.prev else "\n")
                current_node = current_node.prev
    def insert_beginning(self, value):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        self.display_forward()
    def insert_end(self, value):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        self.display_forward()