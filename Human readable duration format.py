'''
4 kyu

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
 in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive
integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is
greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not
correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it
should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute
and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more
significant unit of time.

https://www.codewars.com/kata/52742f58faf5485cae000b9a
'''


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    s = []
    years = seconds // 31536000
    days = (seconds - years * 31536000) // 86400
    hours = (seconds - years * 31536000 - days * 86400) // 3600
    minutes = (seconds - years * 31536000 - hours * 3600 - days * 86400) // 60
    second = seconds - years * 31536000 - hours * 3600 - days * 86400 - minutes * 60
    if years:
        s.append(str(years) + ' ' + ['year', 'years'][years> 1])
    if days:
        s.append(str(days) + ' ' + ['day', 'days'][days > 1])
    if hours:
        s.append(str(hours) + ' ' + ['hour', 'hours'][hours > 1])
    if minutes:
        s.append(str(minutes) + ' ' + ['minute', 'minutes'][minutes > 1])
    if second:
        s.append(str(second) + ' ' + ['second', 'seconds'][second > 1])
    if len(s) == 1: return s[0]
    elif len(s) == 2: return f'{s[0]} and {s[1]}'
    elif len(s) == 3: return f'{s[0]}, {s[1]} and {s[2]}'
    elif len(s) == 4: return f'{s[0]}, {s[1]}, {s[2]} and {s[3]}'
    else: return f'{s[0]}, {s[1]}, {s[2]}, {s[3]} and {s[4]}'
