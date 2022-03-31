'''
5 kyu

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

https://www.codewars.com/kata/520b9d2ad5c005041100000f
'''


def pig_it(text):
    return ' '.join([[c, c[1:] + c[0] + 'ay'][c not in '!/.,&?'] for c in text.split()])
