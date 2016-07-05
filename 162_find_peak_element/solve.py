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
            
    def findPeakElement2(self, nums):
        # O(logn) version
        n = len(nums)
        if n == 1:
            return 0
        
        l, r = 0, n-1
        while l<=r:
            mid = (l+r) / 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and \
               (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid-1]:
                r = mid-1
            else:
                l = mid+1
        
                
                
        

s = Solution()
import pdb
pdb.set_trace()
print s.findPeakElement2([1, 2])
print s.findPeakElement2([1, 2, 3, 4, 3])
