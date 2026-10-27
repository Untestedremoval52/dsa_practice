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
def max_depth(self, node):
    if not node:
        return 0
    left = max_depth(node.left)
    right = max_depth(node.right)
    return 1 + max(left, right)