def two_sum_of_array(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return (left, right)
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []