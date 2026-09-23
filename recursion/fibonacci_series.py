def fibonacci_series(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci_series(num - 1) + fibonacci_series(num - 2)
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = fibonacci_series(num)
    print(f"The {num}th term in the Fibonacci series is: {result}")