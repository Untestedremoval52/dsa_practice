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
sll = Singly_Linked_List()
sll.insert_beginning(10)
sll.insert_beginning(20)
sll.insert_beginning(40)
sll.insert_beginning(30)
sll.search_middle_element()