def min_days(bloom_days, m, k):
    if m * k > len(bloom_days):
        return -1
    def can_make(day):
        count = 0
        bouquets = 0
        for d in bloom_days:
            if d <= day:
                count += 1
            else:
                count = 0
            if count == k:
                bouquets += 1
                count = 0
        return bouquets >= m
    low, high = min(bloom_days), max(bloom_days)
    result = -1
    while low <= high:
        mid = (high + low) // 2
        if can_make(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result