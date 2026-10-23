from collections import Counter
def top_frequent(arr, k):
    freq = Counter(arr)
    return sorted(freq, key = lambda x: freq[x], reverse = True)[ : k]