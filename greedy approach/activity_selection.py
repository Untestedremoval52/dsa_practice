def activity_selection(intervals):
    intervals.sort(key = lambda val : val[1])
    count = 0
    last_end = -float('inf')
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count