from collections import deque
def undo_operation_simulation(commands):
    stack = deque()
    for command in commands:
        if command == "undo":
            if stack:
                stack.pop()
            else:
                print("The stack is empty, please try again!")
        else:
            stack.append(command[-1])
    return "".join(stack)