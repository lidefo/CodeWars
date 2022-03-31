'''
5 kyu

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

https://www.codewars.com/kata/52597aa56021e91c93000cb0
'''


def move_zeros1(array):   # 1st solution
    n, arraytemp = len(array), array.copy()
    for c in arraytemp:
        if c == 0:
            array.remove(c)
    while len(array) != n:
        array.append(0)
    return array


def move_zeros2(array):   # 2nd solution
    out, counter = [], 0
    for elem in array:
        if elem == 0:
            counter += 1
        else:
            out.append(elem)
    return out + [0] * counter


def move_zeros3(array):   # 3rd solution
    out = [elem for elem in array if elem != 0]
    return out + [0] * (len(array) - len(out))
