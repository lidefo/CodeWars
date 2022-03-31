'''
5 kyu

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

https://www.codewars.com/kata/54a91a4883a7de5d7800009c
'''


def increment_string(strng):
    if not strng: return '1'   # empty string
    if not strng[-1].isdigit(): return strng + '1'   # string without digit
    if strng[-1] in '012345678': return strng[:-1] + str(int(strng[-1]) + 1)   # if strng[-1] in '012345678'
    digitcount = sum([strng.count(c) for c in '0123456789'])
    if strng.isdigit():   # strng is digit
        for i in range(1, len(strng) + 1):
            if strng[-i] != '0':
                toreturn = strng[:-i + 1] + str(int(strng[-i + 1:]) + 1)
                newdigitcount = sum([toreturn.count(c) for c in '0123456789'])
                if digitcount == newdigitcount: return toreturn
                return strng[:-i + 1] + ('0' * (digitcount - newdigitcount)) + str(int(strng[-i + 1:]) + 1)

    for i in range(1, len(strng) + 1):
        if not strng[-i].isdigit():
            toreturn = strng[:-i + 1] + str(int(strng[-i + 1:]) + 1)
            newdigitcount = sum([toreturn.count(c) for c in '0123456789'])
            if digitcount == newdigitcount: return toreturn
            return strng[:-i + 1] + ('0' * (digitcount-newdigitcount)) + str(int(strng[-i + 1:]) + 1)
