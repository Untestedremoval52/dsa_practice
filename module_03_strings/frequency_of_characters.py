def frequency_of_characters(string):
    count = dict()
    for char in string:
        if char.isalpha() == True:
            count[char.lower()] = count.get(char.lower(), 0) + 1
    return count
if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Frequency of characters:", frequency_of_characters(string))