'''
5 kyu

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of
integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
 If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
'''


def max_sequence(arr):
    maximum = -100000
    if not arr:
        return 0
    for i in range(len(arr)):
        for g in range(i, len(arr)):
            if sum(arr[i:g + 1]) > maximum:
                maximum = sum(arr[i:g + 1])
    if maximum <= 0: 
        return 0
    else:
        return maximum
