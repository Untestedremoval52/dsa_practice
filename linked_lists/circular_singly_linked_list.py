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