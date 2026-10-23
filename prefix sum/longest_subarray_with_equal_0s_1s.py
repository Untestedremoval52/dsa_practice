def longest_sub_array(arr):
    prefix_sum = 0
    longest = 0
    first_occ = {0 : -1}
    for i, num in enumerate(arr):
        prefix_sum += 1 if num == 1 else -1
        if prefix_sum in first_occ:
            longest = max(longest, i - first_occ[prefix_sum])
        else:
            first_occ[prefix_sum] = i
    return longest