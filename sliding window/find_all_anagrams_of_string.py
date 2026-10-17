from collections import Counter
def find_the_anagrams(s, p):
    p_counts = Counter(p)
    window_counts = Counter()
    result = []
    left = 0
    for right in range(len(s)):
        window_counts[s[right]] += 1
        if (right - left + 1) == len(p):
            if window_counts == p_counts:
                result.append(left)
            window_counts[s[left]] -= 1
            if window_counts[s[left]] == 0:
                del window_counts[s[left]]
            left += 1
    return result