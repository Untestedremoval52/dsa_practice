class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def is_empty(self):
        return self.head is None
    def display_forward(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        current_node = self.head
        while True:
            print(current_node.data, end = " ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()
    def display_backward(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        current_node = self.tail
        while True:
            print(current_node.data, end = " ")
            current_node = current_node.prev
            if current_node == self.tail:
                break
        print()
    def insert_beginning(self, value):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node
        self.length += 1
        self.display_forward()
    def insert_end(self, value):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            self.head.prev = node
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        self.display_forward()
    def insert_middle(self, value, position):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            self.tail = node
            node.prev = node
            node.next = node
            self.length += 1
        elif position < 0 or position > self.length:
            print("Invalid input given, please try again!")
        elif position == 0:
            self.insert_beginning(value)
        elif position == self.length:
            self.insert_end(value)
        else:
            p = self.head
            for _ in range(position):
                p = p.next
            q = p.prev
            q.next = node
            node.next = p
            p.prev = node
            node.prev = q
            self.length += 1
        self.display_forward()