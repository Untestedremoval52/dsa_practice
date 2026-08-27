class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class QueuesUsingLinkedLists:
    def __init__(self):
        self.rear = None
        self.front = None
    def is_empty(self):
        return self.front is None
    def display(self):
        if self.is_empty() == True:
            print("The queue is empty, please try again!")
            return
        current_node = self.front
        while current_node:
            print(current_node.data, end = " ")
            current_node = current_node.next
        print()
    def enqueue(self, data):
        node = Node(data)
        if self.is_empty() == True:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.display()
    def dequeue(self):
        if self.is_empty() == True:
            print("The queue is empty, please try again!")
        current_node = self.front
        self.front = current_node.next
        if not self.front:
            self.rear = None
        popped = current_node.data
        self.display()
        return popped
    def frontpeek(self):
        if self.is_empty() == True:
            print("The queue is empty, please try again!")
            return
        return self.front.data
    def rearpeek(self):
        if self.is_empty() == True:
            print("The queue is empty, please try again!")
            return
        return self.rear.data