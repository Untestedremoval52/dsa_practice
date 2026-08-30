def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swap = False
        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            break
    return array