'''
5 kyu

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format
(HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

https://www.codewars.com/kata/52685f7382004e774f0001f7
'''


def make_readable(seconds):
    HH = str(seconds // 3600) + ':'
    if len(HH) != 3:
        HH = '0' + HH
    MM = str((seconds - (seconds // 3600) * 3600) // 60) + ':'
    if len(MM) != 3:
        MM = '0' + MM
    SS = str(((seconds - (seconds // 3600) * 3600) % 60))
    if len(SS) != 2:
        SS = '0' + SS
    return HH + MM + SS
