def count_sort(array):
    max_value = max(array)
    count_array = [0] * (max_value + 1)
    for element in array:
        count_array[element] += 1
    result = []
    for i in range(len(count_array)):
        result.extend([i] * count_array[i])
    return result