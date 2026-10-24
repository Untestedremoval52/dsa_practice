def search_occurence(arr, target):
    def first_index():
        left, right = 0, len(arr) - 1
        index = -1
        while left <= right:
            mid = (right + left) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if arr[mid] == target:
                index = mid
        return index
    def last_index():
        left, right = 0, len(arr) - 1
        index = -1
        while left <= right:
            mid = (right + left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if arr[mid] == target:
                index = mid
        return index
    return [first_index(), last_index()]