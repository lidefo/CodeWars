'''
4 kyu

Complete the function/method (depending on the language) to return true/True when its argument is an array that has
the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

https://www.codewars.com/kata/520446778469526ec0000001
'''


def same_structure_as(original, other):
    if type(original) != type(other) or len(original) != len(other):
        return False

    for i in range(len(original)):
        if type(original[i]) != type(other[i]):
            return False

        if isinstance(original[i], list):
            if not same_structure_as(original[i], other[i]):
                return False

    return True
