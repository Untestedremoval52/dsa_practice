class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Circular_Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
    def is_empty(self):
        return self.head is None
    def display_list(self):
        if self.is_empty() == True:
            print("The list is empty")
        else:
            current_node = self.head
            while True:
                print(current_node.data, end = " ")
                current_node = current_node.next
                if current_node == self.head:
                    break
            print()
    def insert_beginning(self, value):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = node
            node.next = self.head
            self.head = node
        self.length +=1
        self.display_list()
    def insert_end(self, value):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            node.next = self.head
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = node
            node.next = self.head
        self.length += 1
        self.display_list()
    def insert_middle(self, value, position):
        node = Node(value)
        if self.is_empty() == True:
            self.head = node
            node.next = self.head
            self.length += 1
        elif position < 0 or position > self.length:
            print("Invalid input given, please try again later!")
        elif position == 0:
            self.insert_beginning(value)
        elif position == self.length:
            self.insert_end(value)
        else:
            current_node = self.head
            for i in range (position - 1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length += 1
        self.display_list()
    def search_element(self, key):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        position = 0
        current_node = self.head
        while True:
            if current_node.data == key:
                print(f"{key} was found at position {position}")
                return
            position += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        print(f"{key} was not found in the given list")
    def delete_beginning(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        if self.length == 1:
            self.head = None
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            self.head = self.head.next
            current_node.next = self.head
            self.length = self.length - 1
    def delete_end(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        if self.length == 1:
            self.head = None
        else:
            p = self.head
            q = None
            while p.next != self.head:
                q = p
                p = p.next
            q.next = self.head
            p.next = None
        self.length -= 1
        self.display_list()