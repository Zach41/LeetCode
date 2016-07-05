#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # same as finding the peak element
        n = len(nums)

        l, r = 0, n-1

        while l+1<r:
            mid = (l+r)/2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return min(nums[l], nums[r])

s = Solution()
print s.findMin([4, 5, 6, 7, 0, 1, 2])
print s.findMin([1, 2])
print s.findMin([2, 1])
print s.findMin([5, 1, 2, 3, 4])
