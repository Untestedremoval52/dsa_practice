def counts_vowels_and_consonants(string):
    c1, c2 = 0, 0
    for char in string:
            if char.isalpha() == True and char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                c1 += 1
            elif char.isalpha() == True and char not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                c2 += 1
    return c1, c2
string = input("Enter a string: ")
vowels, consonants = counts_vowels_and_consonants(string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)