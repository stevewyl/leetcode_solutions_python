# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    else:
        x = str(x)
        l = len(x)
        count  = 0
        for i in range(int(l/2)):
            if x[i] == x[l-i-1]:
                count += 1
            else:
                continue
        if count == int(l/2):
            return True
        else:
            return False

print(isPalindrome(1234421))
        