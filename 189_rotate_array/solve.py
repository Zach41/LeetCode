#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        num1 = nums[:n-k]
        num2 = nums[n-k:]

        new = num2+num1

        for i in range(len(new)):
            nums[i] = new[i]

        self.nums = nums
        

S = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
import pdb
pdb.set_trace()
print s.nums
