def count_occurences(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter some numbers (seperate them by spaces): ").split()]
    target = int(input("Enter a number to check its occurences: "))
    print(f"{target} has been found for {count_occurences(nums, target)} times")