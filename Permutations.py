'''
4 kyu

In this kata you have to create all permutations of a non empty input string and remove duplicates, if present.
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

https://www.codewars.com/kata/5254ca2719453dcc0b00027d
'''


from itertools import permutations as perm


def permutations(string):
    return [''.join(combination) for combination in set(perm(string, len(string)))]
