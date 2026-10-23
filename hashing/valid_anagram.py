from collections import Counter
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)