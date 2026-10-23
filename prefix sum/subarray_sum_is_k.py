def subarray_sum(arr, k):
    count = 0
    prefix_sum = 0
    freq = {0 : 1}
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count