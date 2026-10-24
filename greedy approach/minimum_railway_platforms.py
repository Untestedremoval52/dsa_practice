def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    i, j = 0, 0
    curr_platforms = 0
    result = 0
    while i <= len(arrivals):
        if arrivals[i] <= departures[j]:
            curr_platforms += 1
            result = max(result, curr_platforms)
            i += 1
        else:
            curr_platforms -= 1
            j += 1
    return result