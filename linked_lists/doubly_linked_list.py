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
    def insert_middle(self, value, position):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            self.tail = node
            self.length += 1
        elif position < 0 or position > self.length:
            print("Invalid input given, please try again!")
        elif position == 0:
            self.insert_beginning(value)
        elif position == self.length:
            self.insert_end(value)
        else:
            p = self.head
            for _ in range (position):
                p = p.next
            q = p.prev
            q.next = node
            node.prev = q
            node.next = p
            p.prev = node
            self.length += 1
            self.display_forward()
    def search_element(self, key):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        position = 0
        current_node = self.head
        while current_node:
            if current_node.data == key:
                print(f"{key} was found at {position} location")
                return
            position += 1
            current_node = current_node.next
        print(f"{key} not found in the list")
    def delete_beginning(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
        else:
            if self.length == 1:
                self.head = None
                self.tail = None
            elif self.length > 1:
                current_node = self.head
                self.head = self.head.next
                self.head.prev = None
                current_node.next = None
            self.length -= 1
        self.display_forward()