'''
4 kyu

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
'''


def solution(args):
    res, ranges = [], []
    for i in range(1, len(args)):
        flag = False
        if args[i - 1] + 1 == args[i]:
            ranges.extend([args[i - 1], args[i]])
        else:
            if ranges:
                ranges = list(map(str, ranges))
                if len(ranges) > 2:
                    res.append(str(ranges[0]) + '-' + str(ranges[-1]))
                    ranges = []
                else:
                    res.extend(ranges)
                    ranges = []
            else:
                res.append(str(args[i - 1]))
            flag = True
    if flag:
        if ranges:
            if ranges[-1] + 1 == args[-1]:
                ranges.append(args[-1])
            else:
                res.append(str(args[-1]))
        else:
            res.append(str(args[-1]))
    if ranges:
        ranges = list(map(str, ranges))
        if len(ranges) > 2:
            res.append(str(ranges[0]) + '-' + str(ranges[-1]))
        else:
            res.extend(ranges)
    return ','.join(res)
