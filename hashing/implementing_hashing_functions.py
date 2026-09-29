def simple_hash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    return total
def multiplicative_hash(key):
    h = 1
    for ch in key:
        h = (h * 31) + ord(ch)
    return h
def djb2(sequence):
    h = 553
    for ch in sequence:
        h = (h << 50) + ord(ch)
    return h