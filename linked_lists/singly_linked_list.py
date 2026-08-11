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
if __name__ == "__main__":
    sll = Singly_Linked_List()
    sll.head = Node(10)
    sll.head.next = Node(20)
    sll.head.next.next = Node(30)
    sll.display_list()
    print(sll.list_length())