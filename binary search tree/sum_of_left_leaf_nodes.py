import math
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = 0
        self.right = 0
class MyBST:
    def __init__(self):
        self.root = None
    def construct_tree(self):
        self.root = TreeNode(40)
        self.root.left = TreeNode(30)
        self.root.right = TreeNode(50)
        self.root.left.left = TreeNode(25)
        self.root.left.right = TreeNode(50)
    def sum_of_left_leaf_nodes(root):
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        total += root.sum_of_left_leaf_nodes(root.left)
        total += root.sum_of_left_leaf_nodes(root.right)
        return total