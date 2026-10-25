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
def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val, end = " ")