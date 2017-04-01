#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dups = []
        n = len(nums)
        for val in nums:
            nums[(val - 1) % n] += n
        for (idx, val) in enumerate(nums):
            if val > 2 * n:
                dups.append(idx + 1)
        return dups


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
