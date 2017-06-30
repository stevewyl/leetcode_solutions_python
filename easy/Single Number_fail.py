# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:08:43 2017

@author: stevewyl
"""

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    output = []
    d = {n: nums.count(n) for n in set(nums)}
    for num in d:
        if d[num] == 1:
            output.append(num)
    return output

nums = [i for i in range(10000)]

output = singleNumber(nums)