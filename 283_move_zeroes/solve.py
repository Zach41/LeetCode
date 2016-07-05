#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        cnt_zero = 0
        while i < n:
            if nums[i] == 0:
                del([nums[i]])
                n -= 1
                cnt_zero += 1
            else:
                i += 1
        for i in range(cnt_zero):
            nums.append(0)
        self.nums = nums


s = Solution()
import pdb
pdb.set_trace()
s.moveZeroes([0, 1, 0, 3, 12])
print s.nums
