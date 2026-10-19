class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next
class Solution:
    def has_cycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False