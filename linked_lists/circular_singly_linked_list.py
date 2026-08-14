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
cll = Circular_Singly_Linked_List()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)