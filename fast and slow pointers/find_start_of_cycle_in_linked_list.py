class Solution:
    def __init__(self):
        self.slow = None
        self.fast = None
    def has_cycle(self, head):
        self.slow, self.fast = head, head
        while self.fast and self.fast.next:
            self.slow = self.slow.next
            self.fast = self.fast.next.next
            if self.slow == self.fast:
                return True
        return False
    def start_cycle(self, head):
        if not self.has_cycle(self, head):
            return None
        self.slow = head
        while self.slow != self.fast:
            self.slow = self.slow.next
            self.fast = self.fast.next
            return self.slow