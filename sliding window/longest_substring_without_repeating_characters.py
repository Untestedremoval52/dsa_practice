def length_of_substring(string):
    character_set = set()
    max_length = 0
    left = 0
    for right in range(len(string)):
        while string[left] in character_set:
            character_set.remove(string[left])
            left += 1
        character_set.add(string[right])
        max_length = max(max_length, (right - left + 1))
    return max_length