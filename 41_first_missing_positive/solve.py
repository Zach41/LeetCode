#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def firstMissingPositive(self, nums):
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == i+1 or nums[i] <= 0 or nums[i] > n:
                i += 1
            elif nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            else: i += 1
            
        i = 0
        while i < n:
            if nums[i] != i+1:
                break
            i += 1
        return i+1
                

s = Solution()

print s.firstMissingPositive([1, 2, 0])
import pdb
pdb.set_trace()
print s.firstMissingPositive([3, 4, -1, 1])

