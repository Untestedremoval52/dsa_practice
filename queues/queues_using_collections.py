from collections import deque
class QueuesUsingCollections:
    def __init__(self):
        self.queue = deque()
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        if self.is_empty() == True:
            print("The queue is empty, please try again!")
        else:
            print(self.queue)
    def enqueue(self, data):
        self.queue.append(data)
        self.display()
    def dequeue(self):
        if self.is_empty() == True:
            print("The queue is empty, please try again!")
            return
        popped = self.queue.popleft()
        self.display()
        return popped
    def frontpeek(self):
        if self.is_empty == True:
            print("The queue is empty, please try again!")
            return
        return self.queue[0]
    def rearpeek(self):
        if self.is_empty == True:
            print("The queue is empty, please try again!")
            return
        return self.queue[-1]