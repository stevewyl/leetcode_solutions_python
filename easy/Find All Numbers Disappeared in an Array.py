# -*- coding: utf-8 -*-
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    dict = {i:0 for i in range(1,n+1)}
    for num in nums:
        dict[num] += 1
    result = [num for num, value in dict.items() if value == 0]
    return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))