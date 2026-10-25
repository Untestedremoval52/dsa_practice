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
    def deletion(self, node, key):
        if not node:
            return None
        if key < node.val:
            node.left = self.deletion(node.left, key)
        elif key > node.val:
            node.right = self.deletion(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            succ = node.right
            while succ.left:
                succ = succ.left
            node.val = succ.val
            node.right = self.deletion(node.right, succ.val)
        return node