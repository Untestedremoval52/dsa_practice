class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
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
    def search_middle_element(self):
        current_node = self.head
        length = self.list_length
        for _ in range(length // 2):
            current_node = current_node.next
        print(f"The middle element is {current_node.data}")
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
    def count_nodes(self):
        current_node = self.head
        count = 0
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        while True:
            current_node = current_node.next
            count += 1
            if current_node == self.head:
                break
        print(f"The total number of nodes are: {count}")
cdll = Circular_Singly_Linked_List()
cdll.count_nodes()
cdll.insert_beginning(10)
cdll.count_nodes()
cdll.insert_beginning(20)
cdll.insert_beginning(30)
cdll.count_nodes()