def aggressive_cows(stalls, cows):
    stalls.sort()
    def can_place(distance):
        placed = 1
        last = stalls[0]
        for pos in stalls[1:]:
            if pos - last >= distance:
                placed += 1
                last = pos
            if placed == cows:
                return True
        return False
    low, high = 1, stalls[-1] - stalls[0]
    result = 0
    while low <= high:
        mid = (high + low) // 2
        if can_place(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result