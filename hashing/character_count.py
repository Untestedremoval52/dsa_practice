def character_count(text):
    freq = dict()
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return