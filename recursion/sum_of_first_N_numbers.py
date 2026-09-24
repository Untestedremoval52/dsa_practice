def sum_of_first_N_numbers(num):
    if num <= 0:
        return 0
    return num + sum_of_first_N_numbers(num - 1)
if __name__ == "__main__":
    print(sum_of_first_N_numbers(10))