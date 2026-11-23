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
    def kth_smallest(node, k):
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right