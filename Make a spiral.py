'''
3 kyu

Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s.
For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
'''


# I stole this solution

def spiralize(size):
    turn_direction = {
        'right': 'down',
        'down': 'left',
        'left': 'up',
        'up': 'right'
    }

    move_to = {
        'right': [0, 1],
        'down': [1, 0],
        'left': [0, -1],
        'up': [-1, 0]
    }

    matrix = [[0] * size for _ in range(size)]
    length = size
    pos = [0, 0]
    dir = "right"
    for i in range(size):
        move = move_to[dir]
        for j in range(length):
            matrix[pos[0] + move[0] * j][pos[1] + move[1] * j] = 1
        pos[0] += move[0] * (length - 1)
        pos[1] += move[1] * (length - 1)
        if i != 0 and i % 2 == 0:
            length -= 2
        dir = turn_direction[dir]
    return matrix
