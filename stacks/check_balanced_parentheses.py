from collections import deque
def check_balanced_parentheses(expression) -> bool:
    stack = deque()
    pairs = {")" : "(", "}" : "{", "]" : "["}
    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            pair = pairs[ch]
            if (not stack) or pair != stack.pop():
                return False
    return len(stack) == 0
if __name__ == "__main__":
    print(check_balanced_parentheses("({[]})"))
    print(check_balanced_parentheses("([)]"))
    print(check_balanced_parentheses("((("))
    print(check_balanced_parentheses(")("))
    print(check_balanced_parentheses(""))