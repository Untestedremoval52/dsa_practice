def find_duplicates(arr):
    slow = arr[0]
    fast = arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow