#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        pos = self.bsearch(nums, target)
        if pos == -1:
            return [-1, -1]

        i, j = pos, pos
        while j < len(nums) and target == nums[j]:
            j += 1
        while i >= 0 and target == nums[i]:
            i -= 1
        return [i+1, j-1]

    def bsearch(self, nums, target):
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid -1

        if nums[l] == target:
            return l
        return -1

s = Solution()
print s.searchRange([1], 1)
print s.searchRange([5, 7, 7, 8, 8, 10], 8)
