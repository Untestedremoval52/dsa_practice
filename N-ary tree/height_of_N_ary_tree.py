class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def height(node):
        if not node:
            return 0
        heights = []
        for child in node.children:
            heights.append(node.height(child))
        return 1 + max(heights, default = 0)