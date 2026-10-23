def count_subarrays(arr, k):
    count = 0
    prefix_sum = 0
    freq = {0 : 1}
    for num in arr:
        prefix_sum += num
        mod = prefix_sum % k
        if mod in freq:
            count += freq[mod]
        freq[mod] = freq.get(mod, 0) + 1
    return count