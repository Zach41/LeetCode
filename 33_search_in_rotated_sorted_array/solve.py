#!/usr/bin/env python
,
# -*- coding: utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        
        pivot = self.findMin(nums, target)

        idx1 = self.bsearch(nums, target, pivot, len(nums) -1)
        idx2 = self.bsearch(nums, target, 0, pivot-1)
        if idx1 != -1:
            return idx1
        if idx2 != -1:
            return idx2
        return -1


    def findMin(self, nums, target):
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l + r) / 2
            if nums[mid] > nums[n-1]: l = mid+1
            else: r = mid

        return l

    def bsearch(self, nums, target, l, r):
        if l < 0 or r >= len(nums):
            return -1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        return -1


s = Solution()

print s.search([4, 5, 6, 7, 0, 1, 2], 6)
