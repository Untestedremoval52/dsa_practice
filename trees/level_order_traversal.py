from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
def level_order_traversal(node):
    if not node:
        return
    q = deque([node])
    while q:
        curr = q.popleft()
        print(curr.val, end = " ")
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)