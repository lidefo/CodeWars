'''
5 kyu

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

https://www.codewars.com/kata/513e08acc600c94f01000001
'''


def rgb(r, g, b):
    rgblist = [r,g,b]
    for i in range(len(rgblist)):
        if rgblist[i] < 0: rgblist[i] = 0
        elif rgblist[i] > 255: rgblist[i] = 255
    r, g, b = list(map(lambda x: '0' + hex(x)[2:] if len(hex(x)[2:]) < 2 else hex(x)[2:], rgblist))
    return (r+g+b).upper()
