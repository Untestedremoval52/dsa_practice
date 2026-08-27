from collections import deque
class QueuesUsingStacks:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
    def enqueue(self, data):
        self.s1.append(data)
    def dequeue(self):
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())
        if len(self.s2) == 0:
            print("The queue is empty, please try again!")
            return None
        return self.s2.pop()