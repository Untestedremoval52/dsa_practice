def binary_seach(array, target, low, high):
    while low <= high:
        mid = (low + (high - low)) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
def exponential_search(array, target):
    if array[0] == target:
        return 0
    i = 1
    n = len(array)
    while (i < n) and (array[i] <= target):
        i *= 2
    low = i // 2
    high = min(i, n - 1)
    print(f"Target: {target}")
    print(f"Range: ({low}, {high})")
    return binary_seach(array, target, low, high)