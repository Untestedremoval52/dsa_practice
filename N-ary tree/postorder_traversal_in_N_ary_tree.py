class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def postorder_traversal(self, node):
        if not node:
            return node
        for child in node.children:
            self.postorder_traversal(child)
        print(node.val, end = " ")