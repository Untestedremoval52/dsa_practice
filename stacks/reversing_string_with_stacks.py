from collections import deque
def reversing_string_using_stack(string):
    stack = deque()
    result = ""
    for ch in string:
        stack.append(ch)
    while stack:
        result += stack.pop()
    return result
if __name__ == "__main__":
    string = "abracadabra"
    str = reversing_string_using_stack(string)
    print(str)