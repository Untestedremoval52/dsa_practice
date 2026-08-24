class Stack:
    def __init__(self):
        self.stack = []
    def get_length(self):
        return len(self.stack)
    def is_empty(self):
        return True if self.get_length() == 0 else False
    def display_stack(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        else:
            for element in self.stack[::-1]:
                print(element)
    def push(self, data):
        self.stack.append(data)
        self.display_stack()
    def pop(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return None
        return self.stack.pop()
    def peek(self):
        if self.is_empty() == True:
            print("The list is empty, please try again!")
            return
        else:
            print(f"The top of the given stack is: {self.stack[-1]}")
if __name__ == "__main__":
    s = Stack()
    s.pop()
    s.peek()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())
    s.peek()
    print(s.get_length())