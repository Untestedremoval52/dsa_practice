def remove_duplicates(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter some numbers (seperated them by spaces): ").split()]
    print(f"The list after removing duplicates is: {remove_duplicates(nums)}")