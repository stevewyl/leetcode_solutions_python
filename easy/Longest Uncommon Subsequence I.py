# -*- coding: utf-8 -*-
"""
A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
"""

def findLUSlength(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    uncommon = 0
    if len(a) <= len(b):
        subsquence = [b[i:] for i in range(len(b))]
        for sub in subsquence:
            if sub not in a:
                uncommon = len(sub)
                break
        if uncommon == 0: uncommon = -1
    else:
        subsquence = [a[i:] for i in range(len(a))]
        for sub in subsquence:
            if sub not in b:
                uncommon = len(sub)
                break
        if uncommon == 0: uncommon = -1
    return uncommon

a = 'aba'
b = 'abas'
print(findLUSlength(a,b))