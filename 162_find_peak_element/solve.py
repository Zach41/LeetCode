#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == n-1 and nums[i] > nums[i-1]:
                return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

s = Solution()
print s.findPeakElement([1, 2, 3, 4, 3])
