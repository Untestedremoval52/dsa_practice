from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def level_order_traversal(node):
        if not node:
            return node
        q = deque([node])
        while q:
            curr = q.popleft()
            print(curr.val, end = " ")
            for child in curr.children:
                q.append(child)