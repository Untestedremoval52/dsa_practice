class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Singly_Linked_List:
    def __init__(self):
        self.head = None
    def list_length(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length
    def display_list(self):
        if self.head == None:
            print("List is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end=" ")
                current_node = current_node.next
            print()
    def insert_beginning(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.display_list()
    def insert_end(self, value):
        new_node = Node(value)
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node
        self.display_list()
