'''
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(0, len(nums)):
            if target - nums[i] in d:
                return d[target - nums[i]], i
            if nums[i] not in d:
                d[nums[i]] = i