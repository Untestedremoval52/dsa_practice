def palindrome_test(string):
    string = string.lower()
    for i in range (len(string)):
        if string[i] != string[-i - 1]:
            return False
    return True
string = input("Enter a string: ")
print("Is the given input string a palindrome?", palindrome_test(string))