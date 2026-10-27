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
def sum_of_nodes(self, node):
    if not node:
        return 0
    left_sum = sum_of_nodes(node.left)
    right_sum = sum_of_nodes(node.right)
    return node.val + left_sum + right_sum