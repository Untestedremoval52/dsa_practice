from collections import Counter
def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    map1 = dict()
    map2 = dict()
    for c1, c2 in zip(str1, str2):
        if (c1 in map1) and (map1[c1] != c2):
            return False
        if (c2 in map2) and (map2[c2] != c1):
            return False
        map1[c1] = c2
        map2[c2] = c1
    return True