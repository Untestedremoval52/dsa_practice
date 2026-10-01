def first_non_repeating_character(text):
    freq = dict()
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    for k, v in freq.items():
        if v == 1:
            return k
    return None