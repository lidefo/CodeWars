'''
5 kyu

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

https://www.codewars.com/kata/514a024011ea4fb54200004b
'''


def domain_name(url):
    splitted = url.split('/')
    if len(splitted) > 2:
        domain = splitted[2].split('.')
    else:
        if splitted[0].split('.'):
            domain = splitted[0].split('.')
        else:
            domain = splitted[3].split('.')
    return max(domain, key=len)
