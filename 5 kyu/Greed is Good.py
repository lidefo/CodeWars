'''
5 kyu

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw
according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
(contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
In some languages, it is possible to mutate the input to the function. This is something that you should never do.
If you mutate the input, you will not be able to pass all the tests.

https://www.codewars.com/kata/5270d0d18625160ada0000e4
'''


def score1(dice):   # 1st solution
    one = dice.count(1) // 3 * 1000 + dice.count(1) % 3 * 100
    two = dice.count(2) // 3 * 200
    three = dice.count(3) // 3 * 300
    four = dice.count(4) // 3 * 400
    five = dice.count(5) // 3 * 500 + dice.count(5) % 3 * 50
    six = dice.count(6) // 3 * 600
    return sum([one,two,three,four,five,six])


def add_score(dice, item, value):   # 2nd solution
    scores = 0
    while item in dice:
        dice = dice.replace(item, '', 1)
        scores += value
    return [dice, scores]


def score2(dice):
    dice = [str(i) for i in sorted(dice)]
    amount = 0
    dice = ''.join(dice)
    value_board = {
        '111': 1000,
        '222': 200,
        '333': 300,
        '444': 400,
        '555': 500,
        '666': 600,
        '1': 100,
        '5': 50
    }
    for key in value_board:
        dice, value = add_score(dice, key, value_board[key])
        amount += value
    return amount


def score3(dice):   # 3rd solution
    dice = [str(i) for i in sorted(dice)]
    amount = 0
    dice = ''.join(dice)
    value_board = {
        '111': 1000,
        '222': 200,
        '333': 300,
        '444': 400,
        '555': 500,
        '666': 600,
        '1': 100,
        '5': 50
    }
    for key in value_board:
        while key in dice:
            dice = dice.replace(key, '', 1)
            amount += value_board[key]
    return amount
