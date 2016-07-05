#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt_zero = 0
        tot = 1
        for num in nums:
            if num == 0:
                cnt_zero += 1
            else:
                tot *= num

        if cnt_zero > 1:
            return [0] * len(nums)
        elif cnt_zero == 1:
            return [tot if x == 0 else 0 for x in nums]
        else:
            return [tot / x for x in nums]

s = Solution()
print s.productExceptSelf([1, 2, 3, 4])
print s.productExceptSelf([0, 1, 2, 3])
            
