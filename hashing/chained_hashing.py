class ChainingHashTable:
    def __init__(self, size = 5):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    def hash_function(self, key):
        return sum(ord(ch) for ch in key) % self.size
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i} : {bucket}")
    def insert(self, key, value = None):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
        self.table[index].append((key, value))
        return
    def search(self, key):
        index = self.hash_function(key)
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None