#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        if n <= 1:
            return True

        maxStep = nums[0]
        for i in range(1, n):
            if maxStep <= 0:
                return False
            maxStep -= 1
            if maxStep < nums[i]:
                maxStep = nums[i]
            if maxStep + i >= n-1:
                return True

s = Solution()
print s.canJump([2, 3, 1, 1, 4])
print s.canJump([3, 2, 1, 0, 4])
print s.canJump([1, 2])
            
            
