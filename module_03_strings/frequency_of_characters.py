def frequency_of_characters(string):
    count = dict()
    for char in string:
        if char.isalpha() == True:
            count[char] = count.get(char, 0) + 1
    return count
string = input("Enter a string: ")
char_frequency = frequency_of_characters(string)
print("Frequency of characters:", char_frequency)
