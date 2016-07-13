#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        ptr = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = nums[ptr]
                ptr += 1
        for i in range(ptr):
            del nums[0]
        # print nums
        return len(nums)

s = Solution()
print s.removeElement([3, 2, 2, 3], 3)
                
