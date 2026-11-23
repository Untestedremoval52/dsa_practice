import math
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def find_max(node):
        if not node:
            return -math.inf
        res = node.val
        for child in node.children:
            res = max(res, node.find_max(child))
        return res