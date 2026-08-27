class QueuesUsingLists:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        print(self.queue)
    def enqueue(self, data):
        self.queue.append(data)
        self.display()
    def dequeue(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        popped = self.queue.pop(0)
        self.display()
        return popped
    def frontpeek(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        return self.queue[0]
    def rearpeek(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        return self.queue[-1]