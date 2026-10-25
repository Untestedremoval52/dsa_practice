class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class MyBST:
    def __init__(self):
        self.root = None
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end = " ")
        self.inorder(root.right)
    def searching(self, node, key):
        if not node or node.val == key:
            return node
        if key < node.val:
            return self.searching(node.left, key)
        return self.searching(node.right, key)