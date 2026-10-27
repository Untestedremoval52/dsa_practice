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
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end = " ")
        self.inorder(root.right)
    def is_valid_bst(root):
        def traverse(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (traverse(node.left, low, node.val) and traverse(node.right, node.val, high))
        return traverse(root, -math.inf, math.inf)