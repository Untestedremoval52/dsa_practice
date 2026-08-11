from frequency_of_characters import frequency_of_characters
str1 = input("Enter a string: ")
str1 = str1.lower()
str2 = input("Enter another string: ")
str2 = str2.lower()
if frequency_of_characters(str1) == frequency_of_characters(str2):
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.")