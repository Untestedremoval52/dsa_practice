def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index
    return -1