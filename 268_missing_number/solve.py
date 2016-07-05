#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tot = (1+n)*n/2
        return tot - sum(nums)

s = Solution()
print s.missingNumber([0, 1, 3])
