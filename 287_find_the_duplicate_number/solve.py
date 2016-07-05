#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # just quick sort
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
    def findDuplicate2(self, nums):
        # O(n) version
        n = len(nums)-1
        found = 0
        for i in range(len(nums)):
            if nums[i] > 2*n:
                return i
            elif nums[i] <= n:
                nums[nums[i]] += n
            else:
                nums[nums[i] - n] += n

        for i in range(len(nums)):
            if nums[i] > 2*n:
                return i
s = Solution()
import pdb
pdb.set_trace()
print s.findDuplicate2([1, 3, 4, 2, 2])
print s.findDuplicate2([1, 2, 3, 3, 4])


