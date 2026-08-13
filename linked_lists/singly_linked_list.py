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
    def insert_middle(self, position, value):
            length = self.list_length()
            if position < 0 or position > length:
                print("Invalid input given, Try again!")
            elif position == 0:
                self.insert_beginning(value)
            elif position == length:
                self.insert_end(value)
            else:
                new_node = Node(value)
                p = self.head
                q = None
                for i in range(position):
                    q = p
                    p = p.next
                q.next = new_node
                new_node.next = p
                self.display_list()
    def search_element(self, value):
        if self.head == None:
            print("The given list is empty, please try again!")
        else:
            position = 0
            current_node = self.head
            while current_node:
                if current_node.data == value:
                    print(f"Element {value} found at position {position}")
                    return
                current_node = current_node.next
                position += 1
                print(f"Element {value} not found in the list")
    def delete_beginning(self):
        if self.head != None:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None
        else:
            print("The list is empty, please try again!")