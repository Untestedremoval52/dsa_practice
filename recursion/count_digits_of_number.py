def count_digits_of_number(num):
    if num <= 0:
        return 0
    return 1 + count_digits_of_number(num // 10)
if __name__ == "__main__":
    print(count_digits_of_number(570))