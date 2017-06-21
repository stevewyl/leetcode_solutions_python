# -*- coding: utf-8 -*-
"""
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
"""

def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    output = []
    for i in range(len(findNums)):
        start_index = nums.index(findNums[i])
        print(start_index)
        targetNums = nums[start_index+1:]
        greater = [num for num in targetNums if num > findNums[i]]
        if len(greater) == 0:
            output.append(-1)
        else:
            output.append(greater[0])
    return output

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))