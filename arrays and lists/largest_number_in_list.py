def find_largest(nums):
    largest = nums[0]
    for i in range (1, len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter some numbers (seperate them by spaces): ").split()]
    print(f"The largest number in the given list is: {find_largest(nums)}")