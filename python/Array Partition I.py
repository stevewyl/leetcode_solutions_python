'''
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        result = 0
        if type(n) == int:
            nums = sorted(nums)
            pair = [nums[i:i+2] for i in range(0,len(nums),2)]
            for p in pair:
                result += min(p)
        return result    