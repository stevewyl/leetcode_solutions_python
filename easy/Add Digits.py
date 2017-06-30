# -*- coding: utf-8 -*-
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    Flag = True
    while Flag:
        if num < 10:
            Flag = False
        else:
            num = sum([int(n) for n in str(num)])
    return num

print(addDigits(897979))