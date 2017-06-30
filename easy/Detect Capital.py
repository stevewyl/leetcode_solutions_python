# -*- coding: utf-8 -*-
"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False
"""

def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    count  = 0
    for w in word:
        if w.isupper():
            count += 1
    if count == 0 or count == len(word):
        return True
    elif word[0].isupper() and count == 1:
        return True
    else:
        return False

print(detectCapitalUse('USA'))
print(detectCapitalUse('FlaG'))
print(detectCapitalUse('wyl'))
print(detectCapitalUse('Python'))
print(detectCapitalUse('AliPay'))
