# -*- coding: utf-8 -*-
"""
Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
"""

def complexNumberMultiply(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    first = a.split('+')
    second = b.split('+')
    first[1] = first[1][:-1]
    second[1] = second[1][:-1]
    result_num = [int(f)*int(s) for f in first for s in second]
    
    real = result_num[0] - result_num[3]
    complex = result_num[1] + result_num[2]
    
    output = str(real) + '+' + str(complex) + 'i'
    
    return output