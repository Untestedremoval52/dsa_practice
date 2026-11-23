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
    def max_path_sum(root):
        max_sum = -math.inf
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)
            current_path = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path)
            return node.val + max(left_gain, right_gain)
        helper(root)
        return max_sum