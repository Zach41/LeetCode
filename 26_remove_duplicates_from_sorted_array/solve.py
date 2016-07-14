#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n

        i, ptr = 0, 1

        while ptr < n:
            if nums[i] != nums[ptr]:
                i += 1
                nums[i] = nums[ptr]
            ptr += 1
        return i+1
s = Solution()
import pdb
pdb.set_trace()
print s.removeDuplicates([1, 1, 2])
print s.removeDuplicates([1, 1, 1, 3, 3, 4, 5])
            
        
