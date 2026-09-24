def printing_numbers(num):
    if num <= 0:
        return
    print(num, end = " ")
    printing_numbers(num - 1)
if __name__ == "__main__":
    printing_numbers(7)