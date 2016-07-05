#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = None
        cnt = 0

        for num in nums:
            if n == num:
                cnt += 1
            elif cnt == 0:
                n, cnt = num, 1
            else:
                cnt -= 1
        return n

s = Solution()
print s.majorityElement([1, 1, 1, 2, 3])
