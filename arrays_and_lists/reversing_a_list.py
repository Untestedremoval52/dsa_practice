def list_reversal(nums):
    n = len(nums)
    reversed_list = []
    for num in range (n - 1, -1, -1):
        reversed_list.append(nums[num])
    return reversed_list
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter some numbers (seperate them by spaces): ").split()]
    print(f"The reversed string for the given original list is: {list_reversal(nums)}")