def power_function(num, power):
    if power <= 0:
        return 1
    return num * power_function(num, power - 1)
if __name__ == "__main__":
    print(power_function(7, 8))