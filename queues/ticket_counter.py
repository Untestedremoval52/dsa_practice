from collections import deque
def find_last_person(n, k):
    if n == 1:
        return n
    q = deque()
    for i in range (1, n + 1):
        q.append(i)
    while True:
        for _ in range(k):
            q.popleft()
            if len(q) == 1:
                return q[0]
        for _ in range(k):
            q.pop()
            if len(q) == 1:
                return q[0]