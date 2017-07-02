# -*- coding: utf-8 -*-
"""
Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits != "":
        digit = [int(d) for d in digits]
    else:
        return []

    alph = [chr(i) for i in range(97,123)]
    num_dict = {}
    start = 0
    for i in range(2,10):
        if i == 7 or i == 9:
            num_dict[i] = alph[start:start+4]
            start += 4
        else:
            num_dict[i] = alph[start:start+3]
            start += 3

    new_list = [num_dict[d] for d in digit]
    print('list:', new_list)
    temp = new_list[0]
    i = 1
    while i < len(new_list):
        temp = [m+n for n in new_list[i] for m in temp]
        i += 1    
    return temp

print(letterCombinations('23'))
print(letterCombinations('722'))