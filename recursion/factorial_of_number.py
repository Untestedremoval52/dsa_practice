def factorial_of_number(num):
    if (num == 0) or (num == 1):
        return 1
    return num * factorial_of_number(num - 1)
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = factorial_of_number(num)
    print(f"The factorial of {num} is: {result}")