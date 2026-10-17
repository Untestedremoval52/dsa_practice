def max_sum_subarray(arr, key):
    result = float('-inf')
    window_sum = 0
    left =  0
    for right in range(len(arr)):
        window_sum = arr[right]
        if (right - left + 1) == key:
            result = max(window_sum, result)
            window_sum -= arr[left]
            left += 1
    return result