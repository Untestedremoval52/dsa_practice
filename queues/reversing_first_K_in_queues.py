from collections import deque
def reverse_first_k_elements(q, k):
    stack = deque()
    result_queue = deque()
    if k < 0 or k > len(q):
        print("k is invalid, please try again!")
        return q
    for _ in range(k):
        stack.append(q.popleft())
    while stack:
        result_queue.append(stack.pop())
    while q:
        result_queue.append(q.popleft())
    return result_queue