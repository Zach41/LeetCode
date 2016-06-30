#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        num_map = {}

        for i in range(len(nums)):
            if (target - nums[i]) in num_map.keys():
                return [num_map[target-nums[i]], i]
            else:
                num_map[nums[i]] = i

s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
print s.twoSum2([2, 7, 11, 15], 9)
