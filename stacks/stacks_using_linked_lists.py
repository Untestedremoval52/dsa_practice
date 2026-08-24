class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class StackLinkedList:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def display(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print()
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        print(f"The pushed element is: {data}")
        self.display()
    def pop(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.display()
        return popped
    def peek(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return None
        print(f"The peek element is: {self.top.data}")
        return self.top.data
if __name__ == "__main__":
    s = StackLinkedList()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())
    print(s.peek())