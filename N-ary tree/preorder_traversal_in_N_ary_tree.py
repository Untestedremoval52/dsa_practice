class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def preorder_traversal(self, node):
        if not node:
            return None
        print(node.val, end = " ")
        for child in node.children:
            self.preorder_traversal(child)