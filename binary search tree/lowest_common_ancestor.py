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
    def lowest_common_ancestor(root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root