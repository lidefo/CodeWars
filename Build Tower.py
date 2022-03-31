'''
6 kyu

Build Tower
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)

https://www.codewars.com/kata/576757b1df89ecf5bd00073b
'''


def tower_builder(n_floors):
    len_of_floor = n_floors * 2 - 1
    res = []
    for i in range(1, n_floors * 2, 2):
        res.append(' ' * ((len_of_floor - i) // 2) + '*' * i + ' ' * ((len_of_floor - i) // 2))
    return res
