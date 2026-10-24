def can_jump(arr):
    farthest = 0
    for i in (len(arr)):
        if i > farthest:
            return False
        farthest = max(farthest, i + arr[i])
    return True