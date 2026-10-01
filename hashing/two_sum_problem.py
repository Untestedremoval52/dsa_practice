def two_sum(list, target):
    seq = set()
    for x in list:
        if (target - x) in seq:
            return (x, target - x)
        seq.add(x)
    return None