class LinearProbingHashing:
    def __init__(self, size = 5):
        self.size = size
        self.table = [None] * self.size
    def display(self):
        print(self.table)
    def hash_function(self, key):
        return sum(ord(ch) for ch in key) % self.size
    def insert(self, key):
        h = self.hash_function(key)
        for i in range (self.size):
            index = (h + i) % self.size
            if self.table[index] == None:
                self.table[index] = key
                return True
        raise Exception("Hash Table is full!")
    def search(self, key):
        h = self.hash_function(key)
        for i in range (self.size):
            index = (h + i) % self.size
            if self.table[index] == None:
                return False
            elif self.table[index] == key:
                return True
        return False