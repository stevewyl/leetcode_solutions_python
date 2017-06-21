# -*- coding: utf-8 -*-
"""
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    zero_index = [ii for ii,v in enumerate(nums) if v == 0]
    zero_index.insert(0,0)  
    zero_index.append(len(nums)-1)
    diff = []
    if len(zero_index) > 2:
        for i in range(1,len(zero_index)):
            if i == 1 or i == len(zero_index)-1:
                diff.append(zero_index[i] - zero_index[i-1])
            else:
                diff.append(zero_index[i] - zero_index[i-1] - 1)
    else:
        diff = [len(nums)]
    return max(diff)
            