# Problem
# Merge Intervals
# Merge overlapping intervals from 2 sets


def mergeIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    output = [intervals[0]]

    for start,end in intervals[1:]:
        lastend = output[-1][1]

        if start <= lastend:
            output[-1][1] = max(lastend,end)
        else:
            output.append([start,end]) 

    return output

# Driver code
intervals = [[1,3],[2,6],[5,10],[15,18]]
print(mergeIntervals(intervals))