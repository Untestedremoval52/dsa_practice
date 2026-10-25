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
def preorder_traversal(node):
    if not node:
        return
    print(node.val, end = " ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)