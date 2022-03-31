'''
3 kyu

Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a
valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing
several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field.
The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version.
In this kata we will use Soviet/Russian version of the game.

https://i.imgur.com/IWxeRBV.png

Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game,
visit this link(http://en.wikipedia.org/wiki/Battleship_(game)).

https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
'''


def check_ships(field):
    count_of_4ceil = 0
    count_of_3ceil = 0
    count_of_2ceil = 0
    for row in field:
        row = ''.join(row).split('0')
        if '1111' in row:
            count_of_4ceil += 1
        if '111' in row:
            count_of_3ceil += 1
        if '11' in row:
            count_of_2ceil += 1

   # print(count_of_4ceil, count_of_3ceil, count_of_2ceil, sep='|||')
    if count_of_4ceil > 1 or count_of_3ceil > 2 or count_of_2ceil > 3:
        return False
    return True


def validate_battlefield(field):
    str_field = []
    for row in field:
        str_field.append(list(map(str, row)))
    field = str_field

    coordinates_of_ones = []
    for i in range(10):
        for j in range(10):
            if field[i][j] == '1':
                coordinates_of_ones.append([i, j])
    if len(coordinates_of_ones) != 20:
        return False

    for coordinate in coordinates_of_ones:
        if [coordinate[0] + 1, coordinate[1] + 1] in coordinates_of_ones or [coordinate[0] + 1, coordinate[1] - 1] in coordinates_of_ones:
            return False
        elif [coordinate[0] - 1, coordinate[1] - 1] in coordinates_of_ones or [coordinate[0] - 1,coordinate[1] + 1] in coordinates_of_ones:
            return False

    if not check_ships(field):
        return False

    rotated_field = list(zip(*field[::-1]))
    for i in range(10):
        rotated_field[i] = list(rotated_field[i])

    if not check_ships(rotated_field):
        return False

    return True
